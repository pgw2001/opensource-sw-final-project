import streamlit as st
import numpy as np
import random

def check_valid(board, row, col, num):
    if num in board[row]:
        return False
    if num in [board[i][col] for i in range(9)]:
        return False
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if check_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def fill_sudoku(board):
    solve_sudoku(board)
    return board

def remove_numbers(board, difficulty=0.5):
    num_to_remove = int(difficulty * 81)
    while num_to_remove > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            num_to_remove -= 1
    return board

def create_sudoku_board():
    board = np.zeros((9, 9), dtype=int)
    filled_board = fill_sudoku(board)
    puzzle_board = remove_numbers(filled_board, difficulty=0.5)
    return puzzle_board

def display_board(board):
    """3x3 블록마다 다른 배경색 추가하여 구분"""
    colors = [
        "#f0f8ff", "#e6f7ff", "#d9f0ff",  # 배경색 1~3
        "#f7f9fc", "#f0f5fa", "#eaf0f9",  # 배경색 4~6
        "#f5fbfc", "#e5f5f9", "#d5eff5"   # 배경색 7~9
    ]

    for i in range(9):
        cols = st.columns(9, gap="small")
        for j in range(9):
            value = int(board[i][j]) if board[i][j] != 0 else ''
            box_id = (i // 3) * 3 + (j // 3)  # 3x3 블록의 인덱스 계산
            style = f"""
                border: 1px solid black; 
                background-color: {colors[box_id]};
                font-size: 18px; 
                text-align: center; 
                width: 40px; 
                height: 40px;
            """
            
            cols[j].markdown(
                f"""
                <input type="text" maxlength="1" value="{value}" 
                style="{style}" 
                oninput="this.value=this.value.replace(/[^1-9]/g,'');">
                """,
                unsafe_allow_html=True
            )

def check_completion(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return False
    return True

def main():
    st.title("스도쿠 게임")
    st.write("스도쿠 퍼즐을 해결해보세요! 빈 칸에 숫자를 입력하세요.")
    
    if 'board' not in st.session_state:
        st.session_state.board = create_sudoku_board()

    # CSS 스타일 정의
    st.markdown("""
        <style>
        input {
            font-family: Arial, sans-serif;
        }
        </style>
    """, unsafe_allow_html=True)

    # 스도쿠 보드 표시
    display_board(st.session_state.board)

    if st.button("제출"):
        for i in range(9):
            for j in range(9):
                val = st.session_state.get(f"{i}-{j}", "")
                if val.isdigit() and 1 <= int(val) <= 9:
                    st.session_state.board[i][j] = int(val)
                else:
                    st.session_state.board[i][j] = 0

        if check_completion(st.session_state.board):
            st.success("클리어! 스도쿠를 모두 맞췄습니다!")
        else:
            st.warning("아직 모든 칸이 채워지지 않았습니다.")

if __name__ == "__main__":
    main()