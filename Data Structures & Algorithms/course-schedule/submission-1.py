#Preliminary thinking
    #this one we are looking to complete numCourses
    # we have "roadmap" of how to complete courses
    #as some of them will require prerequisites 
    #[1,0] means you must take course 0 before taking course 1
        #for graphs this means directed graph 0 -> 1 
        #what we are looking for if there is any sort of 
        #course curriculum that will not work
        #an example of something that will not work 
            #[1,0], [2,1], [0,2]
            #this reads as 0 -> 1 -> 2 -> 0
        #not possible as all courses require a prereq that you do not have
        #what this looks like graphically is we are simply looking 
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #build a dictionary key: course / value: pre reqs
        preDict = {i: [] for i in range(numCourses)} #i is courseID / [] is what we will fill the pre req with
        #the main idea is via this dictionary
        #we will DFS search all nodes, and if 
        #the pre req is finishable it gets removed from the values of i

        #fill in the dictionary
        for course, prereq in prerequisites:
            preDict[course].append(prereq)
        
        #this cirriculum is not completable if, there exists a directed cycle
        #therefore lets visit all nodes to "build" our graph and look for
        #directed cycles we do this by doing DFS and if we have alr visited a node
        #we know we have a cycle

        visited = set()
        def dfs(course):
            #if we see a course already in visited
            if course in visited:
                return False
        
            #if this course has no prereqs
            if preDict[course] == []:
                return True
            
            #if we are here basic checks out of the way
            #lets add course to set to keep track of cycle
            visited.add(course)

            #now we check if course's prereq's are finishable (not part of directed cycle)
            for prereq in preDict[course]:
                if not dfs(prereq):
                    return False
            
            #if we are here we have checked all prereqs of course
            #and they are finishable
            #lets mark this course as no prereqs (as we know it can be completed)
            #if we visit it in the future we know not to worry about it
            preDict[course] = []
            #also we no longer have to keep track of it in visited
            visited.remove(course)

            return True
        
        #to see if any node is part of a directed cycle sadly we have to check every node
        #as we can have disconnected cycles somewhere
        for course in range(numCourses):
            if not dfs(course):
                return False

        #if we are here we've gone thru every node
        return True