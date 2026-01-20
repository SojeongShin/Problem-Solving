import re
pattern = r'[^a-z0-9_.-]'

def solution(new_id):
    subId = new_id.lower()
    subId = re.sub(pattern, '', subId)
    subId = re.sub(r'\.+', '.', subId)

    # stage 4 
    subId = subId.strip('.')

    if len(subId) == 0:
        subId = "a"

    if len(subId) >= 16:
        subId = subId[:15].strip('.')

    while len(subId) < 3:
        subId += subId[-1]

    return subId