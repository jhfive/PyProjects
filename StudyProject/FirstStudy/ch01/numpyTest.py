import numpy as np

x = np.array([1.0, 2.0, 3.0])
print(str(type(x)))
print('x = ' + str(x))

y = np.array([2.0, 4.0, 6.0])
print('y = ' + str(y))

# 원소별 덧셈
print('x + y = ' + str(x + y))
# 원소별 뺄셈
print('x - y = ' + str(x - y))
# 원소별 곱셈
print('x * y = ' + str(x * y))
# 원소별 나눗셈
print('x / y = ' + str(x / y))

print('x / 2 = ' + str(x / 2))

# N차원 배열
a = np.array([[3, 0], [0, 6], [3, 6]])
print('a = ' + str(a))
# 배열 차원 확인
print('배열 차원 확인 : ' + str(np.ndim(a)))
print('배열 형상 확인 : ' + str(a.shape))
print('배열 형상 중 인덱스 0 확인 : ' + str(a.shape[0]))
print('배열 타입 : ' + str(type(a)))
print('배열 원소 타입 : ' + str(type(a.dtype)))

b = np.array([[1, 2], [3, 4], [5, 6]])
print('b = ' + str(b))

# 원소별 덧셈
print('a + b = ' + str(a + b))
# 원소별 뺄셈
print('a - b = ' + str(a - b))
# 원소별 곱셈
print('a * b = ' + str(a * b))
# 원소별 나눗셈
print('a / b = ' + str(a / b))

print('a * 10 = ' + str(a * 10))

c = np.array([[1, 2], [3, 4]])
d = np.array([10, 20])
print('c = ' + str(c))
print('d = ' + str(d))
print('c * d = ' + str(c * d))

# 원소 접근
z = np.array([[51, 55], [14, 19], [0, 4]])
print('z = ' + str(z))
print('z[1] = ' + str(z[1]))
print('z[1][0] = ' + str(z[1][0]))

for row in z:
    print('for문 row = ' + str(row))

for row in z:
    for v in row:
        print('이중 for문 value = ' + str(v))

print('다차원 배열 1차원 배열로 변환 = ' + str(z.flatten()))
print('1차원 배열로 변환 후 0, 2, 4 인덱스 가져오기 = ' + str(z.flatten()[np.array([0, 2, 4])]))

Z = z.flatten()
print('배열 내 값 조건 조회(15보다 큰가) : ' + str(Z > 15))
print('배열 내 값 조건 조회 해당 값 가져오기 (15보다 큰값) : ' + str(Z[Z > 15]))

# 행렬 곱
p = np.array([[1, 2], [3, 4]])
q = np.array([[5, 6], [7, 8]])
print('행렬 곱 : ' + str(np.dot(p, q)))

# (a*b) * (b*c) = (a*c)
p = np.array([[1, 2], [3, 4], [5, 6]]) # 3행 2열
q = np.array([[7, 8], [9, 10]]) # 2행 2열
print('행렬 곱 : ' + str(np.dot(p, q))) # 3행 2열