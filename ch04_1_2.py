import streamlit as st
# 기본 버튼 생성
button = st.button("뿡대")
if button:
    st.write("우리가족은 대식가인데 방귀를 자주 껴서 뿡뿡이다.")
# 링크 바로가기 버튼 생성
st.link_button("이 버튼을 누르시면 안 됨", "https://poki.com/kr")
# 텍스트 입력 위젯
jenny_text = st.chat_input("데이식스 중에 어떤 멤버를 좋아하세요?")
if jenny_text:
    st.write(f"당신은 {jenny_text}를 좋아하는군요.")
# 드롭다운 선택 위젯
option = st.selectbox("좋아하는 멤버를 고르세요.", ["박성진", "강영현", "김원필", "윤도운"])
st.write(f"선택한 멤버: {option}")