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
    return tile_positions

# Function to draw the current state of the puzzle
def draw_puzzle(tiles, tile_positions, grid_size, tile_width, tile_height):
    puzzle_image = Image.new('RGB', (400, 400))
    for index, pos in enumerate(tile_positions):
        tile = tiles[index]
        box = (pos[1] * tile_width, pos[0] * tile_height)
        puzzle_image.paste(tile, box)
    return puzzle_image

# Function to check if the puzzle is solved
def is_solved(tile_positions):
    for i in range(len(tile_positions)):
        if tile_positions[i] != divmod(i, 4):
            return False
    return True

# Initialize the game state
if 'initialized' not in st.session_state:
    image_path = 'tushi_guess_game/Image_1.jpeg'  # Ensure this path is correct
    grid_size = 4  # 4x4 grid
    image = load_image(image_path)
    tiles, tile_width, tile_height = split_image(image, grid_size)
    tile_positions = shuffle_tiles(grid_size)
    st.session_state.tiles = tiles
    st.session_state.tile_positions = tile_positions
    st.session_state.grid_size = grid_size
    st.session_state.tile_width = tile_width
    st.session_state.tile_height = tile_height
    st.session_state.selected_tile = None
    st.session_state.initialized = True

# Draw the puzzle
puzzle_image = draw_puzzle(
    st.session_state.tiles,
    st.session_state.tile_positions,
    st.session_state.grid_size,
    st.session_state.tile_width,
    st.session_state.tile_height
)
st.image(puzzle_image, caption='Solve the puzzle!', use_column_width=True)

# Capture click events
clicked_tile = st.text_input("Click position:", "")

if clicked_tile:
    click_i, click_j = map(int, clicked_tile.split(","))
    click_pos = (click_i, click_j)
    if st.session_state.selected_tile:
        # Swap tiles
        selected_index = st.session_state.tile_positions.index(st.session_state.selected_tile)
        click_index = st.session_state.tile_positions.index(click_pos)
        st.session_state.tile_positions[selected_index], st.session_state.tile_positions[click_index] = \
            st.session_state.tile_positions[click_index], st.session_state.tile_positions[selected_index]
        st.session_state.selected_tile = None
    else:
        st.session_state.selected_tile = click_pos

    # Check if the puzzle is solved
    if is_solved(st.session_state.tile_positions):
        st.success("Congratulations! You solved the puzzle!")

# JavaScript to capture click events
st.markdown("""
    <script>
    const puzzleImage = document.getElementsByTagName("img")[0];
    puzzleImage.onclick = function(event) {
        const rect = puzzleImage.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        const click_pos = [Math.floor(y / (rect.height / 4)), Math.floor(x / (rect.width / 4))];
        const click_pos_str = click_pos.join(",");
        const input = document.getElementsByTagName("input")[0];
        input.value = click_pos_str;
        input.dispatchEvent(new Event('change'));
    };
    </script>
    """, unsafe_allow_html=True)

# Reset game button
if st.button('Reset Game'):
    st.session_state.initialized = False
    st.experimental_rerun()
