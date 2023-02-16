def solution(nums):
    answer = len(nums) / 2

    nums = set(nums) # nums에 들어있는 정수 종류의 개수

    if answer > len(nums): # nums에 들어있는 정수 종류의 개수가 더 작아?
        answer = len(nums) # answer = nums에 들어있는 정수 종류의 개수

    return answer