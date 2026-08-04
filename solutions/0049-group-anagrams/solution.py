class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # one way to group the words together was to use sorting and sorting all the strings inside the main string and group the original string and return 
        # seciond way is to count the number of each letters present in the string inside the string and add them to the hashmap with similar values or count

        res = defaultdict(list) #{[1e,1a,1t] : ['eat', 'ate' ] }
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1 # convert to 1 based index so that we get the count
            # Convert list to a tuple so it can be used as a dict key
            res[tuple(count)].append(s)
        return list(res.values())
