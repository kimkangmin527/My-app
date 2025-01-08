import streamlit as st
import random

players = {
    "Lionel Messi": "아르헨티나 출신, 현재 미국 인터 마이애미 소속으로 활동 중인 전설적인 선수입니다.",
    "Cristiano Ronaldo": "포르투갈 출신, 현재 사우디 알나스르에서 활동 중이며 다수의 골 기록을 보유하고 있습니다.",
    "Neymar": "브라질 출신, 기술적이고 화려한 플레이로 유명한 공격수입니다.",
    "Kylian Mbappé": "프랑스 출신, 파리 생제르맹에서 뛰고 있으며 빠른 스피드로 유명합니다.",
    "Zlatan Ibrahimović": "스웨덴 출신, 세계 여러 리그에서 활약한 카리스마 넘치는 스트라이커입니다.",
    "Son Heung-min": "대한민국 출신, 현재 토트넘 홋스퍼에서 뛰고 있는 아시아 최고의 선수입니다."
}

# 퀴즈 함수
def football_quiz():
    st.title("⚽ 축구 선수 이름 맞추기 퀴즈")
    st.write("힌트를 보고 축구 선수의 이름을 맞춰보세요!")

    # 세션 상태 초기화
    if "score" not in st.session_state:
        st.session_state.score = 0
        st.session_state.question = None
        st.session_state.answer = None

    # 새로운 질문 생성
    if st.session_state.question is None:
        st.session_state.question, st.session_state.answer = random.choice(list(players.items()))

    # 질문 표시
    st.write(f"힌트: {st.session_state.question}")

    # 사용자 입력 받기
    user_answer = st.text_input("정답을 입력하세요:", key="user_answer")

    if st.button("제출"):
        if user_answer.strip().lower() == st.session_state.answer.lower():
            st.success(f"정답입니다! 선수 이름은 {st.session_state.answer}입니다.")
            st.session_state.score += 1
        else:
            st.error(f"틀렸습니다. 정답은 {st.session_state.answer}입니다.")

        # 새로운 질문으로 갱신
        st.session_state.question = None

    # 점수 표시
    st.write(f"현재 점수: {st.session_state.score}")

# 실행
if __name__ == "__main__":
    football_quiz()
