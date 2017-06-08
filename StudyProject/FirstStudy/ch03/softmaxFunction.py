# 소프트맥스 함수
import numpy as np

def softmax(a):
    exp_a = np.exp(a)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

def softmax_upgrade(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

a1 = np.array([0.3, 2.9, 4.0])
print(softmax(a1))
print(np.sum(softmax(a1)))

a2 = np.array([1010, 1000, 990])
print(softmax_upgrade(a2))
print(np.sum(softmax_upgrade(a2)))