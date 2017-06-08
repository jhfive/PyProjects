# RELU 함수
import numpy as np
import matplotlib.pyplot as plt

def relu_function(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 5.1) # y축의 범위 지정
plt.show()