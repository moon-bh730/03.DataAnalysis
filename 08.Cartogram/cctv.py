import numpy as np 
import pandas as pd 
import matplotlib as mpl 
import matplotlib.pyplot as plt 
# 한글폰트 사용
plt.rc('font', family='NanumBarunGothic')
mpl.rcParams['axes.unicode_minus'] = False
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv(f'cctv/서울시CCTV설치운영현황(자치구)_년도별_210731기준.csv', encoding='euc-kr', header = 1)
print(df.head())
# print(df.tail())
#-----------------------------------------------------
# cctv 전처리
#   0 row 삭제
#   21년 col 삭제
#   새 변수에 필요한것만 가져오기
#   지역정보로 ID 생성
#-----------------------------------------------------

# 인구현황 read_csv
# 인구현황 전처리