# Analysis of Highway Electric Vehicle Charging Stations and Site Selection

## Background and Significance
In recent times, the number of electric vehicles has surged sharply, and this is largely attributed to government subsidies. However, concerns have been raised regarding the rapid growth of electric vehicles in the absence of sufficient infrastructure, leading to a variety of issues

The primary issue lies in the availability of electric vehicle charging stations. Charging electric vehicles requires a significant amount of time, even with the recent advancements in high-speed battery chargers. Despite these improvements, the charging speed remains notably slower compared to refueling a traditional gasoline vehicle. Moreover, the limited number of charging stations brings inconvenience for electric vehicle owners, especially in densely populated areas with the limited number of charging infrastructures

The most representative locations are highway rest areas. Despite attracting a large number of people, rest areas inherently have a limited number of charging stations due to their geographical limitations. This limitation fails to adequately meet the current demand for charging electric vehicles. Also considering the increasing pace of electric vehicle adoption, the demand for fast-charging infrastructure is expected to grow further in the future. Therefore, this project aims to examine the current state of electric vehicle charging stations at highway rest areas and explore data-driven approaches to identify the most suitable locations for future installations.

## Dependencies
- Windows 10
- Jupyter Notebook
- Python
- Google Cloud Platform(BigQuery, Cloud Storage)

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

## Analysis Process
1. Pre-Processing
2. Visualisation

## Results
The number of registered cars has been steadily increasing, averaging an annual growth rate of 2.9% over the past 10 years. In contrast, the number of registered electric vehicles has surged more rapidly, experiencing an average growth rate of 101% per year.

Electric vehicles account for 1.63% of the total number of registered cars(420905 out of 25870152) as of october 31,2023. The number of charging stations at highway rest areas is 1390, which is 0.5% of the total charging stations(1390 out of 265457). The questions arises: is 1390 enough? The answer still remains unclear. It is similar to determining how many toilets are needed in highway rest area, dependent on variables such as location, traffic flow, population. Quantifying the ideal number is quite challenging. Then attempting a simple calculation can help to address this matter.

If we divide the total number of charging stations at highway rest areas (1390) by the number of rest areas (207), the result is approximately 6.7 charging stations per rest area. Assuming that the majority of traffic occurs between 7 am to 10 pm and that each charging station operates continuously, with an average charging time of 30 minutes, we can calculate the daily charging capacity as follows: 6.7 charging stations * 2 (charging sessions per hour) * 15 (hours of peak traffic) = 201 vehicles per day. Let's apply this calculation to the case of 칠곡휴게소.

칠곡휴게소 had 16,447 vehicles visiting for the day on 24,August, 2023. Assuming that 1.6% of these vehicles are electric, approximately 263 electric vehicles visited that day. This exceeds the daily capacity of 201 vehicles. Using this simple calculation, it can be concluded that the current number of charging stations at highway rest areas is insufficient. And in reality, during peak hours, it is expected that the current number of charging stations would not be able to meet demand

## Site Selection

The site selection process is based on several factors such as traffic volume, the number of visitors. Firstly, I identified the top 5 routes with the highest traffic volume, and selected the rest area with the highest visitor counts for each routes. This approach presumably prevents the concentration on a single route or in a specific regions. 25 locations were selected in total.

|경부선|영동선|중부선-대전통영선A|남해선A|서해안선|
|---------|----------|----------|----------|---------|
|입장거봉포도(서울)|여주(강릉)|하남드림|진영(순천)|화성(목포)|
|안성(부산)|용인(강릉)|이천(하남)|함안(순천)|행담도|
|천안삼거리(서울)|횡성(강릉)|마장|문산(순천)|화성(서울)|
|안성(서울)|여주(인천)|오창(남이)|섬진강(부산)|서산(목포)|
|죽전(서울)|용인(인천)|오창(하남)|섬진강(순천)|고창고인돌(목포)|

## Limitations

##### 1. Challenge to pinpoint perpect locations
It was difficult in selecting ideal locations as not all factors were adequately considered. Areas with high traffic volume but lack of rest areas or segments where traffic is large, but insufficient for the entire highway route, were not accounted for in the selection process.

##### 2. Installation Cost
The installation of charging stations at rest areas costs a huge amount of expenses. While rest areas around big cities have fewer challenges in installation, those located in remote areas can easily face difficulties. The biggest issue is installing power infrastructure as charging electric vehicles demands a substantial amount of electricity.

##### 3. Maintenance Cost
The maintenance requires significant expenses since breakdowns occur frequently. According to the survey conducted 11,Nov,2023, it is reported that approximately 84% of electric vehicle users have experienced charging failures, with 75% attributing to equipment malfunctions and breakdowns.

## Acknowledgements

## Contact Info
