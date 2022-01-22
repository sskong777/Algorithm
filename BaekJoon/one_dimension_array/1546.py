n = int(input())

list_score = list(map(int, input().split()))
max_score = max(list_score)

list_modi_score = []

for i in list_score:
    # if i == max_score:
    #     list_modi_score.append(i)
    # else:
    modi_score = (i/max_score)*100
    list_modi_score.append(modi_score) 


# print(list_modi_score)
print(sum(list_modi_score)/n)