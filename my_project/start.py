import os
import pandas as pd
import torch

print(os.getcwd())
print("HI~")

# GPU 사용 가능 -> True, GPU 사용 불가 -> False
print("torch.cuda.is_available():", torch.cuda.is_available())

# GPU 사용 가능 -> 가장 빠른 번호 GPU, GPU 사용 불가 -> CPU 자동 지정 예시
device = torch.device("cuda:0") if torch.cuda.is_available() else torch.device("cpu")

# 사용 가능 GPU 개수 체크
print(torch.cuda.device_count())  # 3
