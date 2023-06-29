def solution(participant, completion):

    hash_dict = {}
    sumHash = 0

    # 1. Hash : Participant의 dictionary 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        print(hash(part))
        hash_dict[hash(part)] = part
        print("has_dict" ,hash_dict)
        sumHash += hash(part)
        print(sumHash)

    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        print(hash(comp))
        sumHash -= hash(comp)

    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다.

    return hash_dict[sumHash]