# 계단 함수
import numpy as np
import matplotlib.pyplot as plt

a = np.array([-1.0, 1.0, 2.0])
print('a : ' + str(a))

b = a > 0
print('b : ' + str(b))

c = b.astype(np.int)
print('c : ' + str(c))

def step_function(x):
    return np.array(x > 0, dtype=np.int)

print('step_function(a) : ' + str(step_function(a)))

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축의 범위 지정
plt.show()