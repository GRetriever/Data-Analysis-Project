import streamlit as st
import streamlit as st
from tkinter.tix import COLUMN
from pyparsing import empty

st.title('🚄숨겨진 명소를 찾아서')
st.write('AI를 이용하여 원하는 관광지 특성을 입력하여 숨겨진 명소를 추천 받아보세요!')

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

st.subheader('소개')
st.write('이 프로젝트는 숨은 관광 명소 발굴, 투어버스 노선 개발을 통해 오버투어리즘을 예방 및 해소하기 위해 진행되었습니다.')
         
st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

st.subheader('배경')
st.write(' ')

st.markdown('1. 여행 관심도 급증')
col1,col2 = st.columns([0.6,0.4])
with col1:
    st.image('./pages/data/img_001.png')
with col2:
    st.write("코로나19 확산 여파에 3년여 동안 억눌렸던 여행심리가 폭발하며 관광객 추이는 크게 증가하고 있습니다. 앞으로 여행 수요는 더욱 증가할 것으로 예상되며, 이로인한 피해가 발생하지 않도록 할 필요성을 느꼈습니다.")
st.write(' ')

st.markdown('2. 나만의 명소 여행 트랜드')
col1,col2 = st.columns([0.6,0.4])
with col1:
    st.image('./pages/data/img_002.png')
with col2:
    st.write("인구 구조의 변화와 SNS의 발달으로 인해 여행객들은 흔히 알려진 관광지보다는 덜 알려진 숨겨진 관광지를 찾는 경향이 있습니다. 이에 따라, 대중교통 이용량을 분석하여 각 지역의 숨겨진 명소를 발견하고 시티투어버스 노선을 개발하여 여행객을 분산시킬 수 있습니다.")
st.write(' ')

st.markdown('3. 오버투어리즘')
col1,col2 = st.columns([0.6,0.4])
with col1:
    st.image('./pages/data/img_003.png')
with col2:
    st.write('관광 수요 증가와 sns의 발달로 관광객들이 특정 관광지에 과도하게 쏠리는 현상이 발생하고 있습니다. 이는 여행객뿐만 아니라 해당 지역 주민들의 삶에도 부정적인 영향을 미칩니다. 이를 해소하기 위해 다양한 지자체에서 오버투어리즘 예방 및 해소를 위해 노력하고 있습니다.')
st.write(' ')
    
st.markdown('4. 남부권 광역관광 개발')
col1,col2 = st.columns([0.6,0.4])
with col1:
    st.image('./pages/data/img_004.png')
with col2:
    st.write("‘남부권 광역관광 개발계획’은 현 정부의 국정과제에 반영되어 내년부터 시작되는 총 3조 원 규모의 초대형 국책사업으로, 남부권을 수도권에 대응하는 지속 가능하고 경쟁력 있는 대한민국 관광의 중심지로 조성하기 위한 프로젝트입니다. 이에 발맞춰 남부권 지역으로 초점을 맞추고자 합니다.")
    st.write(' ')