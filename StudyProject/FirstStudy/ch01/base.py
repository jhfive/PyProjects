print('01. ' + 'Hello world!!')
print('02. ' + '2 * 3 = ' + str(2*3))
print('03. ' + '2 ** 3 = ' + str(2**3))
print('04. ' + 'text의 타입 : ' + str(type('text')))

x = 100
y = 3.14
print('05. ' + '변수 대입 후 곱 (x = 100, y = 3.14) : ' + str(x * y) + ' ' + str(type(x * y)))

vList = ['1st', '2nd', '3rd', '4th', '5th'] # 리스트 생성 (자바의 배열과 비슷)
print('06. ' + '리스트 출력 : ' + str(vList))
print('07. ' + '리스트 길이 : ' + str(len(vList)))
print('08. ' + '첫 원소 값 : ' + str(vList[0]))
print('09. ' + '마지막 원소 값 : ' + str(vList[len(vList) - 1]))

vList[len(vList) - 1] = '6th' # 리스트 값 변경
print('10. ' + '마지막 원소 값 변경 후 리스트 출력 : ' + str(vList))
print('11. ' + '인덱스 2부터 4까지 출력 방식 : ' + str(vList[2:5]))
print('12. ' + '인덱스 3부터 끝까지 출력 방식 : ' + str(vList[3:]))
print('13. ' + '인덱스 처음부터 2까지 출력 방식 : ' + str(vList[:3]))
print('14. ' + '인덱스 처음부터 마지막 원소 1개 앞까지 출력 방식 : ' + str(vList[:-1]))
print('15. ' + '인덱스 마지막 원소 2개 출력 방식 : ' + str(vList[-2:]))

vMap = {'width' : 100, 'height' : 180} # 딕셔너리 생성 (자바의 맵과 비슷)
print('16. ' + '딕셔너리 출력 : ' + str(vMap))
print('17. ' + '딕셔너리 길이 : ' + str(len(vMap)))
print('18. ' + 'width 값 : ' + str(vMap['width']))

vMap['weight'] = '72' # 딕셔너리 원소 추가
print('19. ' + '원소 추가 후 딕셔너리 출력 : ' + str(vMap))

vTrue = True
vFalse = False
print('20. ' + 'bool타입 변수 vTrue : ' + str(vTrue) + ' ' + str(type(vTrue)))
print('21. ' + 'bool타입 변수 vFalse : ' + str(vFalse) + ' ' + str(type(vFalse)))
print('22. ' + 'bool타입 변수 not vTrue : ' + str(not vTrue))
print('23. ' + 'bool타입 변수 not vFalse : ' + str(not vFalse))
print('24. ' + 'vTrue and vFalse : ' + str(vTrue and vFalse))
print('25. ' + 'vTrue or vFalse : ' + str(vTrue or vFalse))

# if문
if vTrue:
    print('26. ' + 'Print vTrue')
else:
    print('26. ')

if not vFalse:
    print('27. ' + 'Print vFalse')
else:
    print('27. ')

if not vTrue:
    print('28. ')
elif not vFalse:
    print('28. ' + 'if elif else')
else:
    print('28. ')

# for문
for vLt in vList:
    print('29. ' + vLt)

# 함수
def who():
    print('30. Who are you?')

def myName(name):
    print('31. My name is ' + name)

who()
myName('Sunggi Cho')

# class
class Man:
    def __init__(self, name):
        self.name = name
        print('32. ' + 'Initialized!')

    def hello(self):
        print('33. ' + 'Hello ' + self.name + '!')

    def goodbye(self):
        print('34. ' + 'Good-bye ' + self.name + '!')

vMan = Man("David")
vMan.hello()
vMan.goodbye()