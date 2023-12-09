# Analysis of Highway Electric Vehicle Charging Stations and Site Selection
<br/><br/>

## Background and Significance
In recent times, the number of electric vehicles has surged rapidly, and this is largely attributed to government subsidies. However, concerns have surfaced regarding the rapid growth of electric vehicles in the absence of sufficient infrastructure, leading to a variety of issues.
<br/>

The primary issue lies in the availability of electric vehicle charging stations. Charging electric vehicles requires a significant amount of time, even with the recent advancements in high-speed battery chargers. Despite these improvements, the charging speed remains notably slower compared to refueling a traditional gasoline vehicle. Moreover, the limited number of charging stations brings inconvenience for electric vehicle owners, especially in densely populated areas with the limited number of charging infrastructures.
<br/>

The most representative locations are highway rest areas. Despite attracting a large number of people, rest areas inherently have a limited number of charging stations due to their geographical limitations. This limitation fails to adequately meet the current demand for charging electric vehicles. Also considering the increasing pace of electric vehicle adoption, the demand for fast-charging infrastructure is expected to grow further in the future. Therefore, this project aims to examine the current state of electric vehicle charging stations at highway rest areas and explore data-driven approaches to identify the most suitable locations for future installations.

<br/>

## Dependencies
- Windows 10
- Jupyter Notebook
- Python
- Google Cloud Platform(BigQuery, Cloud Storage)
<br/>

## Data Sources

