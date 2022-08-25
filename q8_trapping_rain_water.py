'''

빗물 트래핑 : 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산해라.
투 포인터로 풀 수 있도록 한다. 각각 좌우 기둥의 최대 높이가 현재 높이와의 차이만큼 물 높이 volume을 더해 나간다.
적어도 낮은 쪽은 그만큼 항상 채워진다는 것이기 때문에, 낮은 쪽에서 높은 쪽으로 서로 접근한다. 

'''

def trap(height:list[int]) -> int:
    if not height:
        return 0
    volume = 0
    left,right = 0,len(height)-1
    left_max,right_max = height[left],height[right]

    while left<right : # left와 right가 만날 때까지
        left_max,right_max = max(height[left],left_max),max(height[right],right_max)
        if left_max <=right_max:
            volume += left_max - height[left] # 낮은쪽은 항상 채워진다.
            left += 1
        else:
            volume += right_max - height[right]
            right-=1
    return volume
a = [0,1,0,2,1,0,1,3,2,1,2,1]
b = [3,3,3,3,3,2,3]
print(trap(a))
print(trap(b))
