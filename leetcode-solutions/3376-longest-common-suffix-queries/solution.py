class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.best = (float('inf'), float('inf'))

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        global_best = (float('inf'), float('inf'))
        for i, word in enumerate(wordsContainer):
            w_len = len(word)
            if (w_len, i) < global_best:
                global_best = (w_len, i)
        
        # Build the Trie
        for i, word in enumerate(wordsContainer):
            node = root
            w_len = len(word)
            # Update root
            if (w_len, i) < node.best:
                node.best = (w_len, i)
            
            for char in reversed(word):
                idx = ord(char) - ord('a')
                if not node.children[idx]:
                    node.children[idx] = TrieNode()
                node = node.children[idx]
                # Update current node 
                if (w_len, i) < node.best:
                    node.best = (w_len, i)
        
       
        ans = []
        for query in wordsQuery:
            node = root
            # If no match
            best_idx = global_best[1]
            
            for char in reversed(query):
                idx = ord(char) - ord('a')
                if node.children[idx]:
                    node = node.children[idx]
                    best_idx = node.best[1]
                else:
                    break
            ans.append(best_idx)
            
        return ans
