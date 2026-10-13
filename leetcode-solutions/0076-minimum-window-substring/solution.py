from collections import Counter


class Solution:

  def minWindow(self, s: str, t: str) -> str:
    if not t or not s:
      return ""

    # Dictionary to keep track of all unique characters in t and their counts
    dict_t = Counter(t)
    required = len(dict_t)

    # Filtered list of characters in s that are present in t, along with their indices
    filtered_s = []
    for i, char in enumerate(s):
      if char in dict_t:
        filtered_s.append((i, char))

    l = 0
    r = 0
    formed = 0
    window_counts = {}

    # (window length, left index, right index)
    ans = float("inf"), None, None

    while r < len(filtered_s):
      character = filtered_s[r][1]
      window_counts[character] = window_counts.get(character, 0) + 1

      if window_counts[character] == dict_t[character]:
        formed += 1

      # Try and contract the window until it ceases to be 'desirable'
      while l <= r and formed == required:
        character = filtered_s[l][1]

        # Save the smallest window until now
        end = filtered_s[r][0]
        start = filtered_s[l][0]
        if end - start + 1 < ans[0]:
          ans = (end - start + 1, start, end)

        # The character at the position pointed by the `l` pointer is no longer a part of the window
        window_counts[character] -= 1
        if window_counts[character] < dict_t[character]:
          formed -= 1

        l += 1

      r += 1

    return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
