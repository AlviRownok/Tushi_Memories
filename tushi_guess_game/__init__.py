import streamlit as st
from PIL import Image
import random
import numpy as np

# Function to load and prepare the image
def load_image(image_path):
    image = Image.open(image_path)
    image = image.resize((400, 400))  # Resize for simplicity
    return image

# Function to split the image into a grid
def split_image(image, grid_size):
    width, height = image.size
    tile_width = width // grid_size
    tile_height = height // grid_size
    tiles = []
    for i in range(grid_size):
        for j in range(grid_size):
            box = (j*tile_width, i*tile_height, (j+1)*tile_width, (i+1)*tile_height)
            tile = image.crop(box)
            tiles.append(tile)
    return tiles

# Function to shuffle the tiles
def shuffle_tiles(grid_size):
    tile_positions = [(i, j) for i in range(grid_size) for j in range(grid_size)]
    random.shuffle(tile_positions)
    empty_tile = tile_positions.pop()
    return tile_positions, empty_tile

# Function to draw the current state of the puzzle
def draw_puzzle(tiles, tile_positions, empty_tile, grid_size):
    puzzle_image = Image.new('RGB', (400, 400))
    tile_width = 400 // grid_size
    tile_height = 400 // grid_size
    for index, pos in enumerate(tile_positions):
        if pos != empty_tile:
            tile = tiles[index]
            box = (pos[1]*tile_width, pos[0]*tile_height)
            puzzle_image.paste(tile, box)
    return puzzle_image

# Initialize the game state
if 'initialized' not in st.session_state:
    image_path = 'tushi_guess_game/Image_1.jpeg'  # Ensure this path is correct
    grid_size = 8
    image = load_image(image_path)
    tiles = split_image(image, grid_size)
    tile_positions, empty_tile = shuffle_tiles(grid_size)
    st.session_state.tiles = tiles
    st.session_state.tile_positions = tile_positions
    st.session_state.empty_tile = empty_tile
    st.session_state.moves = 0
    st.session_state.initialized = True

# Display the puzzle
puzzle_image = draw_puzzle(st.session_state.tiles, st.session_state.tile_positions, st.session_state.empty_tile, 8)
st.image(puzzle_image, caption='Solve the puzzle!', use_column_width=True)

# Input and move logic
move = st.selectbox('Move tile:', ['Up', 'Down', 'Left', 'Right'])
if st.button('Make Move'):
    empty_i, empty_j = st.session_state.empty_tile
    if move == 'Up' and empty_i < 7:
        target = (empty_i + 1, empty_j)
    elif move == 'Down' and empty_i > 0:
        target = (empty_i - 1, empty_j)
    elif move == 'Left' and empty_j < 7:
        target = (empty_i, empty_j + 1)
    elif move == 'Right' and empty_j > 0:
        target = (empty_i, empty_j - 1)
    else:
        target = None

    if target:
        target_pos = st.session_state.tile_positions.index(target)
        empty_pos = st.session_state.tile_positions.index(st.session_state.empty_tile)
        st.session_state.tile_positions[target_pos], st.session_state.tile_positions[empty_pos] = st.session_state.tile_positions[empty_pos], st.session_state.tile_positions[target_pos]
        st.session_state.empty_tile = target
        st.session_state.moves += 1

    # Update the puzzle image after the move
    puzzle_image = draw_puzzle(st.session_state.tiles, st.session_state.tile_positions, st.session_state.empty_tile, 8)
    st.image(puzzle_image, caption='Solve the puzzle!', use_column_width=True)

# Display the number of moves
st.write(f'Moves: {st.session_state.moves}')
