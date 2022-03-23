#2. 16진수

def Bbit_print(i):
	output = ''
    # i의 j번 비트가 1인지 여부를 검사
	for j in range(7, -1, -1):
		output += '1' if i & (1 << j) else '0'
	print (output, end=' ')

a = 0x20 # 0x -> 16진수
x = 0x01020304
# print ("%d = " % a, end='')
print(f'{a} = ', end='')
Bbit_print(a) # 16진수 -> 2진수 변환
print()

print(f'0x{x:08x} ', end='')
# print ("0x%X = " % x, end='')
"""
4개 byte -> 32bit
0번 bit ~ 31번 bit 중에서 0번 bit ~ 7번비트까지 1이고 나머지는 모두 0

0xff -> | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
"""
for i in range(0, 4):
    # 8칸 -> 16칸 -> 24칸 -> 32칸 오른쪽 shift
    # 8칸 이동? 8번 bit -> 0번 비트 자리로 이동
    # 앞 쪽은 신경쓰지 않아도 됨
    # print(f'\n < {x>>i*8:08x} / {x>>i*8:032b} > => ', end=' ')
    # 뒤에 8 비트를 비교해서 출력
    Bbit_print((x >> i*8) & 0xff)
    # print 표준 입출력 형식으로 작성해도 동일한 결과 출력
    # print(f'{x>>i*8 & 0xff :08b}')

"""
0x01020304 = 0b 00000001 00000010 00000011 00000100

00000100 -> 04 
00000011 -> 03
00000010 -> 02
00000001 -> 01
"""