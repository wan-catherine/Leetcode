import collections
from typing import List

"""
Compare subtree, we can encode the subtree: key(left) + node.val + key(right).
But this problem, the key should not contains itself. So we need to include the subtree's root's val. 

Similar as problem 652.
"""
class Trie:
    def __init__(self, v):
        self.val = v
        self.children = {}

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie('/')
        for path in paths:
            cur = root
            for c in path:
                if c not in cur.children:
                    cur.children[c] = Trie(c)
                cur = cur.children[c]
        num = 1
        node_2_id = collections.defaultdict(int)
        key_2_id = collections.defaultdict(int)
        count = collections.defaultdict(int)
        def get_id(node):
            nonlocal num
            key = []
            for k, child in node.children.items():
                key.append(str(get_id(child)))
                key.append(child.val)
            # here needs to sort, or test_delete_duplicate_folder_5 will be failed.
            skey = '#'.join(sorted(key))
            if skey not in key_2_id:
                key_2_id[skey] = num
                num += 1
            count[key_2_id[skey]] += 1
            node_2_id[node] = key_2_id[skey]
            return key_2_id[skey]
        get_id(root)
        res = []
        def dfs(node, cur):
            nid = node_2_id[node]
            if node.children and count[nid] > 1:
                return
            if node.val != '/':
                cur.append(node.val)
                res.append(cur[:])
            for k, child in node.children.items():
                dfs(child, cur[:])
            if node.val != '/':
                cur.pop()
        dfs(root, [])
        return res
