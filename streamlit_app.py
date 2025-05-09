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


# st.columns(n): 화면을 n개의 수직 열로 나눕니다
col1, col2 = st.columns(2)  # 2개의 열 생성

with col1:
    st.write("왼쪽 열입니다.")  # 첫 번째 열에 내용 작성
with col2:
    st.write("오른쪽 열입니다.")  # 두 번째 열에 내용 작성


# st.tabs(["이름1", "이름2", ...]): 탭 인터페이스 생성
tab1, tab2 = st.tabs(["탭 1", "탭 2"])  # 2개의 탭 생성

with tab1:
    st.write("탭 1에 해당하는 내용입니다.")  # 첫 번째 탭에 표시할 내용
with tab2:
    st.write("탭 2에 해당하는 내용입니다.")  # 두 번째 탭에 표시할 내용
st.snow()



n = st.text_area("이름:")
st.write(n+"안녕")

# 여러 옵션 중 하나 선택
gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
st.write("선택한 성별:", gender)
st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjNhZ2JkZjZncDFvYzdtdTkxcm95Nmd2cm8wNDBqczFvbHdmbWdsNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lv2VhwHrt6ljhvZ6LF/giphy.gif")