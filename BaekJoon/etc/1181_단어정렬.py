# def equal_len(word1,word2):
#     for i in range(len(word1)):
#         if word1[]


N = int(input())
word_list = []
for i in range(N):
    word_list.append(input())

# 중복된 값 지우기
word_arr = []   # 새로운 배열 생성
for i in word_list:
    if i not in word_arr:
        word_arr.append(i)
N = len(word_arr)

# 단어길이로 오름차순 정렬
for i in range(N):
    for j in range(i+1,N):
        if len(word_arr[i]) > len(word_arr[j]):
            word_arr[i],word_arr[j] = word_arr[j],word_arr[i]
        if len(word_arr[i]) == len(word_arr[j]):
            for k in range(len(word_arr[i])):
                if word_arr[i][k] > word_arr[j][k]:
                    word_arr[i], word_arr[j] = word_arr[j], word_arr[i]
                    break
                break
for i in range(N):
    print(word_arr[i])
