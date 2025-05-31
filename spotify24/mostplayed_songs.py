import json
import pandas as pd # basic library for data manipulation and anlaysis
import matplotlib.pyplot as plt #metplotlib: library for data visualisation
import seaborn as sns # library for statistic visualisation
import kagglehub

# Download latest version
df = pd.read_csv('Most Streamed Spotify Songs 2024.csv',encoding = 'ISO-8859-1')
#trying top 5
print(df.head())

print("Column Name:",df.columns)

#checking data type & missing values
print(df.info())

print('--------------------<Examplifying>-----------------')
print(df[['YouTube Likes', 'YouTube Playlist Reach','YouTube Views']].head())

#aims: getting YouTube-related ranking
#creating a column related to "YouTube"
YT_columns = [col for col in df.columns if 'YouTube'in col] #

# Convert the identified YouTube columns to numeric, coercing errors to NaN
for col in YT_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')


#getting the sum of YouTube stuff so that creating'YouTube Ranking' column
df['YouTube Ranking'] = df[YT_columns].sum(axis=1)
# top 10 YouTube related Ranking
df_top10 = df[['Track','Artist','YouTube Ranking']].sort_values(by = 'YouTube Ranking', ascending = False).head(10)
print(df_top10)

#visualisation: YouTube Ranking
#setting the design
sns.set(style="whitegrid")

#size
plt.figure(figsize=(20,8))

#bar graph
sns.barplot(data = df_top10, x = 'Track', y= 'YouTube Ranking')

#printing
plt.show()

