'''
한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
입력 : [7,1,5,3,6,4]
출력 : 5
현재 값을 나타내는 포인터가 있고, 
이전값들 중 min 값을 저장하는 variable이 있다.

'''
def best_time(nums:list[int])->int:
    profit = [0] * len(nums)
    min_value = 5000
    for i in range(len(nums)):
        if nums[i] < min_value:
            min_value = nums[i]
        profit[i] = nums[i] - min_value
    ans = max(profit)
    return ans
input = [7,1,5,3,6,4]

print(best_time(input))
