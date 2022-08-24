import re
def check_validity(s:str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1] # 뒤집는 표현식
    
example1 = 'A man, a plan, a canal: Panama'
example2 = 'A man, a case, a canal: Panama'
print(type(example1))
print(check_validity(example1))

print(check_validity(example2))