import json
import pandas as pd # 데이터 조작 및 분석을 위한 기초 라이브러리
import matplotlib.pyplot as plt #metplotlib: 데이터 시각화를 위한 라이브러리
import seaborn as sns # seaborn: 통계적 데이터 시각화를 위한 라이브러리

#한글 폰트 설정(시각화시 한글깨짐 방지)
plt.rcParams['font.family']='NanumGothic' #시스템에 해당폰트 설치 확인

#loading csv file (df: data frame)
#cp949 : 한글 인코딩 문제 해결하기 위한 default setting
df = pd.read_csv('seoulmetro 복사본.csv',encoding = 'utf-8')
#상위 5개 행 출력
print(df.head())

print("Column Name:",df.columns)

print('------------------------')
#데이터 타입 및 결측치 확인
print(df.info())

print('특정 열 예시 보기')
print(df[['호선명', '지하철역','06시-07시 승차인원', '06시-07시 하차인원']].head())