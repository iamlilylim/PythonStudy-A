import json
import pandas as pd # 데이터 조작 및 분석을 위한 기초 라이브러리
import matplotlib.pyplot as plt #metplotlib: 데이터 시각화를 위한 라이브러리
import seaborn as sns # seaborn: 통계적 데이터 시각화를 위한 라이브러리

import matplotlib.font_manager as fm


#한글 폰트 설정(시각화시 한글깨짐 방지)
#plt.rcParams['font.family']='AppleGothic' #시스템에 해당폰트 설치 확인
plt.rc('font', family='AppleGothic')  # 한글 폰트 설정
plt.rcParams['axes.unicode_minus'] = False  #



#loading csv file (df: data frame)
#cp949 : 한글 인코딩 문제 해결하기 위한 default setting
df = pd.read_csv('seoulmetro 복사본.csv',encoding = 'cp949')
#상위 5개 행 출력
print(df.head())

print("Column Name:",df.columns)

print('------------------------')
#데이터 타입 및 결측치 확인
print(df.info())

print('특정 열 예시 보기')
print(df[['호선명', '지하철역','06시-07시 승차인원', '06시-07시 하차인원']].head())

print('------------------------')
#aims: 시간대별 승차인원 합계 구하기
#시간대별 승차인원 컬럼 추출
#'승차'라는 단어가 포함된 열 이름을 리스트로 생성
time_columns = [col for col in df.columns if '승차'in col] #한줄코딩
#시간대별 승차인원 총합 계산하여 새로운 열'총 승차인원'이라는 column 생성
df['총승차인원'] = df[time_columns].sum(axis=1)
# 총승차인원기준 상위 100개역 추출
df_top100 = df[['지하철역','호선명','총승차인원']].sort_values(by = '총승차인원', ascending = False).head(100)
print(df_top100)

#visualisation: most crowded stations
#setting the design
sns.set(style="whitegrid")

#size
plt.figure(figsize=(12,8))

#bar graph
sns.barplot(data = df_top100, x = '총승차인원', y= '지하철역', hue = '호선명')

#printing
plt.show()