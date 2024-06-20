import streamlit as st
import random
import time

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
        font-size: 40px; /* Adjusted for better mobile compatibility */
        color: yellow;
        text-shadow: 2px 2px 5px blue;
        margin-bottom: 0;
        text-align: left;
    }
    .header {
        font-size: 20px; /* Adjusted for better mobile compatibility */
        color: yellow;
        text-shadow: 1px 1px 3px red;
        margin-top: 0;
        text-align: left;
    }
    .stSelectbox > div {
        background-color: blue;
        color: yellow;
        border-radius: 10px;
        border: 2px solid yellow;
        font-family: 'Press Start 2P', cursive;
        font-size: 14px; /* Adjusted for better mobile compatibility */
        padding: 10px;
        text-align: center;
    }
    .stButton button {
        background-color: blue;
        color: yellow;
        border-radius: 10px;
        border: 2px solid yellow;
        font-family: 'Press Start 2P', cursive;
        font-size: 14px; /* Adjusted for better mobile compatibility */
        padding: 10px;
    }
    .stNumberInput input {
        background-color: blue;
        color: yellow;
        border-radius: 10px;
        border: 2px solid yellow;
        font-family: 'Press Start 2P', cursive;
        font-size: 14px; /* Adjusted for better mobile compatibility */
        padding: 5px;
        text-align: center;
    }
    .hint {
        font-size: 16px; /* Adjusted for better mobile compatibility */
        color: red;
        text-align: center;
        font-family: 'Press Start 2P', cursive;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
    """,
    unsafe_allow_html=True
)

# Layout
col1, col2 = st.columns([2, 3])

with col1:
    # Title of the game
    st.markdown('<div class="title">Tushi\'s Guess the Number Game</div>', unsafe_allow_html=True)

    # Personalized header
    st.markdown('<div class="header">Welcome, Samia Mollika Tushi!</div>', unsafe_allow_html=True)

with col2:
    # Difficulty level selector with fun visual
    difficulty = st.selectbox('Select Difficulty Level:', ['Easy (1-50)', 'Medium (1-100)', 'Hard (1-200)'], index=1, format_func=lambda x: f"🎮 {x}")

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
            st.markdown('<div class="title">🍒🍓🍍 Congratulations, Samia! 🍉🍇🍑</div>', unsafe_allow_html=True)
            attempts = st.session_state.attempts
            st.write(f'You guessed the number in {attempts} attempts and {elapsed_time:.2f} seconds.')
            if attempts < st.session_state.best_score:
                st.session_state.best_score = attempts
                st.write('New Best Score!')
            else:
                st.write(f'Your best score is {st.session_state.best_score} attempts.')
            # Reset the game
            if difficulty == 'Easy (1-50)':
                st.session_state.number = random.randint(1, 50)
            elif difficulty == 'Medium (1-100)':
                st.session_state.number = random.randint(1, 100)
            else:
                st.session_state.number = random.randint(1, 200)
            st.session_state.attempts = 0
            st.session_state.start_time = time.time()
            st.session_state.hint_provided = False

        # Provide a hint if too many attempts
        if st.session_state.attempts > 5 and not st.session_state.hint_provided:
            hint_range = st.session_state.number // 10 * 10
            st.markdown(f'<div class="hint">Hint: The number is between {hint_range} and {hint_range + 10}.</div>', unsafe_allow_html=True)
            st.session_state.hint_provided = True

    # Display the best score
    st.write(f'Best Score: {st.session_state.best_score} attempts')

    # Reset button to start a new game
    if st.button('Reset Game'):
        if difficulty == 'Easy (1-50)':
            st.session_state.number = random.randint(1, 50)
        elif difficulty == 'Medium (1-100)':
            st.session_state.number = random.randint(1, 100)
        else:
            st.session_state.number = random.randint(1, 200)
        st.session_state.attempts = 0
        st.session_state.start_time = time.time()
        st.session_state.hint_provided = False
        st.write('Game has been reset. Start guessing!')
