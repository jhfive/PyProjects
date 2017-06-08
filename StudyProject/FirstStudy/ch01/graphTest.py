import numpy as np
import matplotlib.pyplot as plt

# 데이터 준비
x = np.arange(0, 6, 0.1) # 0에서 6까지 0.1 간격으로 생성
y_sin = np.sin(x)
y_cos = np.cos(x)

# 그래프 그리기
plt.plot(x, y_sin, label="sin")
plt.plot(x, y_cos, label="cos", linestyle="--") # cos 함수는 점선으로 그리기
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title("sin & cos") # 제목
plt.legend
plt.show()