import streamlit as st
import random
import time

# Define themes
themes = {
    "Default": {
        "title_color": "#4CAF50",
        "header_color": "#FF5733",
        "font_family": "'Courier New', Courier, monospace",
    },
    "Dark": {
        "title_color": "#FFFFFF",
        "header_color": "#888888",
        "font_family": "'Arial', sans-serif",
    },
    "Light": {
        "title_color": "#000000",
        "header_color": "#666666",
        "font_family": "'Verdana', sans-serif",
    },
}

# Select a theme
theme = st.selectbox('Select Theme:', list(themes.keys()))
selected_theme = themes[theme]

# Custom CSS for styling
st.markdown(
    f"""
    <style>
    .title {{
        font-size: 50px;
        color: {selected_theme["title_color"]};
        text-align: center;
        font-family: {selected_theme["font_family"]};
    }}
    .header {{
        font-size: 30px;
        color: {selected_theme["header_color"]};
        text-align: center;
        font-family: {selected_theme["font_family"]};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Title of the game
st.markdown('<div class="title">Tushi\'s Guess the Number Game</div>', unsafe_allow_html=True)

# Personalized header
st.markdown('<div class="header">Welcome to the game, Samia Mollika Tushi!</div>', unsafe_allow_html=True)

# Difficulty level selector
difficulty = st.selectbox('Select Difficulty Level:', ['Easy (1-50)', 'Medium (1-100)', 'Hard (1-200)'])

# Generate a random number based on difficulty
if difficulty == 'Easy (1-50)':
    number_to_guess = random.randint(1, 50)
elif difficulty == 'Medium (1-100)':
    number_to_guess = random.randint(1, 100)
else:
    number_to_guess = random.randint(1, 200)

# Session state to keep track of the number, attempts, best score, and start time
if 'number' not in st.session_state:
    st.session_state.number = number_to_guess
    st.session_state.attempts = 0
    st.session_state.best_score = float('inf')
    st.session_state.start_time = time.time()
    st.session_state.hint_provided = False

# Input from the user
guess = st.number_input('Enter your guess:', min_value=1, max_value=200, step=1)

# Button to submit the guess
if st.button('Submit Guess'):
    st.session_state.attempts += 1
    elapsed_time = time.time() - st.session_state.start_time
    if guess < st.session_state.number:
        st.write('Try a higher number!')
    elif guess > st.session_state.number:
        st.write('Try a lower number!')
    else:
        st.balloons()  # Show balloons when guessed correctly
        attempts = st.session_state.attempts
        st.write(f'Congratulations, Samia! You guessed the number in {attempts} attempts and {elapsed_time:.2f} seconds.')
        if attempts < st.session_state.best_score:
            st.session_state.best_score = attempts
            st.write('New Best Score!')
        else:
            st.write(f'Your best score is {st.session_state.best_score} attempts.')
        # Reset the game
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.start_time = time.time()
        st.session_state.hint_provided = False

    # Provide a hint if too many attempts
    if st.session_state.attempts > 5 and not st.session_state.hint_provided:
        hint_range = st.session_state.number // 10 * 10
        st.write(f'Hint: The number is between {hint_range} and {hint_range + 10}.')
        st.session_state.hint_provided = True

# Display the best score
st.write(f'Best Score: {st.session_state.best_score} attempts')

# Reset button to start a new game
if st.button('Reset Game'):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.start_time = time.time()
    st.session_state.hint_provided = False
    st.write('Game has been reset. Start guessing!')
