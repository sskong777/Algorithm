# 스위치 갯수, 스위치 상태, 학생 수 입력받기
switch_ea = int(input())
switch = list(map(int, input().split()))
students = int(input())

# 학생 수 만큼 반복
for i in range(students):
    # 학생 별 성별과 스위치 갯수 입력받기
    gender ,switch_num =  map(int, input().split())
    # 성별이 남자라면
    if gender == 1:
        # switch_num의 배수만 바꿔주면 되므로 switch_num의 인덱스번호 부터 switch_num씩 증가시키며(배수) 반복문을 돈다
        for i in range(switch_num-1, switch_ea, switch_num):
            switch[i] = int(not switch[i])      # switch_num의 배수에 있는 스위치 상태로 반대로 바꾼뒤 정수로 변환해서 저장
    # 성별이 여자라면
    elif gender == 2:
        #s1, s2는 switch_num 앞 뒤 스위치
        s1 = switch_num - 2
        s2 = switch_num 
        switch[switch_num-1] = int(not switch[switch_num-1])  # switch_num번 스위치는 어쨌든 상태가 바뀜

        # s1과s2가 인덱스 범위 내에 있고, s1과s2의 상태가 같으면
        while s1 >= 0 and s2 < switch_ea and switch[s1] == switch[s2]:
            # s1과s2의 스위치 상태를 바꿔준다.
            switch[s1], switch[s2] = int(not switch[s1]) ,int(not switch[s2])
            s1 -= 1
            s2 += 1
            

# 20개씩 출력하기
for i in range(len(switch)):
    print(int(switch[i]), end=' ')  
    if (i+1)%20 == 0:  
        print()

        # while True:

        #     if switch[s1] != switch[s2]:
        #         switch[switch_num-1] = int(not switch)
        #         break
        #     else:
        #         s1 -= 1
        #         s2 += 1
        #         if s1 < 0 or s2 > switch_ea-1:
        #             break
        #         if switch[s1] == switch[s2]:
        #             switch[switch_num-1] = int(not switch)
        #             switch
