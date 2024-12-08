import streamlit as st
import numpy as np
from module import js_test

st.set_page_config(page_title="2048", page_icon="🖥")

# CSS 스타일 정의
st.markdown(
    """
    <style>
    .board {
        display: grid;
        grid-template-columns: repeat(4, 100px);
        grid-gap: 10px;
        margin: 20px auto;
        width: fit-content;
    }
    .cell {
        width: 100px;
        height: 100px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
        border: 1px solid #ccc;
        background-color: #eee;
    }
    .cell-2 { background-color: #eee4da; }
    .cell-4 { background-color: #ede0c8; }
    .cell-8 { background-color: #f2b179; }
    .cell-16 { background-color: #f59563; }
    .cell-32 { background-color: #f67c5f; }
    .cell-64 { background-color: #f75f3b; }
    .cell-128 { background-color: #edd073; }
    .cell-256 { background-color: #edcc61; }
    .cell-512 { background-color: #edc850; }
    .cell-1024 { background-color: #edc53f; }
    .cell-2048 { background-color: #edc22e; }

    .stHorizontalBlock {
        gap: 0rem;
        justify-content: center;
        padding: 1rem;
    }

    .st-emotion-cache-12w0qpk{
        width:100px;
        flex:none;
    }
    .st-emotion-cache-1r6slb0{
        width:60px;
        flex:none;
    }

    .st-key-up{
        position:absolute;
        margin-top: 450px;
    }
    
    .st-key-down{
        position:absolute;
        margin-top: 500px;
    }
    </style>
    """, unsafe_allow_html=True
)

# 초기 설정
def initialize_board():
    board = np.zeros((4, 4), dtype=int)
    for _ in range(2):
        add_random_tile(board)
    return board

def add_random_tile(board):
    empty_positions = list(zip(*np.where(board == 0)))
    if empty_positions:
        x, y = empty_positions[np.random.choice(len(empty_positions))]
        board[x, y] = np.random.choice([2, 4], p=[0.9, 0.1])  # 90% 확률로 2, 10% 확률로 4

# 게임 보드 그리기
def draw_board(board):
    cols = st.columns(4)
    for i in range(4):
        for j in range(4):
            cell_value = board[i, j]
            cell_class = f'cell cell-{cell_value}' if cell_value != 0 else 'cell'
            cols[j].markdown(f'<div class="{cell_class}">{cell_value if cell_value != 0 else ""}</div>', unsafe_allow_html=True)

# 보드 이동 및 합치기 로직
def move_board(board, direction):
    if direction == "up":
        for j in range(4):
            non_zero = [board[i][j] for i in range(4) if board[i][j] != 0]
            merged = []
            skip = False
            for i in range(len(non_zero)):
                if skip:
                    skip = False
                    continue
                if i + 1 < len(non_zero) and non_zero[i] == non_zero[i + 1]:
                    merged.append(non_zero[i] * 2)
                    skip = True
                else:
                    merged.append(non_zero[i])
            merged += [0] * (4 - len(merged))
            for i in range(4):
                board[i][j] = merged[i]
    
    elif direction == "down":
        for j in range(4):
            non_zero = [board[i][j] for i in range(4) if board[i][j] != 0]
            merged = []
            skip = False
            for i in range(len(non_zero) - 1, -1, -1):
                if skip:
                    skip = False
                    continue
                if i - 1 >= 0 and non_zero[i] == non_zero[i - 1]:
                    merged.append(non_zero[i] * 2)
                    skip = True
                else:
                    merged.append(non_zero[i])
            merged += [0] * (4 - len(merged))
            for i in range(4):
                board[3 - i][j] = merged[i]
    
    elif direction == "left":
        for i in range(4):
            non_zero = [board[i][j] for j in range(4) if board[i][j] != 0]
            merged = []
            skip = False
            for j in range(len(non_zero)):
                if skip:
                    skip = False
                    continue
                if j + 1 < len(non_zero) and non_zero[j] == non_zero[j + 1]:
                    merged.append(non_zero[j] * 2)
                    skip = True
                else:
                    merged.append(non_zero[j])
            merged += [0] * (4 - len(merged))
            for j in range(4):
                board[i][j] = merged[j]
    
    elif direction == "right":
        for i in range(4):
            non_zero = [board[i][j] for j in range(4) if board[i][j] != 0]
            merged = []
            skip = False
            for j in range(len(non_zero) - 1, -1, -1):
                if skip:
                    skip = False
                    continue
                if j - 1 >= 0 and non_zero[j] == non_zero[j - 1]:
                    merged.append(non_zero[j] * 2)
                    skip = True
                else:
                    merged.append(non_zero[j])
            merged += [0] * (4 - len(merged))
            for j in range(4):
                board[i][3 - j] = merged[j]

    return board

# 게임 오버 상태 체크
def is_game_over(board):
    if np.any(board == 0):
        return False
    for direction in ["up", "down", "left", "right"]:
        test_board = board.copy()
        if not np.array_equal(move_board(test_board, direction), board):
            return False
    return True

# 점수 계산
def calculate_score(board):
    return np.sum(board)

st.title("2048 게임")
if 'board' not in st.session_state:
    st.session_state.board = initialize_board()

# 점수 표시
score = calculate_score(st.session_state.board)
st.write(f"**점수:** {score}")

if st.button("리셋"):
    st.session_state.board = initialize_board()
    st.write("게임이 리셋되었습니다.")

with st.container(key="score"):
    score = calculate_score(st.session_state.board)
    st.write(f"**점수:** {score}")

with st.container(key="up"):
    col1, col2, col3 = st.columns(3)
    with col2:
        if st.button("↑"):
            st.session_state.board = move_board(st.session_state.board, "up")
            add_random_tile(st.session_state.board)

with st.container(key="down"):
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("←"):
            st.session_state.board = move_board(st.session_state.board, "left")
            add_random_tile(st.session_state.board)
    with col2:
        if st.button("↓"):
            st.session_state.board = move_board(st.session_state.board, "down")
            add_random_tile(st.session_state.board)
    with col3:
        if st.button("→"):
            st.session_state.board = move_board(st.session_state.board, "right")
            add_random_tile(st.session_state.board)

draw_board(st.session_state.board)

# 게임 오버 메시지
if is_game_over(st.session_state.board):
    st.error("게임 오버! 더 이상 이동할 수 없습니다.") 
