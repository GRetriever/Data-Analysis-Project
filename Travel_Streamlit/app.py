import streamlit as st
from openai import OpenAI

client = OpenAI(api_key = st.secrets['OPENAI_API_KEY'])

st.title("AI 여행 계획 짜기")
st.subheader("AI를 이용하여 손쉽게 여행 계획을 짜보세요!")

def generate_prompt(country,city,nights,days,places,activities,etc):
    prompt = f'''
{country}의 {city}에서 {nights}박 {days}일 여행 일정표를 만들어주세요.
{places}도 포함해주세요.
{activities}도 포함해 주세요.
장소,활동,요리가 주어질 경우 반드시 포함해야 합니다.
{etc}가 주어질 경우 반드시 고려하여 작성해주세요.
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


with st.form('form'):
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
     
    st.text('원하는 방문지를 입력하세요 (필수 아님)')
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
        
    st.text('원하는 활동을 입력하세요 (필수 아님)')
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
        '원하는 사항이 있으면 입력하세요'
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
            prompt = generate_prompt(
                country = country,
                city = city,
                nights = nights,
                days = days,
                places = places,
                activities = activities,
                etc = etc
            )
            response = request_chat_completion(prompt)
            print_streaming_response(response)