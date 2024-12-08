import streamlit as st
import numpy as np
import time
import streamlit_shortcuts
import random

# 그리드 크기
rows = 10
cols = 10
update_interval = 0.3  # 0.3초마다 업데이트

# 페이지 로드 시 session_state 초기화
if "game_state" not in st.session_state or "game_started" not in st.session_state:
    st.session_state.game_state = {
        "snake": [(2, 2), (2, 1), (2, 0)],
        "direction": (0, 1),
        "food": (5, 5),
        "score": 0,
        "game_over": False,
        "last_update": time.time(),
        "fruit": "🍐"
    }
    st.session_state.game_started = False  # 게임 시작 여부를 추적하는 변수 추가

def place_food(snake):
    empty_cells = [(r, c) for r in range(rows) for c in range(cols) if (r, c) not in snake]
    return empty_cells[np.random.choice(len(empty_cells))]

def set_fruit(fruits):
    return fruits[random.randint(0, len(fruits)-1)]

def on_button_click():
    if st.session_state.game_state["game_over"]:
        st.session_state.game_state = {
            "snake": [(2, 2), (2, 1), (2, 0)],
            "direction": (0, 1),
            "food": place_food(st.session_state.game_state["snake"]),
            "score": 0,
            "game_over": False,
            "last_update": time.time(),
            "fruit": "🍐"
        }

def start_game():
    st.session_state.game_started = True  # 게임 시작 상태를 True로 설정
    st.session_state.game_state = {
        "snake": [(2, 2), (2, 1), (2, 0)],
        "direction": (0, 1),
        "food": place_food([]),
        "score": 0,
        "game_over": False,
        "last_update": time.time(),
        "fruit": "🍐"
    }

def update_snake():
    snake = st.session_state.game_state["snake"]
    direction = st.session_state.game_state["direction"]
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if new_head[0] < 0 or new_head[0] >= rows or new_head[1] < 0 or new_head[1] >= cols or new_head in snake:
        st.session_state.game_state["game_over"] = True
        return

    snake.insert(0, new_head)

    if new_head == st.session_state.game_state["food"]:
        st.session_state.game_state["food"] = place_food(snake)
        st.session_state.game_state["fruit"] = set_fruit(["🍎", "🍓", "🍒", "🍊", "🍉"])
        st.session_state.game_state["score"] += 1
    else:
        snake.pop()

def render_grid():
    snake = st.session_state.game_state["snake"]
    food = st.session_state.game_state["food"]
    fruit = st.session_state.game_state["fruit"]
    
    for row in range(rows):
        columns = st.columns(cols)
        for col_index, col in enumerate(columns):
            with col.container():
                if (row, col_index) == food:
                    col.button(fruit, key=f"button_{row}_{col_index}")
                elif (row, col_index) in snake:
                    col.button("", key=f"button_{row}_{col_index}", type="primary")
                else:
                    col.button("", key=f"button_{row}_{col_index}", disabled=True)

def control_snake(key):
    if st.session_state.game_state["game_over"]:
        return
    direction_map = {
        "↑": (-1, 0),
        "↓": (1, 0),
        "←": (0, -1),
        "→": (0, 1)
    }

    current_direction = st.session_state.game_state["direction"]
    new_direction = direction_map[key]
    if (current_direction[0] + new_direction[0], current_direction[1] + new_direction[1]) != 0:
        st.session_state.game_state["direction"] = new_direction

def up_callback():
    return control_snake("↑")

def down_callback():
    return control_snake("↓")

def left_callback():
    return control_snake("←")

def right_callback():
    return control_snake("→")

# 게임 조작 방법 설명
st.title("Snake 게임")
st.markdown(
    """
    ### 🎮 조작 방법은 다음과 같습니다. <br>
    1) 게임 아래에 존재하는 **버튼**을 눌러 이동
    2) **단축키**를 사용 (추천)
    - Shift + W : 위로 이동 
    - Shift + A : 왼쪽으로 이동
    - Shift + S : 아래로 이동 
    - Shift + D : 오른쪽으로 이동
    <br><br>

    
     
    ### [Snake 게임]
    """,
    unsafe_allow_html=True
)

# 사이드바에서 페이지 전환 시 초기화 처리
if "game_started" in st.session_state and not st.session_state.game_started:
    st.session_state.game_state = {
        "snake": [(2, 2), (2, 1), (2, 0)],
        "direction": (0, 1),
        "food": (5, 5),
        "score": 0,
        "game_over": False,
        "last_update": time.time(),
        "fruit": "🍐"
    }

# 게임 시작 여부에 따라 화면을 달리 렌더링
if not st.session_state.game_started:
    st.button("게임 시작", on_click=start_game)
else:
    current_time = time.time()
    if current_time - st.session_state.game_state["last_update"] >= update_interval:
        st.session_state.game_state["last_update"] = current_time
        if not st.session_state.game_state["game_over"]:
            update_snake()
            render_grid()
            st.rerun()  # 게임이 끝나지 않은 경우에만 rerun
        else:
            render_grid()  # 게임이 끝났을 때는 rerun 없이 그리드만 렌더링
    else:
        render_grid()

    # 단축키를 이용한 조작 설정
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            streamlit_shortcuts.button("←", on_click=left_callback, shortcut="Shift+A")
        with col2:
            streamlit_shortcuts.button("↑", on_click=up_callback, shortcut="Shift+W")
        with col3:
            streamlit_shortcuts.button("→", on_click=right_callback, shortcut="Shift+D")

    # 아래쪽 버튼 추가
    col1, col2, col3 = st.columns(3)
    with col2:
        streamlit_shortcuts.button("↓", on_click=down_callback, shortcut="Shift+S")

    st.button("재시작", on_click=on_button_click)
    st.text(f"점수: {st.session_state.game_state['score']}")

    # 게임이 끝났을 때만 'Game Over' 텍스트 표시
    if st.session_state.game_state["game_over"]:
        st.balloons()

    # 이 구문은 게임이 종료되지 않으면 새로 고침을 유발
    time.sleep(update_interval)

    if not st.session_state.game_state["game_over"]:
        st.rerun()
