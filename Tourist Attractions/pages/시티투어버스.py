import streamlit as st
import pandas as pd
import folium

st.title('다함께 즐겨요~ 시티투어 버스')


tab_busan,tab_ulsan,tab_gyeongnam,tab_jeonnam,tab_gwangju = st.tabs(['부산','울산','경남(창원)','전남(여수)','광주'])
#============================================================

area = ['부산','울산','경남','전남','광주']
p_up = ['숨은 명소','일반 명소']
busan = pd.read_csv('./pages/data/busan_tour.csv')
ulsan = pd.read_csv('./pages/data/ulsan_tour.csv')
gyeongnam = pd.read_csv('./pages/data/gyeongnam_tour.csv')
jeonnam = pd.read_csv('./pages/data/jeonnam_tour.csv')
gwangju = pd.read_csv('./pages/data/gwangju_tour.csv')

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

with tab_busan:
    st.header('부산의 내륙과 바다, 둘 다 즐기는 투어버스')
    location = get_location(busan)
    map = folium.Map(location=[35.1578157,129.0600331],zoom_start=12)
    get_mark(busan)
    location = get_location(busan)
    folium.PolyLine(locations=location,tooltip='Polyline').add_to(map)
    st.components.v1.html(map._repr_html_(),width=800,height=500)
    draw_items(busan)

with tab_ulsan:
    st.header('뚜벅이의 뚜벅이에 의한 뚜벅이를 위한 울산 투어버스')
    location = get_location(ulsan)
    map = folium.Map(location=[35.5372222,129.37],zoom_start=11)
    get_mark(ulsan)
    location = get_location(ulsan)
    folium.PolyLine(locations=location,tooltip='Polyline').add_to(map)
    st.components.v1.html(map._repr_html_(),width=800,height=500)
    draw_items(ulsan)
    
with tab_gyeongnam:
    st.header('창원시 빙글빙글 투어버스')
    location = get_location(gyeongnam)
    map = folium.Map(location=[35.2028593,128.6000923],zoom_start=12)
    get_mark(gyeongnam)
    location = get_location(gyeongnam)
    folium.PolyLine(locations=location,tooltip='Polyline').add_to(map)
    st.components.v1.html(map._repr_html_(),width=800,height=500)
    draw_items(gyeongnam)

with tab_jeonnam:
    st.header('여수시 숨은 보섯 찾기, 우리끼리 투어버스')
    location = get_location(jeonnam)
    map = folium.Map(location=[34.7603737,127.6622221],zoom_start=11)
    get_mark(jeonnam)
    location = get_location(jeonnam)
    folium.PolyLine(locations=location,tooltip='Polyline').add_to(map)
    st.components.v1.html(map._repr_html_(),width=800,height=500)
    draw_items(jeonnam)

with tab_gwangju:
    st.header('광주의 숨은 명소 미션 클리어 투어버스')
    location = get_location(gwangju)
    map = folium.Map(location=[35.1557358,126.8354271],zoom_start=12)
    get_mark(gwangju)
    location = get_location(gwangju)
    folium.PolyLine(locations=location,tooltip='Polyline').add_to(map)
    st.components.v1.html(map._repr_html_(),width=800,height=500)
    draw_items(gwangju)