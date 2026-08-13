class SegmentTreeNode:
    def __init__(self, left_char='', right_char='', prefix=0, suffix=0, max_len=0):
        self.left_char = left_char
        self.right_char = right_char
        self.prefix = prefix
        self.suffix = suffix
        self.max_len = max_len

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        tree = [SegmentTreeNode() for _ in range(4 * n)]
        s_list = list(s)

        def merge(left_node: SegmentTreeNode, right_node: SegmentTreeNode, left_len: int, right_len: int) -> SegmentTreeNode:
            res = SegmentTreeNode()
            res.left_char = left_node.left_char
            res.right_char = right_node.right_char
            
            res.prefix = left_node.prefix
            if left_node.prefix == left_len and left_node.right_char == right_node.left_char:
                res.prefix += right_node.prefix
                
            res.suffix = right_node.suffix
            if right_node.suffix == right_len and right_node.left_char == left_node.right_char:
                res.suffix += left_node.suffix
                
            res.max_len = max(left_node.max_len, right_node.max_len)
            if left_node.right_char == right_node.left_char:
                res.max_len = max(res.max_len, left_node.suffix + right_node.prefix)
                
            return res

        def build(node: int, start: int, end: int):
            if start == end:
                ch = s_list[start]
                tree[node] = SegmentTreeNode(ch, ch, 1, 1, 1)
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1], mid - start + 1, end - mid)

        def update(node: int, start: int, end: int, idx: int, char: str):
            if start == end:
                s_list[idx] = char
                tree[node] = SegmentTreeNode(char, char, 1, 1, 1)
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node, start, mid, idx, char)
            else:
                update(2 * node + 1, mid + 1, end, idx, char)
            tree[node] = merge(tree[2 * node], tree[2 * node + 1], mid - start + 1, end - mid)

        build(1, 0, n - 1)
        
        ans = []
        for q_char, q_idx in zip(queryCharacters, queryIndices):
            if s_list[q_idx] != q_char:
                update(1, 0, n - 1, q_idx, q_char)
            ans.append(tree[1].max_len)
            
        return ans
