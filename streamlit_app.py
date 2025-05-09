import streamlit as st

st.title("안녕")
st.write("안녕하세요")
st.divider()
st.info("안녕안녕")
st.button("adf")
# 체크 여부에 따라 분기
agree = st.checkbox("위 조건에 동의합니다")
if agree:
    st.write("감사합니다! 계속 진행합니다.")
    st.warning("!!")