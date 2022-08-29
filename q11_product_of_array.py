'''
배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라. 
입력 : [1,2,3,4]
출력 : [24,12,8,6]
주의사항 - 나눗셈을 하지 말고 구해라. 

'''
def ProductExceptself(nums:list[int]) -> list[int]:
    ans = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i==j:
                pass
            else:
                ans[i] = ans[i]*nums[j]
    return ans
input = [1,2,3,4]
print(ProductExceptself(input))