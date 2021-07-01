class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.n = len(candidates)
        self.result =[]
        self.helper(candidates, 0, [], target)
        return self.result
    
    def helper(self, candidates, index, path, target):
        #base
        if target < 0 or index == self.n: return 
        if target == 0:
            self.result.append(path)
            return
        
        
        #logic
        #case 1: Not choosing the element
        self.helper(candidates, index+1, path.copy(), target)
        #case 2: choosing the element
        path.append(candidates[index])
        #recursive call -> decreasing the target and on the same index
        self.helper(candidates, index, path.copy(), target-candidates[index])

#Time complexity is O(2^n) since we are making 1 of 2 decisions at each node
#Space complexity is O(n) as we are storing a new array list at each each recursive call