# word = input()
# up_word = word.upper()
# dict = {}
# res = []
# for i in up_word:
#     dict[i] = up_word.count(i)

# for i in dict:
#     if dict[i] == max(dict.values()):
#         res.append(i)
# if len(res) > 1:
#     print('?')
# elif len(res) == 1:
#     print(''.join(res))


word = input().upper()
word_set = list(set(word))
res = []

for i in word_set:
    res.append(word.count(i))

if res.count(max(res)) > 1:
    print('?')
else:
    print(word_set[res.index((max(res)))])
