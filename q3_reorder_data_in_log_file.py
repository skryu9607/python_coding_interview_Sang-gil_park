'''
로그의 가장 앞부분은 식별자다.
문자로 구성된 로그가 숫자 로그보다 앞에 온다.
식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다
숫자 로그는 입력 순서대로 한다.

'''
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

def reorder(self,logs:list[str])-> None:
    letters,digits = [],[]
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters = letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits