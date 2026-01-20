def solution(today, terms, privacies):
    answer = []
    
    today = list(map(int, today.split('.'))) 
        
    for j in range(len(privacies)):
        p_date, p_content = privacies[j].split()
        p_date = list(map(int, p_date.split('.')))
        
        for i in terms:
            t_content, t_month = i.split()
            remain_month = 0
            remain_days = 0
            if p_content == t_content:
                remain_month = 12*(today[0] - p_date[0]) + today[1] - p_date[1]
                remain_days = remain_month * 28 + today[2] - p_date[2]

                if remain_days >= int(t_month)*28:
                    answer.append(j+1)

    return answer
