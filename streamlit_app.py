# import streamlit as st
# import openai

# # --- 기본 정보 출력 ---
# st.title("안녕")
# st.write("안녕하세요")
# st.divider()
# st.info("안녕안녕")

# # --- 버튼 및 체크박스 ---
# st.button("adf")

# agree = st.checkbox("위 조건에 동의합니다")
# if agree:
#     st.write("감사합니다! 계속 진행합니다.")
#     st.warning("!!")

# # --- 열(column) 분할 레이아웃 ---
# col1, col2 = st.columns(2)
# with col1:
#     st.write("왼쪽 열입니다.")
# with col2:
#     st.write("오른쪽 열입니다.")

# # --- 탭(Tab) UI 구성 ---
# tab1, tab2 = st.tabs(["탭 1", "탭 2"])
# with tab1:
#     st.write("탭 1에 해당하는 내용입니다.")
# with tab2:
#     st.write("탭 2에 해당하는 내용입니다.")

# # --- 사용자 입력: 이름 및 성별 ---
# name = st.text_area("이름:")
# st.write(f"{name}안녕")

# gender = st.radio("성별을 선택하세요", ["남성", "여성", "기타"])
# st.write("선택한 성별:", gender)

# # --- 이미지 삽입 ---
# st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjNhZ2JkZjZncDFvYzdtdTkxcm95Nmd2cm8wNDBqczFvbHdmbWdsNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lv2VhwHrt6ljhvZ6LF/giphy.gif")

# # --- GPT 프롬프트 입력 및 응답 ---
# st.subheader("🔑 OpenAI GPT와 대화하기")

# user_api_key = st.secrets["openai"]["api_key"]
# if user_api_key:
#     from openai import OpenAI

#     client = OpenAI(api_key=user_api_key)

#     prompt = st.text_input("프롬프트 입력")

#     if prompt:
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[{"role": "user", "content": prompt}]
#         )
#         st.markdown("### 💡 GPT의 답변:")
#         st.write(completion.choices[0].message.content)
# else:
#     st.warning("🔑 API 키가 입력되지 않았습니다!")
import streamlit as st
import openai

# --- 페이지 제목 ---
st.set_page_config(page_title="Streamlit 예제", layout="centered", page_icon= "😊")
st.title("🧪 Streamlit 인터페이스 예제")

# --- 탭 구성 ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 기본 정보", "📐 레이아웃", "🧑 입력", "💬 GPT", "🖼 이미지"
])

# --- 탭 1: 기본 정보 ---
with tab1:
    st.write("안녕하세요, 이 페이지는 Streamlit 기능 예제입니다.")
    st.divider()
    st.info("이곳은 정보 메시지입니다.")
    
    st.button("adf")

    agree = st.checkbox("위 조건에 동의합니다")
    if agree:
        st.success("감사합니다! 계속 진행합니다.")
        st.warning("⚠️ 주의하세요!")

# --- 탭 2: 레이아웃 ---
with tab2:
    col1, col2 = st.columns(2)
    with col1:
        st.write("📌 왼쪽 열입니다.")
    with col2:
        st.write("📌 오른쪽 열입니다.")
    
    tab_a, tab_b = st.tabs(["🔹 탭 A", "🔸 탭 B"])
    with tab_a:
        st.write("이곳은 탭 A의 내용입니다.")
    with tab_b:
        st.write("이곳은 탭 B의 내용입니다.")

# --- 탭 3: 사용자 입력 ---
with tab3:
    name = st.text_area("이름을 입력하세요:")
    if name:
        st.write(f"👋 {name}님, 안녕하세요!")
    
    gender = st.radio("성별을 선택하세요:", ["남성", "여성", "기타"])
    st.write(f"선택한 성별: {gender}")

# --- 탭 4: GPT 응답 ---
with tab4:
    st.subheader("🔑 OpenAI GPT와 대화하기")

    # secrets.toml 에 openai.api_key 가 저장되어 있어야 합니다
    user_api_key = st.secrets["openai"]["api_key"]

    if user_api_key:
        from openai import OpenAI
        client = OpenAI(api_key=user_api_key)

        prompt = st.text_input("프롬프트를 입력하세요:")

        if prompt:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            st.markdown("### 💡 GPT의 답변:")
            st.write(completion.choices[0].message.content)
    else:
        st.warning("🔐 API 키가 설정되어 있지 않습니다!")

# --- 탭 5: 이미지 출력 ---
with tab5:
    st.image(
        "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExcjNhZ2JkZjZncDFvYzdtdTkxcm95Nmd2cm8wNDBqczFvbHdmbWdsNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lv2VhwHrt6ljhvZ6LF/giphy.gif",
        caption="움직이는 이미지입니다 🎞️"
    )
