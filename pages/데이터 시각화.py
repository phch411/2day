import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

CSV_file = st.file_uploader(label="펭귄데이터를 업로드해주세요. 단, CSV 파일만 가능합니다.")

if CSV_file is not None:

    CSV_file_df = pd.read_csv(CSV_file, encoding='euc-kr')
    st.write(CSV_file_df.head(5))


st.bar_chart(CSV_file_df["종"].value_counts())

fig, ax = plt.subplots()
sns.histplot(CSV_file_df.culmen_length_mm, binrange=[30, 60], binwidth=2.5)
st.pyplot(fig)

#어떤 파일이든 넣어서 시각화하는 방법
CSV_file = st.file_uploader(label="데이터를 업로드해주세요. 단, CSV 파일만 가능합니다.")

if CSV_file is not None:

    CSV_file_df = pd.read_csv(CSV_file, encoding='euc-kr')
    st.write(CSV_file_df.head(5))

column = st.radio(label="열 이름을 선택해주세요.", options = CSV_file_df.columns())
st.subheader(column, "의 분포를 그려보겠습니다.")
st.bar_chart(CSV_file_df[column].value_counts())

fig, ax = plt.subplots()
sns.histplot(CSV_file_df[column], binrange=[2500, 7000], binwidth=100)
st.pyplot(fig)