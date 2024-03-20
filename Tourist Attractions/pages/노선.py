import streamlit as st
import pandas as pd
import folium

st.title('시티투어 버스 함 타봐라 개안터라')

#============================================================

area = ['부산','울산','경남','전남','광주']
p_up = ['숨은 명소','일반 명소']
busan = pd.read_csv('./pages/data/busan_tour.csv')

def get_location(df):
    location = []
    for i,row in df.iterrows():
        location.append([row['latitude'],row['longitude']])
    location.append(location[0])
    return location

def get_mark(df):
    for i in range(len(df)):
        folium.Marker(
            [df.iloc[i]['latitude'],df.iloc[i]['longitude']],
            popup=folium.Popup(df.iloc[i]['관광지명'],maxWidth=300),
            fill_opacity=0.5,
            icon=folium.Icon(color='blue')            
            ).add_to(map)

def draw_items(df):
    for i,item in df.iterrows():
        if i == 0:
            continue
        if pd.isna(item['img']):
            continue
        with st.expander(f'{i}번 : {item['관광지명']}'):
            st.write(item['catch'])
            col1,col2 = st.columns([0.4,0.6])
            with col1:
                st.image(item['img'])
            with col2:
                st.write(item['description'])
                
#================================================================

with st.form('form'):
    
    지역 = st.selectbox(
        '지역',
        area
    )
    submit = st.form_submit_button('제출')
if submit:
    st.header('부산의 내륙과 바다 지기네!!')
    location = get_location(busan)
    map = folium.Map(location=[35.115225,129.042243],zoom_start=11)
    get_mark(busan)
    location = get_location(busan)
    folium.PolyLine(locations=location,tooltip='Polyline').add_to(map)
    st.components.v1.html(map._repr_html_(),width=800,height=500)
    draw_items(busan)