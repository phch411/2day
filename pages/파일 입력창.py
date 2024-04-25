import streamlit as st
import random

st.title("여러 가지 입력창")

st.button("Reset", type="primary")
if st.button('랜덤숫자'):
    st.write(random.randint(0,10))
else:
    st.write('Goodbye')

#st.download_button예시
text_contents = '''This is some text'''
st.download_button('Download some text', text_contents)

#st.link_button예시
st.link_button("Go to gallery", "https://streamlit.io/gallery")

#st.checkbox 예시
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')
else:
    st.write("동의버튼을 눌러주세요.")

#st.multiselect 예시
options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

#st.radio 예시
genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

if genre == ':rainbow[Comedy]':
    st.write('You selected comedy.')
else:
    st.write("You didn\'t select comedy.")

#st.number_input 예시
number = st.number_input('Insert a number')
st.write('The current number is ', number)

#st.text_input 예시
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)

#st.file_uploader 예시
import pandas as pd

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    # bytes_data = uploaded_file.read()
    data = pd.read_csv(uploaded_file, encoding='euc-kr')
    st.write("filename:", uploaded_file.name)
    st.write(data)

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    # bytes_data = uploaded_file.read()
    data = pd.read_csv(uploaded_file, encoding='euc-kr')
    st.write("filename:", uploaded_file.name)
    st.write(data)