#valid tree satisfies two things
    #no cycles
    #connected
    #since graph undirected important subfact: 
        #need exactly n-1 edges
    #then we just check that we can visit 

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #quick edge check
        if len(edges) != n - 1:
            return False
        
        #build an adjacency list
        #this will be done via dictionary 
            #key: node label (say x)
            # value: node labels that are adjacent to x
        graph = {i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        #keep a visited set, if visited sees all n nodes we are a valid tree
        def dfs(node):
            if node in visited: #we've alr seen this node
                return 
            
            #we have visited this node
            visited.add(node)

            for neighbour in graph[node]:
                dfs(neighbour)

        
        dfs(0) #start from node 0

        return len(visited) == n 







