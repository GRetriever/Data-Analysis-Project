import streamlit as st
from openai import OpenAI
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
from io import BytesIO
import requests

# client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])

st.title("여행지 날씨 알아보기")
st.subheader("원하는 여행지의 날씨를 미리 알아보세요!")



def information_crawling(country,city):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    actions = ActionChains(driver)
    url = 'https://www.naver.com/'
    
    driver.get(url)
    
    driver.find_element('xpath','//*[@id="query"]').send_keys(country,city)
    driver.find_element('xpath','//*[@id="search-btn"]').click()

    try:
        recommendation = driver.find_element('xpath','//*[@id="nxTsOv"]/div/div[1]/div[2]/div[1]/div[2]/div[4]/ul/li[1]/div/a/strong/p').text
        flight = driver.find_element('xpath','//*[@id="nxTsOv"]/div/div[1]/div[2]/div[1]/div[2]/div[4]/ul/li[2]/div/a/strong').text
        visa = driver.find_element('xpath','//*[@id="nxTsOv"]/div/div[1]/div[2]/div[1]/div[2]/div[4]/ul/li[3]/div/a/strong').text
        currency =  driver.find_element('xpath','//*[@id="nxTsOv"]/div/div[1]/div[2]/div[1]/div[2]/div[4]/ul/li[4]/div/a/strong').text
        voltage = driver.find_element('xpath','//*[@id="nxTsOv"]/div/div[1]/div[2]/div[1]/div[2]/div[4]/ul/li[5]/div/a/strong').text
        
        image_url_1 = driver.find_element('xpath','//*[@id="nxTsOv"]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/ul/li[1]/a/div/img').get_attribute('src')
        image_url_2 = driver.find_element('xpath','//*[@id="nxTsOv"]/div/div[1]/div[2]/div[1]/div[1]/div[1]/div/ul/li[2]/a/div/img').get_attribute('src')
        response_1 = requests.get(image_url_1)
        response_2 = requests.get(image_url_2)
        img_1 = Image.open(BytesIO(response_1.content))
        img_2 = Image.open(BytesIO(response_2.content))
        st.image([img_1, img_2], width=330)

        st.write('추천 : ', recommendation)
        st.write('비행시간 : ', flight)
        st.write('비자 : ', visa)
        st.write('환율 : ', currency)
        st.write('전압 : ', voltage)
    except:
        st.write('추천 : N/A')
        st.write('비행시간 : N/A')
        st.write('비자 : N/A')
        st.write('환율 : N/A')
        st.write('전압 : N/A')

tab_1,tab_2 = st.tabs(['실험1','실험2'])

with tab_1:
    with st.form('form'):
        st.text("아래의 정보를 입력하세요.")
        col1,col2,col3 = st.columns(3)
        with col1:
            country = st.text_input(
                '국가 (필수)'
            )
        with col2:
            city = st.text_input(
                '도시 (필수)'
            )
        with col3:
            month = st.number_input(
                '월 (필수)',
                min_value = 1,
                max_value = 12,
                step = 1,
                value = 1
            )
        submit = st.form_submit_button('제출하기')
        if submit:
            country = country
            city = city
            information_crawling(country,city)

# =========================================================



