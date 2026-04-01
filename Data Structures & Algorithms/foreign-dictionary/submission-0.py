class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #we will use a graph to store directed edges:
            #a -> b means "a must come before b"
        
        #we first create a node for each of the letters we see
        graph = {c: set() for word in words for c in word}
        #this is saying for each char we sede create a dictionary element
            #where the key is the char
            #and the value is the outgoing edges 

        #need another dictionary
        indegree = {c: 0 for c in graph}
        #here key again is each letter we see
            #value is the amount of incoming edges
        
        #if the indegree is 0 (because "x -> y" means x before y)
            #this means that no nothing needs to come before it
            #therefore we populate indegree
            #we then look for anything with indegree 0 (say b)
            #place these chars in order into a string
                #the string represents the ordering required
            #once a char (say b) has been placed into the string
                #we can indegree[a] -= 1 , for all a s.t.
                    #there exists a (dir) edge from b to a


        #we have to build the adjacency graph

        #we are going to assume that only adjacent words matter, because the list is already sorted word wise
        for i in range (len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            #edge case 
                #if len(w1) > len(w2) and w1 starts with w2
                #this is an impossible ordering
                #e.g:
                    #["abc", "ab"]
                    #no alphabet rules can make "abc" come before "ab"
            if len(w1) > len(w2) and w1[:len(w2)] == w2:
                return ""
            
            #compare the 2 words char by char
            #where they differ gives us insight on ordering rule
            minLen = min(len(w1),len(w2))
            for j in range(minLen):
                if w1[j] != w2[j]:
                    #the we know a rule! 
                        #w1[j] must come before w2[j]
                    # add edge (unless already there)
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    
                    #once we find first difference lets stop
                    #later characters will not give us extra info (giving that we are only looking at this pair)
                    break

        #topological sort (kahn's alg)
        from collections import deque

        q = deque() #double ended queue
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)

        order = []

        while q:
            #take a charcter whose prereq are all satisfied
            c = q.popleft()
            order.append(c)

            #remove its outgoing edges
            for neighbour in graph[c]:
                indegree[neighbour] -= 1

                #if now this neighbour has no indegree its ready to be put in the order
                if indegree[neighbour] == 0:
                    q.append(neighbour)
                
        #if not every character placed, there must be a cycle
            #e.g a->b and b->a
        #no valid ordering exists
        if len(order) != len(graph):
            return ""
        
        return "".join(order) #converts list of characters into one string
            
            
