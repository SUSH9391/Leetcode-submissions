#!/usr/bin/env python3
import json, re, time
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]
SOLUTIONS = ROOT / 'leetcode-solutions'
TOPICS = ROOT / 'leetcode-topics'
CACHE_FILE = ROOT / '.leetcode-metadata.json'
STATS_FILE = ROOT / 'leetcode-stats.json'

QUERY = '''
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    title
    titleSlug
    difficulty
    topicTags { name slug }
  }
}
'''

def safe_name(name):
    name = name.lower().strip().replace('&', 'and')
    name = re.sub(r'[^a-z0-9]+', '-', name)
    return name.strip('-') or 'uncategorized'

def fetch_problem(slug):
    payload = json.dumps({'query': QUERY, 'variables': {'titleSlug': slug}}).encode()
    req = Request('https://leetcode.com/graphql', data=payload, headers={
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 LeetCode-GitHub-Topic-Indexer'
    }, method='POST')
    with urlopen(req, timeout=20) as response:
        data = json.loads(response.read().decode())
    question = data.get('data', {}).get('question')
    if not question:
        raise RuntimeError('No LeetCode question returned for ' + slug)
    return {
        'id': int(question['questionFrontendId']),
        'title': question['title'],
        'slug': question['titleSlug'],
        'difficulty': question['difficulty'],
        'topics': [{'name': t['name'], 'slug': t['slug']} for t in question.get('topicTags', [])]
    }

def load_cache():
    try:
        return json.loads(CACHE_FILE.read_text(encoding='utf-8')) if CACHE_FILE.exists() else {}
    except json.JSONDecodeError:
        return {}

def problem_dirs():
    if not SOLUTIONS.exists(): return []
    out = []
    for p in SOLUTIONS.iterdir():
        if p.is_dir():
            m = re.match(r'^(\d+)-(.+)$', p.name)
            if m: out.append((int(m.group(1)), m.group(2), p))
    return sorted(out, key=lambda x: x[0])

def write_cache(cache):
    CACHE_FILE.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding='utf-8')

def fetch_missing(cache, dirs):
    for number, slug, _ in dirs:
        key = str(number)
        if key in cache and cache[key].get('slug') == slug: continue
        print(f'Fetching metadata: {number} - {slug}')
        try:
            cache[key] = fetch_problem(slug)
            write_cache(cache)
            time.sleep(0.25)
        except Exception as exc:
            print(f'WARNING: {number}-{slug}: {exc}')

def build(cache, dirs):
    TOPICS.mkdir(exist_ok=True)
    topic_map = {}
    difficulty = {'Easy': [], 'Medium': [], 'Hard': []}
    indexed = []
    for number, slug, path in dirs:
        m = cache.get(str(number))
        if not m: continue
        item = {'id': number, 'title': m.get('title', slug), 'difficulty': m.get('difficulty', 'Unknown'), 'path': path.relative_to(ROOT).as_posix(), 'topics': m.get('topics', [])}
        indexed.append(item)
        if item['difficulty'] in difficulty: difficulty[item['difficulty']].append(item)
        for topic in item['topics']: topic_map.setdefault(topic['name'], []).append(item)
    for items in topic_map.values(): items.sort(key=lambda x: x['id'])
    for topic, items in sorted(topic_map.items(), key=lambda x: x[0].lower()):
        lines = [f'# {topic}', '', f'**Problems solved:** {len(items)}', '', '| # | Problem | Difficulty |', '|---:|---|---|']
        for item in items:
            lines.append(f"| {item['id']} | [{item['title']}](../{item['path']}) | {item['difficulty']} |")
        (TOPICS / (safe_name(topic) + '.md')).write_text('\n'.join(lines) + '\n', encoding='utf-8')
    STATS_FILE.write_text(json.dumps({'total_indexed': len(indexed), 'difficulty': {k: len(v) for k,v in difficulty.items()}, 'topics': {k: len(v) for k,v in topic_map.items()}}, indent=2), encoding='utf-8')
    lines = ['# LeetCode Submissions', '', 'Automatically synced from LeetCode and organized by LeetCode topic.', '', '## Progress', '', f'**Total indexed:** {len(indexed)}', '', '| Difficulty | Solved |', '|---|---:|']
    for d in ('Easy','Medium','Hard'): lines.append(f'| {d} | {len(difficulty[d])} |')
    lines += ['', '## Topics', '', '| Topic | Problems |', '|---|---:|']
    for topic, items in sorted(topic_map.items(), key=lambda x: (-len(x[1]), x[0].lower())): lines.append(f'| [{topic}](leetcode-topics/{safe_name(topic)}.md) | {len(items)} |')
    lines += ['', '## Structure', '', 'Each problem remains in one canonical folder under leetcode-solutions/. Topic pages link to those folders, so solutions are never duplicated.', '']
    (ROOT / 'README.md').write_text('\n'.join(lines), encoding='utf-8')

def main():
    cache = load_cache()
    dirs = problem_dirs()
    print(f'Found {len(dirs)} solution folders.')
    fetch_missing(cache, dirs)
    write_cache(cache)
    build(cache, dirs)

if __name__ == '__main__': main()