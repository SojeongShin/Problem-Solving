from itertools import product

def match(user, ban):
    if len(user) != len(ban):
        return False
    for u, b in zip(user, ban):
        if b == '*':
            continue
        if u != b:
            return False
    return True

def solution(user_id, banned_id):
    candidates = []
    for ban in banned_id:
        tmp = []
        for user in user_id:
            if match(user, ban):
                tmp.append(user)
        candidates.append(tmp)

    result = set()
    for p in product(*candidates):
        if len(set(p)) == len(p):   # 중복 user 제거
            result.add(frozenset(p))  # 순서 무시

    return len(result)