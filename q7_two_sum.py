'''
두개의 숫자의 합을 표현할 수 있는 조합을 찾아보자.
예시)
nums = [2,7,11,15], target = 9
출력 : [0,1]

'''
''' Solution 1 - Brute force
nums = [2,7,11,15]
target = 9
def two_sum(nums:list[int],target) -> list:
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
print(two_sum(nums,target))
'''
# Solution 2 - 첫번째 수를 뺀 결과를 키로 저장 , 훨씬빠름
def twosum(nums:list[int],target:int)->list:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    for i,num in enumerate(nums):
        if target-num in nums_map and i!=nums_map[target-num]:
            return[i,nums_map[target-num]]


