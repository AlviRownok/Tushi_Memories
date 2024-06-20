import streamlit as st
from PIL import Image
import numpy as np
import random

# Load and split the image
def load_image(image_path):
    img = Image.open(image_path)
    return img

def split_image(img, grid_size):
    w, h = img.size
    piece_w, piece_h = w // grid_size, h // grid_size
    pieces = []
    for i in range(grid_size):
        row = []
        for j in range(grid_size):
            piece = img.crop((j * piece_w, i * piece_h, (j + 1) * piece_w, (i + 1) * piece_h))
            row.append(piece)
        pieces.append(row)
    return pieces

def create_puzzle(grid_size):
    puzzle = list(range(1, grid_size * grid_size)) + [0]
    random.shuffle(puzzle)
    return np.array(puzzle).reshape((grid_size, grid_size))

def find_empty(puzzle):
    return np.argwhere(puzzle == 0)[0]

def is_adjacent(empty, position):
    return (abs(empty[0] - position[0]) == 1 and empty[1] == position[1]) or \
           (abs(empty[1] - position[1]) == 1 and empty[0] == position[0])

def move_piece(puzzle, position):
    empty = find_empty(puzzle)
    if is_adjacent(empty, position):
        puzzle[empty[0], empty[1]], puzzle[position[0], position[1]] = \
        puzzle[position[0], position[1]], puzzle[empty[0], empty[1]]
    return puzzle

def check_puzzle(puzzle):
    return np.array_equal(puzzle, np.arange(1, puzzle.size + 1).reshape(puzzle.shape))

# Game settings
grid_size = 3
image_path = "tushi_guess_game/Image_1.jpeg"

# Load and split image
img = load_image(image_path)
pieces = split_image(img, grid_size)

# Initialize puzzle state
if 'puzzle' not in st.session_state:
    st.session_state.puzzle = create_puzzle(grid_size)

st.title("Sliding Puzzle Game")
st.write("Arrange the pieces to solve the puzzle!")

# Display puzzle
puzzle = st.session_state.puzzle
empty = find_empty(puzzle)
cols = st.columns(grid_size)

for i in range(grid_size):
    for j in range(grid_size):
        piece_idx = puzzle[i, j]
        if piece_idx != 0:  # Skip the empty piece
            with cols[j]:
                if is_adjacent(empty, (i, j)):
                    if st.button('', key=f'{i}-{j}', on_click=move_piece, args=(st.session_state.puzzle, (i, j))):
                        st.experimental_rerun()
                st.image(pieces[(piece_idx - 1) // grid_size][(piece_idx - 1) % grid_size], use_column_width=True)

# Shuffle button
if st.button("Shuffle"):
    st.session_state.puzzle = create_puzzle(grid_size)

# Check if solved
if check_puzzle(st.session_state.puzzle):
    st.balloons()
    st.write("Congratulations! You've solved the puzzle!")
