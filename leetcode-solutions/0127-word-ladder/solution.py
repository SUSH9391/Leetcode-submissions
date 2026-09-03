from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        nei = defaultdict(list)
        wordList.append(beginWord)
        #since we are asked to get the shortest path we use bfs so we need a adj list
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*"+ word[j+1:]
                nei[pattern].append(word)
        visit = set([beginWord])
        q=deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j]+"*"+word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
                    nei[pattern] = []
            res += 1
        return 0


