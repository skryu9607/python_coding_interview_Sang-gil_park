'''
n개의 페이를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라. 
입력 : [1,4,3,2]
출력 : 4
풀이 : 정렬한 후에 짝수끼리 더하는게 어떨까?
'''
def arrayPartition(nums: list[int]) -> int:
    return sum(sorted(nums)[::2])
input = [1,4,3,2]
print(arrayPartition(input))