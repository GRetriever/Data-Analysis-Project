import streamlit as st
from openai import OpenAI
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import requests
from PIL import Image
from io import BytesIO


client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])

st.title("AI 여행 계획 짜기")
st.subheader("어디로 떠나고 싶나요?")

def generate_itinerary(country,city,nights,days,places,activities,etc):
    prompt = f'''
{country}의 {city}에서 {nights}박 {days}일 여행 일정표를 만들어주세요.
{places}도 포함해주세요.
{activities}도 포함해 주세요.
장소,활동,요리가 주어질 경우 반드시 포함해야 합니다.
{etc}가 주어질 경우 반드시 고려하여 작성해주세요.
마지막으로 {city}를 여행할 때 주의해야 될 사항을 3가지만 알려주세요.
---
국가 : {country}
도시 : {city}
일정 : {nights}박 {days}일
방문지 : {places}
활동 : {activities}
---    
    '''.strip()
    return prompt

def request_chat_completion(prompt):
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role' : 'system', 'content' : '당신은 전문 여행계획가 입니다.'},
            {'role' : 'user', 'content' : prompt}
        ],
        stream = True
    )
    return response

def print_streaming_response(response):
    message = ''
    placeholder = st.empty()
    for chunk in response:
        delta = chunk.choices[0].delta
        if delta.content:
            message += delta.content
            placeholder.markdown(message + "▌")
    placeholder.markdown(message)

def information_crawling(country,city):
    options = Options()
    options.headless = True
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    actions = ActionChains(driver)
    url = 'https://www.naver.com/'
    
    driver.get(url)
    time.sleep(1)
    
    driver.find_element('xpath','//*[@id="query"]').send_keys(country,city)
    driver.find_element('xpath','//*[@id="search-btn"]').click()
    time.sleep(1)
    
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
        st.image([img_1, img_2], caption=['Web Crawled Image 1', 'Web Crawled Image 2'], width=330)

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

    

tab_itineary,tab_weather,tab_food = st.tabs(['일정','날씨','음식'])

# =====================================================================================================

with tab_itineary:
    with st.form('form1'):
        st.text('아래의 정보를 입력하세요.')
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
            nights = st.number_input(
                '0 박 (필수)',
                min_value = 0,
                max_value = 30,
                step = 1,
                value = 3
            )
        with col2:
            days = st.number_input(
                '0 일 (필수)',
                min_value = 1,
                max_value = 30,
                step = 1,
                value = 4
            )
        st.text('원하는 방문지를 입력하세요. (필수 아님)')
        col1,col2,col3 = st.columns(3)
        with col1:
            place_one = st.text_input(
                '방문지1'
            )
        with col2:
            place_two = st.text_input(
                '방문지2'
            )
        with col3:
            place_three = st.text_input(
                '방문지3'
            )
            
        st.text('원하는 활동을 입력하세요. (필수 아님)')
        col1,col2,col3 = st.columns(3)
        with col1:
            activity_one = st.text_input(
                '활동1'
            )
        with col2:
            activity_two = st.text_input(
                '활동2'
            )
        with col3:
            activity_three = st.text_input(
                '활동3'
            )
        etc = st.text_input(
            '원하는 사항이 있으면 입력하세요. (필수 아님)'
        )
        submit = st.form_submit_button('제출하기')
        if submit:
            if not country:
                st.error('국가를 입력해주세요.')
            elif not city:
                st.error('도시를 입력해주세요.')
            else:
                places = [place_one,place_two,place_three]
                places = [x for x in places if x]
                activities = [activity_one,activity_two,activity_three]
                activities = [x for x in activities if x]
                etc = [x for x in etc if x]
                prompt = generate_itinerary(
                    country = country,
                    city = city,
                    nights = nights,
                    days = days,
                    places = places,
                    activities = activities,
                    etc = etc
                )
                response = request_chat_completion(prompt)
                information_crawling(country,city)
                st.write('======================================================================')
                print_streaming_response(response)

# ===========================================================================================

def generate_weather(country,city,month):
    prompt = f'''
{month}월에 {country}의 {city}를 여행할겁니다.
해당 {city}의 {month}월 날씨와 가져갈 옷을 추천해주세요.
'''.strip()
    return prompt
                
with tab_weather:
    with st.form('form2'):
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
            if not country:
                st.error('국가를 입력해주세요.')
            elif not city:
                st.error('도시를 입력해주세요.')
            elif not month:
                st.error('월을 입력해주세요.')
            else:
                prompt = generate_weather(
                    country = country,
                    city = city,
                    month = month
                )
                response = request_chat_completion(prompt)
                print_streaming_response(response)
                
# ======================================================================================================

def generate_food(country,city):
    prompt = f'''
{country}의 {city}를 여행할겁니다.
해당 {city}의 맛있는 요리 3가지 추천해주세요.
'''.strip()
    return prompt

with tab_food:
    with st.form('form3'):
        st.text('아래의 정보를 입력하세요.')
        col1,col2 = st.columns(2)
        with col1:
            country = st.text_input(
                '국가 (필수)'
            )
        with col2:
            city = st.text_input(
                '도시 (필수)'
                
            )
        submit = st.form_submit_button('제출')
        if submit:
            if not country:
                st.error('국가를 입력해주세요.')
            elif not city:
                st.error('도시를 입력해주세요.')
            else:
                prompt = generate_food(
                    country = country,
                    city = city
                )
                response = request_chat_completion(prompt)
                print_streaming_response(response)

# =========================================================================================================
