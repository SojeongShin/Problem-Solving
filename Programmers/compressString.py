def solution(s):
    n = len(s)
    if n == 1:
        return 1

    best = n  # 압축 안 했을 때 길이

    for unit in range(1, n // 2 + 1):
        compressed_len = 0

        prev = s[:unit]
        cnt = 1

        for i in range(unit, n, unit):
            cur = s[i:i+unit]
            if cur == prev:
                cnt += 1
            else:
                # prev 덩어리 확정
                if cnt > 1:
                    compressed_len += len(str(cnt))
                compressed_len += len(prev)

                prev = cur
                cnt = 1

        # 마지막 덩어리 처리
        if cnt > 1:
            compressed_len += len(str(cnt))
        compressed_len += len(prev)

        best = min(best, compressed_len)

    return best
