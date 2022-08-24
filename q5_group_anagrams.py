'''
문자열을 받아서 애너그램 단위로 그룹핑해라. -> 철자의 set이 같은 것들끼리 그룹핑하라.
실제 문제 풀이 방식은 달랐다. 애너그램 관계인 단어들을 정렬하면, 서로 같은 값을 갖게 되기 때문이다. 
입력 : string들이 담긴 list
출력 : 애너그램 관계인 단어들끼리 묶여있는 list

'''
import collections
from tokenize import group
def group_anagrams(strs:list[str])->list[list[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        print(sorted(word))
        # "".join 함수는 매겨변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수.
        anagrams[''.join(sorted(word))].append(word)
    print(anagrams)
    print(anagrams.keys())
    print(anagrams.values())
    return list(anagrams.values())
words = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(words))

'''
1. collection.defaultdict(list) <- default값을 int로 했을 때의 0이 아니라, 빈 list로 만듦. 추가하려면 append 필요
2. join에 대해서 배움. sorted(word)해보니까 ['a','e','t'] 이런식으로 나오는데, 이걸 합쳐서 그걸 key로 저장하고 key에 해당하는 빈 list에는 원래 단어를 추가한다. 
3. list(anagrams.values())는 잘 되나, list(anagrams.keys())는 잘 안된다. 대신 anagrams.keys()는 가능.

'''
