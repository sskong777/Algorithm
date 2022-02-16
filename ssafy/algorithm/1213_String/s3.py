# search_str = 'ti'
# str = 'Starteatingwellwiththeseeighttipsforhealthyeating,whichcoverthebasicsofahealthydietandgoodnutrition'

import sys
sys.stdin = open('input.txt', encoding='utf-8')

for tc in range(1,11):
    tc_num = int(input())
    search_str = input()
    str = input()
    count = 0
    for i in range(len(str)):
        if str[i:i+len(search_str)] == search_str:
            count += 1
    print("#{} {}".format(tc, count))