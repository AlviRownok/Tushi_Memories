import streamlit as st
from PIL import Image
import numpy as np
import random
import base64
import io

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: yellow;
        font-family: 'Press Start 2P', cursive;
    }
    .title {
        font-size: 60px;
        color: yellow;
        text-shadow: 2px 2px 5px blue;
        margin-bottom: 0;
        text-align: left;
    }
    .header {
        font-size: 30px;
        color: yellow;
        text-shadow: 1px 1px 3px red;
        margin-top: 0;
        text-align: left;
    }
    .puzzle-piece {
        width: 100px;
        height: 100px;
        border: 1px solid yellow;
        display: inline-block;
        margin: 5px;
    }
    .dropzone {
        width: 100px;
        height: 100px;
        border: 2px dashed yellow;
        display: inline-block;
        margin: 5px;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    <script>
    function allowDrop(ev) {
        ev.preventDefault();
    }
    
    function drag(ev) {
        ev.dataTransfer.setData("text", ev.target.id);
    }
    
    function drop(ev) {
        ev.preventDefault();
        var data = ev.dataTransfer.getData("text");
        ev.target.appendChild(document.getElementById(data));
    }
    </script>
    """,
    unsafe_allow_html=True
)

# Load and split the image
def load_image(image_path):
    img = Image.open(image_path)
    return img

def split_image(img, grid_size):
    w, h = img.size
    piece_w, piece_h = w // grid_size, h // grid_size
    pieces = []
    for i in range(grid_size):
        for j in range(grid_size):
            piece = img.crop((j * piece_w, i * piece_h, (j + 1) * piece_w, (i + 1) * piece_h))
            pieces.append(piece)
    return pieces

def check_puzzle(puzzle, grid_size):
    flat_puzzle = puzzle.flatten()
    for idx, val in enumerate(flat_puzzle):
        if val != idx:
            return False
    return True

# Game settings
grid_size = 3
image_path = "tushi_guess_game/Image_1.jpeg"

# Load and split image
img = load_image(image_path)
pieces = split_image(img, grid_size)

# Convert image pieces to base64 to embed in HTML
pieces_base64 = []
for piece in pieces:
    buffer = io.BytesIO()
    piece.save(buffer, format="PNG")
    pieces_base64.append(base64.b64encode(buffer.getvalue()).decode())

# Initialize puzzle state
if 'puzzle' not in st.session_state:
    st.session_state.puzzle = np.arange(grid_size * grid_size).reshape((grid_size, grid_size))
    random.shuffle(st.session_state.puzzle.flat)

st.title("Sliding Puzzle Game")
st.write("Drag and drop the pieces to solve the puzzle!")

# Display piece pile
st.write("Piece Pile")
for idx, piece in enumerate(pieces_base64):
    piece_html = f'<img id="piece-{idx}" src="data:image/png;base64,{piece}" draggable="true" ondragstart="drag(event)" class="puzzle-piece">'
    st.markdown(piece_html, unsafe_allow_html=True)

# Display puzzle board
st.write("Puzzle Board")
for i in range(grid_size):
    cols = st.columns(grid_size)
    for j in range(grid_size):
        piece_idx = st.session_state.puzzle[i, j]
        if piece_idx != 0:
            dropzone_html = f'<div id="dropzone-{i}-{j}" ondrop="drop(event)" ondragover="allowDrop(event)" class="dropzone"><img id="piece-{piece_idx}" src="data:image/png;base64,{pieces_base64[piece_idx]}" draggable="true" ondragstart="drag(event)" class="puzzle-piece"></div>'
        else:
            dropzone_html = f'<div id="dropzone-{i}-{j}" ondrop="drop(event)" ondragover="allowDrop(event)" class="dropzone"></div>'
        cols[j].markdown(dropzone_html, unsafe_allow_html=True)

# Check if solved
if check_puzzle(st.session_state.puzzle, grid_size):
    st.balloons()
    st.write("Congratulations! You've solved the puzzle!")
