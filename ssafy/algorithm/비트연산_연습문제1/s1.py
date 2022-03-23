lst = [
    '0000000111',
    '1000000110',
    '0000011110',
    '0110000110',
    '0001111001',
    '1110011111',
    '1001100111',
]

arr = ''.join(lst)  # 하나의 문자열로 만듦

length = len(arr) // 7

for i in range(length):
    res = 0         # 7 비트의 값
    for j in range(i*7, i*7+7):
        res = res * 2 + int(arr[j])
    print(res, end=' ')
