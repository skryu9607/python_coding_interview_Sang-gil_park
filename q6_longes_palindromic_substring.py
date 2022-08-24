'''
가장 긴 팰린드롬 부분 문자열을 출력하라. 

입력 : 'babad'
출력 : 'bab'
입력 : 'cbbd'
출력 : 'bb'

투 포인터가 2칸, 3칸씩 간다. 그런후에 일단 판별되면 거기서 멈춰서 확장하여 가장 긴 팰린드롬 부분 문자열을 만들어낸다. 
간단하게 생각해서, s[left] == s[right]이면 확장하면 된다.
'''
def longest_palindrome(s:str)->str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left:int, right:int) -> str:
        while left>= 0 and right<len(s) and s[left]==s[right]:
            left -=1
            right +=1
            # return이 여기있으니까 expand한 object가 return이 안됐다. 어차피 이 while문에 성립안할때 끝날텐데 항상 return이 안되니까 Nonetype이 나왔다. 
            # None type은 사실상 return값이 없다고 생각해도 좋을 것 같다. 
            #return s[left+1:right]
        
        return s[left+1:right] # 이게 max인 palindrome
    if len(s)<2 or s==s[::-1]:
        return s
    result = ''
    for i in range(len(s)-1):
        result = max(result,expand(i,i+1),expand(i,i+2),key=len)
    return result

input1 = "babad"
input2 = 'cbbd'
input3 = 'caabaac'
input4 = 'd'
print(longest_palindrome(input1))    
print(longest_palindrome(input2))    
print(longest_palindrome(input3))    
print(longest_palindrome(input4))    
