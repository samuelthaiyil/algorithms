def combinationSum(candidates, target):
    results = []

    def dfs(start, remain, comb):

        # if remain is 0, we found a match append it to results
        if remain == 0:
            results.append(list(comb))
            return
        # if remain is negative, we overshot - return
        elif remain < 0:
            return    

        # backtracking
        for i in range(start, len(candidates)):
            curr = candidates[i]

            # append the current candidate
            comb.append(curr)

            # backtrack on the 
            dfs(i, remain - curr, comb)
            
            # remove the current candidate
            comb.pop()

    # starts the backtrack process
    dfs(target, [], 0)

    return results
    
