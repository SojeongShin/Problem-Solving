from collections import deque

def solution(begin, target, words):
    if target not in words: return 0
    
    q = deque([(begin, 0)])
    visited = set()
    
    while q:
        curr, count = q.popleft()
        
        if curr == target:
            return count
            
        for word in words:
            if word not in visited:
                diff = sum(1 for c1, c2 in zip(curr, word) if c1 != c2)
                if diff == 1:
                    visited.add(word)
                    q.append((word, count + 1))
    return 0