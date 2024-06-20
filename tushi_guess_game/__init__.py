import streamlit as st
from PIL import Image
import random

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
            box = (j * tile_width, i * tile_height, (j + 1) * tile_width, (i + 1) * tile_height)
            tile = image.crop(box)
            tiles.append(tile)
    return tiles, tile_width, tile_height

# Function to shuffle the tiles
def shuffle_tiles(grid_size):
    tile_positions = [(i, j) for i in range(grid_size) for j in range(grid_size)]
    random.shuffle(tile_positions)
    empty_tile = tile_positions.pop()
    return tile_positions, empty_tile

# Function to draw the current state of the puzzle
def draw_puzzle(tiles, tile_positions, empty_tile, grid_size, tile_width, tile_height):
    puzzle_image = Image.new('RGB', (400, 400))
    for index, pos in enumerate(tile_positions):
        if pos != empty_tile:
            tile = tiles[index]
            box = (pos[1] * tile_width, pos[0] * tile_height)
            puzzle_image.paste(tile, box)
    return puzzle_image

# Function to check if a move is valid and perform the move
def move_tile(tile_positions, empty_tile, click_pos, grid_size):
    empty_i, empty_j = empty_tile
    click_i, click_j = click_pos
    if (abs(empty_i - click_i) == 1 and empty_j == click_j) or (abs(empty_j - click_j) == 1 and empty_i == click_i):
        empty_index = tile_positions.index(empty_tile)
        click_index = tile_positions.index(click_pos)
        tile_positions[empty_index], tile_positions[click_index] = tile_positions[click_index], tile_positions[empty_index]
        return click_pos, tile_positions
    return empty_tile, tile_positions

# Initialize the game state
if 'initialized' not in st.session_state:
    image_path = 'tushi_guess_game/Image_1.jpeg'  # Ensure this path is correct
    grid_size = 4  # 4x4 grid
    image = load_image(image_path)
    tiles, tile_width, tile_height = split_image(image, grid_size)
    tile_positions, empty_tile = shuffle_tiles(grid_size)
    st.session_state.tiles = tiles
    st.session_state.tile_positions = tile_positions
    st.session_state.empty_tile = empty_tile
    st.session_state.moves = 0
    st.session_state.grid_size = grid_size
    st.session_state.tile_width = tile_width
    st.session_state.tile_height = tile_height
    st.session_state.initialized = True

# Draw the puzzle
puzzle_image = draw_puzzle(st.session_state.tiles, st.session_state.tile_positions, st.session_state.empty_tile, st.session_state.grid_size, st.session_state.tile_width, st.session_state.tile_height)
st.image(puzzle_image, caption='Solve the puzzle!', use_column_width=True)

# Capture click events
click_position = st.empty()

if st.button('Reset Game'):
    st.session_state.initialized = False
    st.experimental_rerun()

st.write(f'Moves: {st.session_state.moves}')

# JavaScript to capture click events
st.markdown("""
    <script>
    const puzzleImage = document.getElementsByTagName("img")[0];
    puzzleImage.onclick = function(event) {
        const rect = puzzleImage.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        const click_pos = [Math.floor(y / (rect.height / 4)), Math.floor(x / (rect.width / 4))];
        window.parent.postMessage(click_pos, "*");
    };
    </script>
    """, unsafe_allow_html=True)

# Receive the click position
st.session_state.clicked = st.experimental_get_query_params().get('click_pos')
if st.session_state.clicked:
    click_i, click_j = map(int, st.session_state.clicked[0].split(','))
    click_pos = (click_i, click_j)
    st.session_state.empty_tile, st.session_state.tile_positions = move_tile(st.session_state.tile_positions, st.session_state.empty_tile, click_pos, st.session_state.grid_size)
    st.session_state.moves += 1
    st.experimental_rerun()
