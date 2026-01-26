from itertools import combinations

def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])
    candidate_keys = []

    # 1개 컬럼부터 전체 컬럼까지 조합
    for r in range(1, n_col + 1):
        for cols in combinations(range(n_col), r):

            # 유일성 검사
            tuples = set()
            for row in relation:
                tuples.add(tuple(row[c] for c in cols))
            if len(tuples) != n_row:
                continue

            # 최소성 검사
            is_minimal = True
            for key in candidate_keys:
                if set(key).issubset(set(cols)):
                    is_minimal = False
                    break

            if is_minimal:
                candidate_keys.append(set(cols))

    return len(candidate_keys)
