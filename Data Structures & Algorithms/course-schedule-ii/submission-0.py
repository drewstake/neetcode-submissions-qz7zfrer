class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # map each course to prereq list
        prereq = {}
        output = []

        for c in range(numCourses):
            prereq[c] = []
        
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        

        # visitSet = all courses along the curr DFS path

        visit = set()
        done = set()

        def dfs(crs):
            if crs in visit:
                return False
            if crs in done:
                return True
            
            visit.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)

            done.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output