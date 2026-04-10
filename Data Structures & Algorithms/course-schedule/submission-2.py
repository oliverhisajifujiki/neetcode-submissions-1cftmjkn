class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #first idea is to use a dictionary where key is the course and value is the prereq
        preDict = {i : [] for i in range(numCourses)}

        for course, prereq in prerequisites: #populate the dictionary 
            preDict[course].append(prereq)

        visited = set()
        #lets add to this visited set, if we visit something twice we know that we are not copmletable
        def dfs(course): #we start at a course, we visit all its pre reqs, , if there is a repeat we know there is a cycle
                    #if there is no repeat then we know there is a beginning, therefore the courses must be completable
            if course in visited:
                return False
            
            if preDict[course] == []: #therefore there are no prereqs
                return True #this course is copmletable
            
            #if we are here we know that there are prereqs, lets 
            # add the current course we are in to visited and traverse the prereqs to see if there is a cycle
            visited.add(course)

            for prereq in preDict[course]:
                if not dfs(prereq):
                    return False
            
            #if we are here we visited all prereqs and they were completable 
            #lets set thiscourses prereqs to nothing 
            preDict[course] == []
            #and we can also remove it from the visited set
            visited.remove(course)

            return True
            
        #if we have returned from here we did all our prereqs 
        for course in range(numCourses):
            if not dfs(course):
                return False
            
        #went through all courses we can return true here

        return True 
        