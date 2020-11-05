class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = {i: set() for i in range(n)}

        for e in edges:
            a, b = e[0], e[1]
            graph[a].add(b)
            graph[b].add(a)

        res = set(graph.keys())
        while len(res) > 2:
            q = deque()
            for k in graph:
                if len(graph[k]) == 1 and k in res:
                    q.append(k)
            for leaf in q:
                res.remove(leaf)
                (parent,) = graph[leaf]
                graph[parent].remove(leaf)
        return res
