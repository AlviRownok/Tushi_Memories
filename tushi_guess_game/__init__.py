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

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

# Session state to keep track of the number and attempts
if 'number' not in st.session_state:
    st.session_state.number = number_to_guess
    st.session_state.attempts = 0

# Input from the user
guess = st.number_input('Enter your guess:', min_value=1, max_value=100, step=1)

# Button to submit the guess
if st.button('Submit Guess'):
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.write('Try a higher number!')
    elif guess > st.session_state.number:
        st.write('Try a lower number!')
    else:
        st.balloons()  # Show balloons when guessed correctly
        st.write(f'Congratulations, Samia! You guessed the number in {st.session_state.attempts} attempts.')
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0
