# MNIST

# import sys, os
# sys.path.append(os.pardir) # 부모 디렉터리의 파일을 가져올 수 있도록 설정
import numpy as np
from StudyProject.dataset.mnist import load_mnist
from PIL import Image

# 처음 한 번은 몇 분 정도 걸립니다
#(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False) # flatten은 배열을 1차원으로 변경할것인지 # normalize true이면 0.0 ~ 1.0 으로 정규화 false이면 0 ~ 255 으로 원래 픽셀값으

# 각 데이터의 형상 출력
#print(x_train.shape) # (60000, 784)
#print(t_train.shape) # (60000,)
#print(x_test.shape) # (10000, 784)
#print(t_test.shape) # (10000,)

# page 99
def img_show(img):
    pil_img = Image.fromarray(np.uint8(img)) # 넘파이로 저장된 이미지 데이터를 PIL용 데이터 객체로 변환
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)  # 5

print(img.shape)  # (784,)   28 * 28 = 784
img = img.reshape(28, 28)  # 형상을 원래 이미지의 크기로 변형
print(img.shape)  # (28, 28)

img_show(img)