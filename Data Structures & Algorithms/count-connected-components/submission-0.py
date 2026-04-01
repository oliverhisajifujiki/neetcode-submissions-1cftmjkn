class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #build adjacency list from undirected edges
        graph = {i: [] for i in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        #keep visited set and a counter for the number of components
        visited = set()
        componentCount = 0

        #loop through all nodes
        def dfs(node):
            if node in visited:
                return #already seen it just go to next
                
            visited.add(node) #we haven't seen node yet add it to our set

            for neighbour in graph[node]:
                dfs(neighbour)

        for node in range(n):
            if node not in visited:
                componentCount += 1
                dfs(node)
        
        return componentCount



        