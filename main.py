import streamlit as st
import time
import csv

hours = int(time.strftime('%H'))
saved_data = []
# Section 1: Title
st.title('Affective Foretell')
st.subheader('What is your name?')
name = st.selectbox(
    'Select your nickname.',
    ('--', 'Alex', 'Ben', 'Chris', 'Don', 'Eddie', 'Fem', 'Greta',
     'Hans', 'Iris', 'Jon'))
if name != '--':
    st.write('Hello', name,'!')

# Section 2: Mood
st.subheader('How are you feeling right now?')
mood_NH_PL = st.select_slider(' ',
    ['Very tense', 'Tense', 'Somewhat tense', 'Neutral', 'Somewhat calm', 'Calm', 'Very calm'],
    value='Very tense')

mood_PM_NM = st.select_slider(' ',
    ['Very discontent', 'Discontent', 'Somewhat discontent', 'Neutral', 'Somewhat content', 'Content', 'Very content'],
    value='Very discontent')

mood_PH_NL = st.select_slider(' ',
    ['Very bored', 'Bored', 'Somewhat bored', 'Neutral', 'Somewhat excited', 'Excited', 'Very excited'],
    value='Very bored')

moods = [mood_NH_PL, mood_PM_NM, mood_PH_NL]
# Section 3: Activities
if hours in range(6, 12):
    st.subheader('How many hours did you sleep last night?')
    sleep_time = st.slider(
        label='',
        min_value=0.0,
        max_value=16.0,
        step=0.5,
        format='%1f'
    )
    food_options = 'food_options'
    activity_options = 'activity_options'
elif hours in range(12, 17):
    st.subheader('What was your last meal?')
    food_options = st.multiselect(
        'You can select multiple options.',
        ['🥩', '🍔', '🍕', '🌭', '🍝', '🍚', '🍞', '🥛',
         '🥔', '🧀', '🍎', '🍌', '🥗', '🥒', '🍰', '🍪' ])
    sleep_time = 'sleep_time'
    activity_options = 'activity_options'
else:
    st.subheader('What were your activities today?')
    activity_options = st.multiselect(
        'You can select multiple options.',
        ['⚽️', '🧘️', '🎹', '🚗', '📱', '🛏', '🛍', '📚', '💻',
         '🍽', '🍻'])
    sleep_time = 'sleep_time'
    food_options = 'food_options'

user_input = [time.ctime(), moods, sleep_time, food_options, activity_options]

if st.button('Submit'):
    '''with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(user_input)'''
    if name == '--':
        st.write('Please select your nickname.')
    else:
        st.write('Thank you for your submission!')
        st.balloons()
        saved_data.append(user_input)
        st write(saved_data)
