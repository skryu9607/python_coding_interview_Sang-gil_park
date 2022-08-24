'''
입력 : string 하나랑 banned로 들어오는 list[string]하나. 
출력 : string 
방법 : dictionary로 정리하여, common을 하여, 가장 흔한 단어와 빈도수를 체크한 후에 빈도수로 정렬한다. 
그 이후에 만약에 가장 흔한 단어가 banned일 경우는 그 다음 순위의 단어를 출력한다. 
'''
import re
import collections
def most_common(s:str,banned:list)->str:
    # 정규 표현식에서 ' ' 꼭 스페이스바 찍기.
    words = [word for word in re.sub(r'[^\w]',' ',s).lower().split()]
    counts = collections.Counter(words)
    print(words)
    ans = counts.most_common(1)[0][0]
    # 잘 안됐던 이유. 
    # if ans == str(banned):라고 했는데, 이건 banned라는 list안에 있는 것들을 다 string으로 바꾸는 것이라서 원소에 대한 접근은 X
    # banned[0]이 banned라는 list가 품는 금지단어에 대해서 접근 가능.
    if ans == banned[0]:
        # most_common(2)를 하면, 최빈 단어 두개가 연속으로 나온다. 여기서는
        # [('hit',3),('ball',2)] 이런식이다. 여기서 두번째를 고르려면 counts.most_common(2)[1]이렇게 해야한다. 
        ans = counts.most_common(2)[1][0]
    return ans
paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit.'
banned = ["hit"]
# Expected output = "ball"

print(most_common(paragraph,banned))

'''
1. 정규표현식에서 단어 아닌 것들에 대해서 전부 공백으로 처리하는 법
2. str(banned)가 내 생각과 달랐던 점
3. most_common(2)하면 최빈 두 번째것만 나오는게 아니라 첫 번째, 두 번째 이렇게 2개가 나오는 것.
'''