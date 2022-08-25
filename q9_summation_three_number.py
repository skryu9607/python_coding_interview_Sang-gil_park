'''
배열을 입력받아서 합으로 0을 만들 수 있는 3개의 elements를 출력하라.
입력 :  nums = [-1,0,1,2,-1,-4]

'''
# Solution. Using Two pointer
nums = [-1,0,1,2,-1,-4]
def threesum(nums:list[int]) ->list[list[int]]:
    results = []
    nums.sort()
    print(nums)
    for i in range(len(nums)-2):
        # 중복체크
        if i>0 and nums[i]==nums[i-1]:
            continue
        left,right = i + 1, len(nums)-1
        while left<right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum >0:
                right -= 1
            else:
                results.append([nums[i],nums[left],nums[right]])
                while left<right and nums[left] ==  nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1

    return results
print(threesum(nums))






