import streamlit as st

st.write("Welcom~!! ")
st.write("LEO 1004 Home")
st.write("")
st.write("")
st.write("")


# 기본 버튼 생성
button = st.button("S토드")
if button:
    st.write("S토드는 어렵다")

st.link_button("15세 이상만 누르세요", "https://youtu.be/pz2HZLcg8P8?si=NZHum11YRcXTIuoG")


leo_text = st.chat_input("귀멸의 칼날에서 어떤 캐릭터를 가장 좋아하나요?")
if leo_text:
    st.write(f"{leo_text} 좋아하시는군요~!")
    
option = st.selectbox("좋아하는 캐릭터를 고르세요.", ["탄지로", "네즈코", "렌고쿠", "코쿠시보", "젠이츠","상현1","귀살대"])
st.write(f"선택한 캐릭터는 : {option} 이네요")