def hotel_crawling(country,city,people,sort):
    # options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    actions = ActionChains(driver)
    url = 'https://kr.hotels.com/'
    
    driver.get(url)
    
    # 위치 입력
    driver.find_element('xpath','//*[@id="lodging_search_form"]/div/div/div[1]/div/div/div[2]/div[1]/button').click()
    driver.find_element('xpath','//*[@id="destination_form_field"]').send_keys(city)
    time.sleep(1)
    driver.find_element('xpath','//*[@id="lodging_search_form"]/div/div/div[1]/div/div/div[1]/section/div[2]/div[2]/div[1]/div/ul/li[1]/div/div/button').click()
    
    # 인원수 입력
    driver.find_element('xpath','//*[@id="lodging_search_form"]/div/div/div[3]/div/div[1]/button').click()
    if people == 1:
        driver.find_element('xpath','//*[@id="lodging_search_form"]/div/div/div[3]/div/div[2]/div/div/section/div[1]/div[1]/div/div/button[1]/span').click()
    elif people > 2:
        for i in range(abs(people - 2)):
            driver.find_element('xpath','//*[@id="lodging_search_form"]/div/div/div[3]/div/div[2]/div/div/section/div[1]/div[1]/div/div/button[2]/span').click()

    time.sleep(1)
    driver.find_element('xpath','//*[@id="traveler_selector_done_button"]').click()
    
    driver.find_element('xpath','//*[@id="search_button"]').click()
    
    # 정렬
    driver.find_element('xpath','//*[@id="app-layer-base"]/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/section/div[1]/div[1]/div/div/form/button').click()
    if sort == '낮은 가격부터':
        driver.find_element('xpath','//*[@id="sort-filter-dropdown-sort"]/option[2]').click()
    elif sort == '높은 가격부터':
        driver.find_element('xpath','//*[@id="sort-filter-dropdown-sort"]/option[3]').click()
    elif sort == '시내에서 거리':
        driver.find_element('xpath','//*[@id="sort-filter-dropdown-sort"]/option[4]').click()
    elif sort == '고객평점 + 추천':
        driver.find_element('xpath','//*[@id="sort-filter-dropdown-sort"]/option[5]').click()
    elif sort == '숙박 시설 등급':
        driver.find_element('xpath','//*[@id="sort-filter-dropdown-sort"]/option[6]').click()
    
    driver.find_element('xpath','//*[@id="onetrust-close-btn-container"]/button').click()
    driver.find_element('xpath','//*[@id="app-layer-ShoppingSortAndFilters-SORT_AND_FILTERS"]/section/div[4]/div').click()
    
    time.sleep(4)
    # 1번 호텔
    hotel_name_1 = driver.find_element('xpath','//*[@id="app-layer-base"]/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div/div[1]/div[1]/div/h3').text
    hotel_image_url_1 = driver.find_element('xpath','//*[@id="app-layer-base"]/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[3]/div/div/div[1]/figure/span/span/div/div[1]/div[2]/figure/div/img').get_attribute('src')
    hotel_rating_1 = driver.find_element('xpath','//*[@id="app-layer-base"]/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[3]/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/span/span[1]').text
    
    # 2번 호텔
    hotel_name_2 = driver.find_element('xpath','//*[@id="app-layer-base"]/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[4]/div/div/div/div[2]/div/div[1]/div[1]/div/h3').text
    hotel_image_url_2 = driver.find_element('xpath','//*[@id="app-layer-base"]/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[4]/div/div/div/div[1]/div/figure/span/span/div/div[1]/div[2]/figure/div/img').get_attribute('src')
    hotel_rating_2 = driver.find_element('xpath','//*[@id="app-layer-base"]/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[4]/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/span/span[1]').text
    
    # 3번 호텔
    hotel_name_3 = driver.find_element('xpath','//*[@id="app-layer-base"]/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[5]/div/div/div[2]/div/div[1]/div[1]/div/h3').text
    hotel_image_url_3 = driver.find_element('xpath','//*[@id="app-layer-base"]/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[5]/div/div/div[1]/div/figure/span/span/div/div[1]/div[2]/figure/div/img').get_attribute('src')
    hotel_rating_3 = driver.find_element('xpath','//*[@id="app-layer-base"]/div/main/div/div/div/div/div[2]/section[2]/div/div[2]/div/div[2]/div[1]/div[3]/div[5]/div/div/div[2]/div/div[2]/div[1]/div/div[2]/div[1]/span/span[1]').text
    
    
    response_1 = requests.get(hotel_image_url_1)
    response_2 = requests.get(hotel_image_url_2)
    response_3 = requests.get(hotel_image_url_3)

    img_1 = Image.open(BytesIO(response_1.content))
    img_2 = Image.open(BytesIO(response_2.content))
    img_3 = Image.open(BytesIO(response_3.content))
    
    cols = st.columns(2)
    with cols[0]:
        st.image([img_1], width=330,height=200)
    with cols[1]:
        st.write('호텔명 : ',hotel_name_1)
        st.write('평점 : ',hotel_rating_1)
        
    cols = st.columns(2)
    with cols[0]:
        st.image([img_2], width=330,height=200)
    with cols[1]:
        st.write('호텔명 : ',hotel_name_2)
        st.write('평점 : ',hotel_rating_2)

    cols = st.columns(2)
    with cols[0]:
        st.image([img_3], width=330,height=200)
    with cols[1]:
        st.write('호텔명 : ',hotel_name_2)
        st.write('평점 : ',hotel_rating_2)

sorted = ['추천','낮은 가격부터','높은 가격부터','시내에서 거리','고객평점 + 추천','숙박 시설 등급']

with tab_2:
    with st.form('form2'):
        st.text('아래의 정보를 입력하세요')
        col1,col2 = st.columns(2)
        with col1:
            country = st.text_input(
                '국가 (필수)'
            )
        with col2:
            city = st.text_input(
                '도시 (필수)'
            )
        col1,col2 = st.columns(2)
        with col1:
            people = st.number_input(
                '인원',
                min_value = 1,
                max_value = 10,
                step = 1,
                value = 1
            )
        with col2:
            sort = st.selectbox(
                '정렬',
                sorted
            )
        submit = st.form_submit_button('제출')
        if submit:
            country = country
            city = city
            people = people
            sort = sort
            hotel_crawling(country,city,people,sort)
    
