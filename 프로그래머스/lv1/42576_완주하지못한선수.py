# 해쉬로 풀이

def solution(participant, completion):

    hash_dict = {}
    sumHash = 0

    # 1. Hash : Participant의 dictionary 만들기
    # 2. Participant의 sum(hash) 구하기
    for part in participant:
        hash_dict[hash(part)] = part
        sumHash += hash(part)

    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sumHash -= hash(comp)

    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다.

    return hash_dict[sumHash]

# participant               completion          return
# ["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"