|Name|Website|
|-----|-----|
|자동차 등록 현황 보고|[국토교통 통계누리](https://stat.molit.go.kr/portal/cate/statFileView.do?hRsId=58&hFormId=1244&hSelectId=1244&sStyleNum=562&sStart=2021&sEnd=2021&hPoint=00&hAppr=1)|
|전기차 등록 현황|[차지 인포](https://chargeinfo.ksga.org/front/statistics/evCar)|
|충전소 리스트|[무공해차 통합누리집](https://ev.or.kr/nportal/monitor/evMap.do)|
|전기차 충전소 충전량|[공공데이터포털](https://www.data.go.kr/data/15102510/fileData.do)|
|구간단면 양방향 교통량|[한국도로공사 고속도로 공공데이터 포털](https://data.ex.co.kr/portal/fdwn/view?type=TCS&num=67&requestfrom=dataset)|
|구간교통량(월별, 차종별)(2022년)|[한국도로공사 고속도로 공공데이터 포털](https://data.ex.co.kr/portal/docu/docuList?datasetId=17&serviceType=&keyWord=&searchDayFrom=2014.12.01&searchDayTo=2023.11.14&CATEGORY=TR&GROUP_TR=TRAF_STAT&sId=17)|
|휴게소이용객 및 교통량 현황|[한국도로공사 고속도로 공공데이터 포털](https://data.ex.co.kr/portal/docu/docuList?datasetId=811&serviceType=&keyWord=%ED%9C%B4%EA%B2%8C%EC%86%8C&searchDayFrom=2014.12.01&searchDayTo=2023.11.14&CATEGORY=&GROUP_TR=&sId=811)|
<br/>

## Analysis Process


### 1. The Number of Registered Vehicles

![1](https://github.com/GRetriever/Data-Analysis-Project/assets/148840826/1da24197-cdd5-4ea6-986b-249a13dc15d7)

 The graph above illustrates the increase in the number of registered vehicles over the past 10 years. The total number is 25,870,152 as of 31 Oct 2023.
 

![2](https://github.com/GRetriever/Data-Analysis-Project/assets/148840826/d6da0242-8291-402e-98aa-fcc61b904f21)


 This graph shows the annual growth rate of registered vehicles. The maximum growth rate is 4.03% in 2014-2015, while the minimum was recorded at 1.84% from 2022 to 2023. The average rate is 2.94%.
 <br/>
 <br/>
 
### 2. The Number of Registered Electric Vehicles

![3](https://github.com/GRetriever/Data-Analysis-Project/assets/148840826/8ebee6a8-2676-47ea-ad21-bff6b0a0fe20)

 The graph above illustrates the changes in the number of EV registrations over the last 10 years. The total number is 420,905 as of 31 Oct 2023.
 

![4](https://github.com/GRetriever/Data-Analysis-Project/assets/148840826/a499284f-610c-4811-89f2-375711d5368f)

 This graph represents the growth rate of EV registrations. The maximum growth rate occured at 259.76% in 2017-2018, while the minimum was 5.57% from 2012-2013. The average growth rate is 101.44%.
 <br/>

### 3. The Number of Registered Charging Stations

![5](https://github.com/GRetriever/Data-Analysis-Project/assets/148840826/c9858898-a813-4cc4-a1fd-3b5d280f4b3a)

 It shows the number of registered EV charging stations nationwide. As of 14 Nov 2023, the total number is 265,457, with 1,390 registered for highway use.
 <br/>

### 4. Average Charging Capacity and Charging Time at Highway Rest Area

| Number | Type | Charge | Time |
| --- | --- | --- | --- |
| 162768 | 급속 | 23.233272 | 29.968292 |

 The table above represents the average charging amount and charging time of EV at highway charging stations registered with the Korea Electric Power Corporation in 2023.

![6](https://github.com/GRetriever/Data-Analysis-Project/assets/148840826/1ceb1809-ad6f-4b0e-a47e-58ad808efafa)

 The X-axis of the graph stans for charging capacity (kW), and the Y-axis for the number of vehicles. The majority are below 40kW.

![7](https://github.com/GRetriever/Data-Analysis-Project/assets/148840826/743f342d-527e-4bc6-a1ac-062e691a5a1f)

 The X-axis represents charging time, and the Y-axis represents the number of vehicles. The height of the bars is highest around 30 minutes, with the 1-hour bar standing out.
<br/>

### 5. Top 15 Highway Traffic Volume

![8](https://github.com/GRetriever/Data-Analysis-Project/assets/148840826/3c9e1ee3-a686-46c4-8c81-a72682986b87)

 The graph depicts the top 15 daily average highway traffic volumes as of 12 Nov 2023. The highest is 5,789,176, followed by 3,237,706 and 2,575,357.
<br/>

### 6. Top 15 Highway Segment Traffic Volume

![9](https://github.com/GRetriever/Data-Analysis-Project/assets/148840826/8d3d7a7e-1bed-4750-9020-499a32ecbafe)

 It shows the top 15 daily average traffic volumes by highway segment in 2022. The highest traffic volume records 230,936 for a day.
<br/>

### 7. Top 15 Rest Area Visitors

![10](https://github.com/GRetriever/Data-Analysis-Project/assets/148840826/c4c77829-8411-40eb-9cd9-19caaf765009)

 This represents the top 15 rest areas with the highest daily visitor numbers as of 24 Aug 2023.

<br/><br/>


## Results
The number of registered cars has been steadily increasing, averaging an annual growth rate of 2.9% over the past 10 years. In contrast, the number of registered electric vehicles has surged more rapidly, experiencing an average growth rate of 101% per year.

Electric vehicles account for 1.63% of the total number of registered cars(420905 out of 25870152) as of october 31,2023. The number of charging stations at highway rest areas is 1390, which is 0.5% of the total charging stations(1390 out of 265457). The questions arises: is 1390 enough? The answer still remains unclear. It is similar to determining how many toilets are needed in highway rest area, dependent on variables such as location, traffic flow, population. Quantifying the ideal number is quite challenging. Then attempting a simple calculation can help to address this matter.

If we divide the total number of charging stations at highway rest areas (1390) by the number of rest areas (207), the result is approximately 6.7 charging stations per rest area. Assuming that the majority of traffic occurs between 7 am to 10 pm and that each charging station operates continuously, with an average charging time of 30 minutes, we can calculate the daily charging capacity as follows: 6.7 charging stations * 2 (charging sessions per hour) * 15 (hours of peak traffic) = 201 vehicles per day. Let's apply this calculation to the case of 칠곡휴게소.

칠곡휴게소 had 16,447 vehicles visiting for the day on 24,August, 2023. Assuming that 1.6% of these vehicles are electric, approximately 263 electric vehicles visited that day. This exceeds the daily capacity of 201 vehicles. Using this simple calculation, it can be concluded that the current number of charging stations at highway rest areas is insufficient. And in reality, during peak hours, it is expected that the current number of charging stations would not be able to meet demand
<br/><br/>
<br/>

## Site Selection

The site selection process is based on several factors such as traffic volume, the number of visitors. Firstly, I identified the top 5 routes with the highest traffic volume, and selected the rest area with the highest visitor counts for each routes. This approach presumably prevents the concentration on a single route or in a specific regions. 25 locations were selected in total.

|경부선|영동선|중부선-대전통영선A|남해선A|서해안선|
|---------|----------|----------|----------|---------|
|입장거봉포도(서울)|여주(강릉)|하남드림|진영(순천)|화성(목포)|
|안성(부산)|용인(강릉)|이천(하남)|함안(순천)|행담도|
|천안삼거리(서울)|횡성(강릉)|마장|문산(순천)|화성(서울)|
|안성(서울)|여주(인천)|오창(남이)|섬진강(부산)|서산(목포)|
|죽전(서울)|용인(인천)|오창(하남)|섬진강(순천)|고창고인돌(목포)|
<br/>
<br/>

## Limitations

##### 1. Challenge to pinpoint perpect locations
It was difficult in selecting ideal locations as not all factors were adequately considered. Areas with high traffic volume but lack of rest areas or segments where traffic is large, but insufficient for the entire highway route, were not accounted for in the selection process.

##### 2. Installation Cost
The installation of charging stations at rest areas costs a huge amount of expenses. While rest areas around big cities have fewer challenges in installation, those located in remote areas can easily face difficulties. The biggest issue is installing power infrastructure as charging electric vehicles demands a substantial amount of electricity.

##### 3. Maintenance Cost
The maintenance requires significant expenses since breakdowns occur frequently. According to the survey conducted 11,Nov,2023, it is reported that approximately 84% of electric vehicle users have experienced charging failures, with 75% attributing to equipment malfunctions and breakdowns.

<br/><br/>

## Acknowledgements
I would like to express my sincere gratitude to
- [김형준](https://github.com/yeomko22), coach of Multicampus

for matplotlib/seaborn

<br/><br/>


## References
- [신차 67%를 전기차로... 美, 2032년까지 대전환](https://www.chosun.com/international/2023/04/12/LVSWS62CORBNRBLZJY4AGX7UZM/)
- ["현대차, 전기차 목표치 상향…시장 선점 키는 투자확대·원가절감"](https://www.hankyung.com/article/2023062130576)
- [고속도로 전기차 충전소는 왜 아직도 부족할까요](https://www.edaily.co.kr/news/read?newsId=01108646635637456&mediaCodeNo=257&OutLnkChk=Y)
- [충전기 고장 분통 터지네…전기차 이용자 84% “충전 실패 경험 有”](https://www.sedaily.com/NewsView/29X6Z5B1L1)
- [“전기차 45만대인데 고속도로 휴게소 충전소는 1천여 개 뿐”](https://www.yna.co.kr/view/AKR20230924040000001?input=1195m)
- [“전기차 날로 느는데… 고속도로 휴게소 충전기는 1천여 개뿐](https://www.yonhapnewstv.co.kr/news/MYH20230930003400641?input=1825m)
- [“전기차 타고 고향 가다 설라… 휴게소 충전소 1015개뿐](https://www.womaneconomy.co.kr/news/articleView.html?idxno=218875)
- [“전기차 5배 증가했는데… 고속도로 충전시설 1015개 불과”](https://www.ekn.kr/web/view.php?key=20230928010008110)
- [지역 맞춤 전기차 충전기 설치 사업 시동…1만5665기에 1283억 지원](https://www.etoday.co.kr/news/view/2238990)
<br/><br/>


## Contact Info
> Email : xzv2221@naver.com
