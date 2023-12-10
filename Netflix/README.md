# Neflix Original Films Suggestion Based on IMDB Score
<br/><br/>

## 🎯Goal
This project aims to conduct a statistical analysis on Netflix Original Films data using IMDB scores and provide recommendations for future production.
<br/>
[Netflix 데이터 바로가기](https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores/data)

</br></br>

## Overview
</br>
### 1. EDA (Exploratory Data Anaylsis)
Analyse the means and differences
</br>
### 2. Recommendations Based on Statistical Hypothesis Test
Optimized production recommendations based on genre, premiere, runtime, and language
</br>
### 3. Insights & Limitations

</br>

## Dependencies
- Windows 10
- Jupyter Notebook
- Python
<br/>

## Dataset
</br>

### 1. Dataset

![](https://velog.velcdn.com/images/xzv2221/post/20e396cb-24b9-419c-a3e4-31c886089456/image.png)

he dataset comprises 6 columns and 584 rows of data.

</br>

### 2. Column

|컬럼명|내용|
|-----|-----|
|Title|필름 제목|
|Genre|필름 장르|
|Premiere|개봉 날짜|
|Runtime|상영 시간|
|IMDB Score|IMDB 평점|
|Language|상영 언어|

</br>

### 3. Background Knowledge
[IMDb (Internet Movie Database)](https://www.imdb.com/)

- American movie information site, recognized as the world's largest movie website

- Reflects popular preference

- Has a high level of credibility contributed by the high number of votes and is utilised in various analyses and predictions

</br>

**eg)**
![](https://velog.velcdn.com/images/xzv2221/post/d0a54ae5-f103-4709-8c70-5f8661ac9a23/image.png)
![](https://velog.velcdn.com/images/xzv2221/post/34ed666a-c8c2-480e-b15d-05fffe37ef45/image.png)

</br></br>

## EDA

</br>

### 1. Columns and Data

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv(r'C:\Users\bluek\OneDrive\Desktop\mulcam\NetflixOriginals.csv', encoding ='unicode_escape')
```

</br>

### 2. Column 및 Data

```python
df.shape
```
![](https://velog.velcdn.com/images/xzv2221/post/6b486bf9-8299-49ea-a48c-6a2b662e6a23/image.png)

 6개 column, 584개 데이터

</br>

### 3. 결측치 확인

```python
df.isnull().sum()
```
![](https://velog.velcdn.com/images/xzv2221/post/1ad57f28-1902-4e16-afc6-7dda9ea1dc62/image.png)

</br>

### 4. 각 Column의 고유값 확인

```python
df.nunique()
```

![](https://velog.velcdn.com/images/xzv2221/post/c1f66179-630e-4edc-bd8f-eb9925a644c3/image.png)

 장르 115 가지, 언어 38가지

</br>

### 5. IMDB Score 분포

```python
plt.figure(figsize=(8, 6))
sns.histplot(df['IMDB Score'], bins=30, color= 'black', kde=True)
plt.xlabel('IMDB Score')
plt.ylabel('Frequency')
plt.title('Distribution of IMDB')
plt.show()
```
![](https://velog.velcdn.com/images/xzv2221/post/e2bfb0ef-ae36-4983-bf94-f9c4ef0cec51/image.png)

 6.5점에서 가장 많은 분포를 보임

</br>

### 6. Genre 분석
</br>

#### 6-1. 빈도수 상위권 장르의 평균 IMDB Score

```python
top_genres = df['Genre'].value_counts().nlargest(10).index

# Genre 상위 10개 항목에 속하는 데이터만 선택
df_top_genres = df[df['Genre'].isin(top_genres)]

plt.figure(figsize=(12, 8))
sns.countplot(data=df_top_genres, x='Genre', order=top_genres, palette='viridis')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Top 10 Genres Distribution')
plt.xticks(rotation=45, ha='right')
plt.show()

# 상위 10개 장르의 평균 IMDB Score 계산후 큰 순서대로 반환
mean_top_genres = df[df['Genre'].isin(top_genres)].groupby('Genre')['IMDB Score'].mean()

mean_top_genres.nlargest(10)
```

![](https://velog.velcdn.com/images/xzv2221/post/a8983d7d-a557-4020-b816-a45bcee66e9f/image.png)


![](https://velog.velcdn.com/images/xzv2221/post/4172e57b-a892-49a0-b7bc-a09d4cb1a3cd/image.png)

 빈도수 상위 10개의 장르중 평균 IMDB Score는 Documentary가 제일 높았다

</br>

#### 6-2. 빈도수 상관 없이 평균 IMDB Score가 높은 장르

```python
#T-test 가설 검정 전에 장르별로 IMDB Score 평균이 높은 순으로 나열해본다


Gen_IMDB = df.groupby(["Genre"])[["IMDB Score"]].mean()
result = Gen_IMDB.sort_values(by='IMDB Score', ascending=False)
result

```

![](https://velog.velcdn.com/images/xzv2221/post/ee616171-581c-4027-ba57-69e5015121a5/image.png)

평균 IMDB Score가 높아도 빈도수가 월등히 적은 장르는 제거

</br>

#### 6-3. 빈도수가 10이상인 장르중 평균 IMDB Score 비교

```python
# 각 장르별 빈도수 계산
genre_count = df['Genre'].value_counts()

# 빈도수가 10건 이상인 장르만 필터링
genres_over_10 = genre_count[genre_count >= 10].index

# 필터링된 장르의 평균 'IMDB Score' 및 빈도수 계산
filtered_genres = df[df['Genre'].isin(genres_over_10)]
genre_stats = filtered_genres.groupby("Genre").agg({"IMDB Score": ["mean", "count"]})
genre_stats.columns = ["Avg_IMDB_Score", "Frequency"]

# 평균 'IMDB Score'를 기준으로 내림차순 정렬
sorted_genre_stats = genre_stats.sort_values(by='Avg_IMDB_Score', ascending=False)
sorted_genre_stats
```

![](https://velog.velcdn.com/images/xzv2221/post/eea07039-fea0-467a-bec9-d8b35db531e8/image.png)

![](https://velog.velcdn.com/images/xzv2221/post/3d25bf38-f4a2-4cb9-ab9b-8f2e3cb3a8c8/image.png)

분석할 장르는 Documentary로 선정

</br>

### 7. Language 분석
</br>

#### 7-1.  언어별 빈도수 분석

```python
top_lang = df['Language'].value_counts().nlargest(10).index

# 'Language' 상위 10개 항목에 속하는 데이터만 선택
df_top_lang = df[df['Language'].isin(top_lang)]

plt.figure(figsize=(12, 8))
sns.countplot(data=df_top_lang, x='Language', order=top_lang, palette='viridis')
plt.xlabel('Language')
plt.ylabel('Count')
plt.title('Top 10 Language Distribution')
plt.xticks(rotation=45, ha='right')
plt.show()
```

![](https://velog.velcdn.com/images/xzv2221/post/a10ef100-5fd2-4ffd-9d0d-37a73bdbed76/image.png)

영어가 압도적으로 많다.

</br>

#### 7-2. IMDB Score가 높은 언어 반환

```python
#T-test 가설 검정전에 언어별로 IMDB Score 평균이 높은 순으로 나열해본다

Gen_IMDB = df.groupby(["Language"])[["IMDB Score"]].mean()
result = Gen_IMDB.sort_values(by='IMDB Score', ascending=False)
result
```

![](https://velog.velcdn.com/images/xzv2221/post/4c012d4d-3f47-4ce1-840b-610cf11684f3/image.png)

</br>

### 8. Runtime 분석
</br>

#### 8-1. Runtime 분포도

```
plt.figure(figsize=(8, 6))
sns.histplot(df['Runtime'], color = 'black', kde=True)
plt.xlabel('Runtime')
plt.ylabel('Frequency')
plt.title('Distribution of Runtime')
plt.show()
```

![](https://velog.velcdn.com/images/xzv2221/post/7413ae9b-7261-4d76-bc13-9a2ce9f0bda3/image.png)

100분에서 최빈값을 가짐

</br>

#### 8-2. IMDB Score by Runtime Scatterplot

```python
#IMDB score by Runtime 스캐터플롯 
plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.scatterplot(data=df,x="Runtime",y="IMDB Score").set(title="IMDB score by Runtime")
```
![](https://velog.velcdn.com/images/xzv2221/post/036af264-f865-445b-a6b9-12cd95a654aa/image.png)

</br>

#### 8-3. Pearson Correlation & Heatmap

```python
#pearson_correlation & heatmap
df_1 = df[["Runtime","IMDB Score"]]
cor = df_1.corr()
print(cor,"\n")

#Correlation Heatmap
plt.figure(figsize=(12,10))
fig, ax = plt.subplots(figsize=(7,5))
sns.heatmap(cor, annot=True, cmap=plt.cm.Reds,ax=ax)
plt.title("Heapmap")
plt.show()
```

![](https://velog.velcdn.com/images/xzv2221/post/46484b0a-2f02-4dd3-b114-4a1475b3d1e4/image.png)

Runtime 과 IMDB Score간의 상관관계가 적다.

</br>

#### 8-4. 연도에 따른 Runtime 추이 & Regplot

```python
#연도에 따른 runtime 추이
df_5 = df.groupby(['Year'])[["Runtime"]].mean()
sns.set_style("whitegrid")
sns.lineplot(data=df_5).set(title="Avg_Runtime by Year" )#연도에 따른 runtime 추이
#연도에 따른 runtime 추이 regplot
sns.regplot(data=df_5,x=df_5.index, y= "Runtime",scatter_kws={"s":10},
line_kws={"color":"coral"}).set(title="regplot of Runtime by Year")
```

![](https://velog.velcdn.com/images/xzv2221/post/cd971200-268f-4e80-80dc-5a1e434c2ec4/image.png)
![](https://velog.velcdn.com/images/xzv2221/post/1d45a22b-4351-41fe-b73a-0b49a307442f/image.png)

연도에 따라 Runtime이 증가하는 추세임을 알 수 있다. 

</br>

### 9. Premiere 분석
</br>

#### 9-1. 연도별 평균 IMDB Score

```python
# 연도별 평균 점수

yearly_average_score = df.groupby(df['Premiere'].dt.year)['IMDB Score'].mean()

yearly_average_score.plot(kind='bar',color = sns.color_palette('winter'),alpha=0.6)
plt.xlabel('Genre')
plt.ylabel('Count')
plt.title('Yearly Average Score')
_=plt.xticks(rotation=0)
```

![](https://velog.velcdn.com/images/xzv2221/post/b550a12e-b507-4bbd-9c04-a6e2f4a56feb/image.png)


평균은 6.4점 정도이며 약간의 차이는 존재하나 대체로 균등함

</br>

#### 9-2. 월별 평균 IMDB Score

```python
# 월별 스코어

monthly_average_score = df.groupby(df['Premiere'].dt.month)['IMDB Score'].mean()

sns.set_style('whitegrid')
monthly_score.plot(kind='bar',color = sns.color_palette('winter'),alpha=0.6)
plt.xlabel('Month')
plt.ylabel('Score')
plt.title('Monthly Average Score')
_=plt.xticks(rotation=0)

```

![](https://velog.velcdn.com/images/xzv2221/post/5cf7a494-381f-41a7-b848-508d1f60d224/image.png)

![](https://velog.velcdn.com/images/xzv2221/post/b4b92443-1570-4bd1-bb56-f42f74f775df/image.png)

6월 점수가 가장 높음을 알 수 있다.

</br></br>

## T-test 가설 검정

</br>

### 어떤 장르를 제작할까❓
</br>

#### 1. Documentary와 나머지의 평균 IMDB Score 차이 검정
</br>

**1-1. 등분산 검정**

```python
# 등분산성 검정

test_names = ["IMDB Score"]

documentary_scores = df[df['Genre'] == 'Documentary'][['IMDB Score']]
other_scores = df[df['Genre'] != 'Documentary'][['IMDB Score']]

for test_name in test_names:
    _, p_value_levene = stats.levene(documentary_scores[test_name], other_scores[test_name])
    if p_value_levene > 0.05:
        print(f"{test_name} p-value: {p_value_levene}, 등분산 가정 만족")
    else:
        print(f"{test_name} p-value: {p_value_levene}, 이분산 가정 만족")
        
```
![](https://velog.velcdn.com/images/xzv2221/post/d917604e-0473-4e0c-8c13-78b564e408a1/image.png)

</br>

**1-2. 가설 설정 및 T-test**

```python
t_statistic, p_value = stats.ttest_ind(
    a=documentary_scores,
    b=other_scores,
    alternative="greater",
    equal_var=False
)

print(f"p-value: {p_value}")
print(f"귀무 가설 기각: {p_value < 0.05}")

Documentary_Gen_IMDB = df.groupby("Genre")[["IMDB Score"]].mean().loc['Documentary']
print("Documentary Score:" ,Documentary_Gen_IMDB)

Drama_Gen_IMDB = df.groupby("Genre")[["IMDB Score"]].mean().loc['Drama']
print("Drama Score:", Drama_Gen_IMDB)
```

귀무가설 : Documentary 평균 IMDB Score와 나머지 장르의 평균 IMDB Score는 같다

대립가설: Documentary 평균 IMDB Score가 나머지 장르의 평균 IMDB Score보다 크다

![](https://velog.velcdn.com/images/xzv2221/post/d6551711-67eb-4caf-8dcc-a16aea20a084/image.png)


True이므로 귀무가설을 기각하고 대립가설을 채택한다

Documentary 장르와  나머지 장르 간의 IMDB Score는 유의미한 차이가 있다.

→ Documentary의 IMDB Score가 더 높다

</br>

**Documentary 장르 추천!**

</br>

### 어떤 시기에 개봉할까❓
</br>

#### 2. Documentary 개봉월에 따른 평균 IMDB Score 차이 검정
</br>

**2-1. Documentary 월별 점수 분포**

```python
# 다큐멘터리 월 평균 점수
documentary_monthly_score = df[df['Genre']=='Documentary'].groupby(df['Premiere'].dt.month)['IMDB Score'].mean()

documentary_monthly_score.plot(kind='line')
plt.title('Documentary Monthly Score')
```

![](https://velog.velcdn.com/images/xzv2221/post/94f31cd8-6e18-42ea-a61f-beb0befdd929/image.png)

다큐멘터리의 평균 IMDB스코어는 6월, 10월에 가장 높음을 확인할 수 있다.
</br>

**2-2. 등분산 검정**

```python
# 등분산성 검정
test_names = ["IMDB Score"]

june_scores = df[(df['Premiere'].dt.month == 10) & (df['Genre'] == 'Documentary')][['IMDB Score']]
other_scores = df[(df['Premiere'].dt.month != 10) & (df['Genre'] == 'Documentary')][['IMDB Score']]
for test_name in test_names:
    _, p_value_levene = stats.levene(june_scores[test_name], other_scores [test_name])
    if p_value_levene > 0.05:
        print(f"{test_name} p-value: {p_value_levene}, 등분산 가정 만족")
    else:
        print(f"{test_name} p-value: {p_value_levene}, 이분산 가정 만족")
```

![](https://velog.velcdn.com/images/xzv2221/post/db79c79e-18bb-4856-88bf-3c98b9fbdad1/image.png)
</br>

**2-3. 가설 설정 및 T-test**

```python
t_statistic, p_value = stats.ttest_ind(
    a=june_scores,
    b=other_scores ,
    alternative="greater",
    equal_var=True
)

print(f"p-value: {p_value}")
print(f"귀무 가설 기각: {p_value < 0.05}")
```

귀무가설 : Documentary의 10월 개봉 IDBM Score와  나머지 평균 IMDB Score는 같다.

대립가설 : Documentary의 10월 개봉 IDBM Score는  나머지 평균 IMDB Score보다 크다.

![](https://velog.velcdn.com/images/xzv2221/post/a1f082fe-df80-4439-a9b3-604732b277ef/image.png)

True 이므로 귀무가설을 기각한다.


**Documentary는 10월에 개봉하는 것이 가장 좋다!**

</br>

### 상영시간은 몇분❓
</br>

#### 3. Documentary 런타임에 따른 평균 IMDB Score 차이 검정
</br>

**3-1. 상영시간별 점수 분포**

```python
#IMDB score by Documentary Runtime 스캐터플롯 
documentary_runtime= df[df['Genre']=='Documentary']
plt.figure(figsize=(12,6))
sns.set_style("whitegrid")
sns.scatterplot(data=documentary_runtime,x="Runtime",y="IMDB Score").set(title="IMDB score by Documentary Runtime")


# Documentary Runtime 분포
plt.figure(figsize=(8, 6))
documentary_runtimes = df[df['Genre'] == 'Documentary']['Runtime']
sns.histplot(documentary_runtimes, color='black', kde=True)
plt.xlabel('Runtime')
plt.title('Distribution of Runtimes for Documentary')
plt.show()
```

![](https://velog.velcdn.com/images/xzv2221/post/5a8e996b-c77d-457f-89f7-29628c4dd308/image.png)

해당 Scatterplot으로 확인하기 어렵다

Documentary 컨텐츠의 runtime의 기준으로 런타임 상위25% = 1 나머지 = 0으로 나누어 진행 

![](https://velog.velcdn.com/images/xzv2221/post/68ac3297-b459-4334-8141-6ae316ff7490/image.png)


귀무가설: 런타임 상위25% 집단 과 나머지 집단의 평균의 차는 0이다
대립가설: 런타임 상위25% 집단 과 나머지 집단의 평균의 차는 0보다 크다
</br>

**3-2. 등분산성 검정**

```
test_names = ["IMDB Score"]

over_runtime = df_2[df_2['runtime_percent'] == 1][['IMDB Score']]
under_runtime = df_2[df_2['runtime_percent'] == 0][['IMDB Score']]

for test_name in test_names:
    _, p_value_levene = stats.levene(over_runtime[test_name], under_runtime[test_name])
    if p_value_levene > 0.05:
        print(f"{test_name} p-value: {p_value_levene}, 등분산 가정 만족")
    else:
        print(f"{test_name} p-value: {p_value_levene}, 이분산 가정 만족")
```

![](https://velog.velcdn.com/images/xzv2221/post/50e9ac28-0f86-4ede-a44b-b5ed65c4de13/image.png)
</br>

**3-3. 가설 설정 및 T-test**

```python
t_statistic, p_value = stats.ttest_ind(
    a=over_runtime,
    b=under_runtime,
    alternative="greater",
    equal_var=True
)
print(f"p-value: {p_value}")
print(f"귀무 가설 기각: {p_value < 0.05}")
```

![](https://velog.velcdn.com/images/xzv2221/post/55fd6571-81bb-4912-b1a2-63438818888a/image.png)


True 이므로 귀무가설을 기각하고 대립가설을 채택한다.

런타임 상위25%과 나머지간의 IMDB score에는 유의미한 차이가 있다.


**Documentary 장르의 경우 98분 이상의 런타임 추천**

</br>

### 어떤 언어❓
</br>

#### 4. English 포함 여부에 따른 평균 IMDB Score 차이 검정
</br>

**4-1. 영어와 영어를 지원하지 않는 영화 개수 비교**

```python
english = df[df['Language'].str.contains('English')]
other = df[~df['Language'].str.contains('English')]

plt.bar(['English', 'Other'], [len(english), len(other)])
plt.xlabel('Language')
plt.ylabel('Count')
plt.title('Number of Films in English vs Other Languages')
plt.show()
```

![](https://velog.velcdn.com/images/xzv2221/post/a9c577e5-dac4-4282-a8ea-cec6de07195f/image.png)


영어를 지원하는 영화가 더 많다
</br>

**4-2. 등분산성 검정**

```python
#English를 포함하는 것과 포함하지 않는 것 차이의 등분산성 검정

test_names = ["IMDB Score"]

english_scores = df[df['Language'].str.contains('English')][['IMDB Score']]
other_scores = df[~df['Language'].str.contains('English')][['IMDB Score']]

for test_name in test_names:
    _, p_value_levene = stats.levene(english_scores[test_name], other_scores[test_name])
    if p_value_levene > 0.05:
        print(f"{test_name} p-value: {p_value_levene}, 등분산 가정 만족")
    else:
        print(f"{test_name} p-value: {p_value_levene}, 이분산 가정 만족")
```

![](https://velog.velcdn.com/images/xzv2221/post/2b2693b6-91d9-4ed5-b738-02a06c3b1685/image.png)
</br>

**4-3. 영어와 비영어 간의 IMDB Score 차이 검정 **

```python
#English를 포함하는 것과 포함하지 않는 것 차이의 T-test

t_statistic, p_value = stats.ttest_ind(
    a=english_scores,
    b=other_scores,
    alternative="greater",
    equal_var=True
)

print(f"p-value: {p_value}")
print(f"귀무 가설 기각: {p_value < 0.05}")
```

![](https://velog.velcdn.com/images/xzv2221/post/df1489c7-4c1a-4fb8-b838-3127f6bac0fc/image.png)


귀무가설을 기각하고 대립가설을 채택한다.

영어와 영어를 포함하지 않는 영화간의 평균 IMDB Score는 유의미한 차이가있다.


**영어를 포함해야한다!**

</br></br>

### 💡Insight


1.언어에서 영어와 비영어에 따른 Score 차이가 있다.


2.Runtime과 IMDB score사이의 상관 관계가 없다. 하지만 Documentary의 경우 상위 25% 와 나머지 간의 IMDB score에는 유의미한 차이가 있다.


3.전체 월별 스코어는 6월이 가장 높으나, Documentary는 10월이 가장 높다


4.런타임은 증가하는 추세다.

</br></br>

### Suggestion

|영화정보|상세정보|
|-----|-----|
|언어|English|
|장르|Documentary|
|개봉월|Otc|
|런타임|98분|

</br></br>

### 🚨한계점


1. IMDB Score가 무조건적인 흥행 요소는 아니다.
→ 흥행 여부를 판단하는데 추가 지표들 필요 : 조회수, User의 평균 시청 시간 데이터 등

2. 총 데이터가 584개로 Column항목별로 집단을 세분화 할때마다 표본이 부족하다 


3. 장르가 ‘/’ 로 과하게 세분화되어 정확한 분류를 하는데 어려움이 있다

![](https://velog.velcdn.com/images/xzv2221/post/52e90a56-553a-4e70-b7ed-6e04a6f606fe/image.png)

