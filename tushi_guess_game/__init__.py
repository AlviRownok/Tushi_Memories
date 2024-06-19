import streamlit as st
import random

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        font-size: 50px;
        color: #4CAF50;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
    .header {
        font-size: 30px;
        color: #FF5733;
        text-align: center;
        font-family: 'Courier New', Courier, monospace;
    }
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

# Session state to keep track of the number, attempts, and best score
if 'number' not in st.session_state:
    st.session_state.number = number_to_guess
    st.session_state.attempts = 0
    st.session_state.best_score = float('inf')

# Input from the user
guess = st.number_input('Enter your guess:', min_value=1, max_value=200, step=1)

# Button to submit the guess
if st.button('Submit Guess'):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.write('Try a higher number!')
    elif guess > st.session_state.number:
        st.write('Try a lower number!')
    else:
        st.balloons()  # Show balloons when guessed correctly
        attempts = st.session_state.attempts
        st.write(f'Congratulations, Samia! You guessed the number in {attempts} attempts.')
        if attempts < st.session_state.best_score:
            st.session_state.best_score = attempts
            st.write('New Best Score!')
        else:
            st.write(f'Your best score is {st.session_state.best_score} attempts.')
        # Reset the game
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0

# Display the best score
st.write(f'Best Score: {st.session_state.best_score} attempts')

# Reset button to start a new game
if st.button('Reset Game'):
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.write('Game has been reset. Start guessing!')

