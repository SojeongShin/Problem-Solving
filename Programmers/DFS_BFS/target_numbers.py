def solution(numbers, target):
    answer = 0
    n = len(numbers)
    
    def dfs(size, curr):
        nonlocal answer
        
        if size == n:
            if curr == target:
                answer += 1
            return
                
        dfs(size + 1, curr + numbers[size])
        dfs(size + 1, curr - numbers[size])
            
    dfs(0, 0)
    
    return answer

    