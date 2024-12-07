import streamlit as st
import numpy as np

def check_valid(board, row, col, num):
    for c in range(9):
        if c != col and board[row][c] == num:
            return False
    for r in range(9):
        if r != row and board[r][col] == num:
            return False
    box_row, box_col = row // 3 * 3, col // 3 * 3
    for i in range(3):
        for j in range(3):
            if (box_row + i != row or box_col + j != col) and board[box_row + i][box_col + j] == num:
                return False
    return True

def create_sudoku_board(difficulty=0.5):
    board = np.zeros((9, 9), dtype=int)
    def fill_board(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    nums = np.random.permutation(range(1, 10))
                    for num in nums:
                        if check_valid(board, row, col, num):
                            board[row][col] = num
                            if fill_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True
    fill_board(board)
    num_to_remove = int(difficulty * 81)
    coords = [(r, c) for r in range(9) for c in range(9)]
    np.random.shuffle(coords)
    for r, c in coords[:num_to_remove]:
        board[r][c] = 0
    return board

st.set_page_config(page_title="Sudoku Game", page_icon="🧩", layout="centered")

def main():
    st.title("🧩 스도쿠 게임")
    st.write("각 행, 열, 3x3 박스에 1-9 숫자가 중복되지 않도록 채워주세요!")

    if 'board' not in st.session_state:
        st.session_state.board = create_sudoku_board()
        st.session_state.original_board = st.session_state.board.copy()
        st.session_state.invalid_positions = []

    difficulty_levels = 5
    difficulty_step = 0.5 / (difficulty_levels - 1)
    difficulty_map = {i + 1: i * difficulty_step + 0.1 for i in range(difficulty_levels)}
    
    selected_difficulty = st.slider("난이도 선택 (1-5단계)", min_value=1, max_value=difficulty_levels, value=3, step=1)
    difficulty = difficulty_map[selected_difficulty]

    col1, col2 = st.columns(2)
    with col1:
        if st.button("새 게임"):
            st.session_state.board = create_sudoku_board(difficulty)
            st.session_state.original_board = st.session_state.board.copy()
            st.session_state.invalid_positions = []

    with col2:
        if st.button("난이도 적용"):
            st.session_state.board = create_sudoku_board(difficulty)
            st.session_state.original_board = st.session_state.board.copy()
            st.session_state.invalid_positions = []

    board_container = st.container()
    with board_container:
        board = st.session_state.board
        original_board = st.session_state.original_board

        colors = [
            "#FFEBEE", "#E3F2FD", "#E8F5E9",
            "#FFF3E0", "#F3E5F5", "#EDE7F6",
            "#FBE9E7", "#E1F5FE", "#F9FBE7"
        ]

        for i in range(9):
            cols = st.columns(9)
            for j in range(9):
                box_id = (i // 3) * 3 + (j // 3)
                if original_board[i, j] != 0:
                    cols[j].markdown(f'''
                        <div style="
                            background-color: {colors[box_id]};
                            width: 50px;
                            height: 50px;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            font-size: 24px;
                            font-weight: bold;
                            border: 1px solid black;
                        ">
                            {original_board[i, j]}
                        </div>
                    ''', unsafe_allow_html=True)
                else:
                    input_value = cols[j].text_input(
                        f"cell_{i}_{j}",
                        value=str(board[i, j]) if board[i, j] != 0 else '',
                        max_chars=1,
                        label_visibility='collapsed',
                        key=f'input_{i}_{j}'
                    )
                    if input_value.isdigit() and 1 <= int(input_value) <= 9:
                        board[i, j] = int(input_value)
                    else:
                        board[i, j] = 0  # 유효하지 않은 경우 0으로 설정

    if st.button("제출"):
        st.session_state.invalid_positions = []
        for i in range(9):
            for j in range(9):
                if st.session_state.original_board[i, j] == 0:  # 사용자가 입력한 칸만 검증
                    if board[i, j] != 0 and not check_valid(board, i, j, board[i, j]):
                        st.session_state.invalid_positions.append((i, j))

        if np.all(st.session_state.board != 0):
            if not st.session_state.invalid_positions:
                st.success("축하합니다! 스도쿠를 완성했습니다!")
            else:
                st.error("잘못된 입력이 있습니다! 빨간색으로 표시된 칸을 확인하세요.")
        else:
            st.warning("아직 모든 칸을 채우지 않았습니다.")

    for pos in st.session_state.invalid_positions:
        row, col = pos
        st.markdown(f'<div style="color:red;">({row + 1}, {col + 1}) 위치에 잘못된 숫자가 있습니다!</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()