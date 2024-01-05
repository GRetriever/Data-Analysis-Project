import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])


def generate_itinerary(flight,continent,price,area,population,etc):
    prompt = f'''
{continent}대륙에 있는 국가 1곳을 추천해주세요.
한국에서 출발하는 비행기의 비행시간은 {flight} 입니다.
그 국가의 물가는 {price} 수준입니다.
목적지는 {area}이며, 목적지의 인기도는 {population} 입니다.
{etc}
---
비행시간 : {flight}
대륙 : {continent}
물가 : {price}
인기도 : {population}
특이사항 : {etc}
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



st.title(' ')
st.title('여행지 추천받기!')
st.subheader('🌎 어디로 갈지 못 정하셨나요?')
st.subheader('✈️ 원하는 조건의 여행지를 AI에게 추천받아보세요!')
st.title(' ')


flight = ['상관없음','1시간','2시간','3시간','4시간','5시간','6시간','7시간','8시간','9시간','10시간']
continents = ['전체','아시아','아프리카','북미','남미','유럽','오세아니아','남극']
price = ['상관없음','상','중','하']
area = ['상관없음','산','도시','바다','자연']
population = ['상관없음','상','중','하']

with st.form('form'):
    col1,col2 = st.columns(2)
    with col1:
        flight = st.selectbox(
            '비행시간',
            flight
        )
    col1,col2 = st.columns(2)
    with col1:
        continent = st.selectbox(
            '대륙',
            continents
        )
    col1,col2 = st.columns(2)
    with col1:
        price = st.selectbox(
            '물가',
            price
        )
    col1,col2 = st.columns(2)
    with col1:
        area = st.selectbox(
            '특징',
            area
        )
    col1,col2 = st.columns(2)
    with col1:
        population = st.selectbox(
            '인기도',
            population
        )
    col1,col2 = st.columns(2)
    with col1:
        etc = st.text_input(
            '원하는 사항을 입력하세요'
        )
    submit = st.form_submit_button('제출')
    if submit:
        prompt = generate_itinerary(
            flight = flight,
            continent = continent,
            price = price,
            area = area,
            population = population,
            etc = etc
        )
        response = request_chat_completion(prompt)
        print_streaming_response(response)