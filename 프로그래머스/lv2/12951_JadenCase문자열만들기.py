def solution(s):
    answer = []
    new_s = s.split(" ")
    # 공백이 들어갈 경우 대비(ex. 3people     Unfollwed Me)
    # split()말고, split(" ")이라고 공백 하나만 들어가게 할 것

    for x in new_s:
        answer.append(x.lower().capitalize())
    return ' '.join(answer)