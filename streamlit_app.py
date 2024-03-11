import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express
import matplotlib.pyplot as plt


st.set_page_config(page_title='Excel Plotter')
st.title('Excel Plotter 📈')
st.subheader('Feed me with your Excel file')

uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('---')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    groupby_column = st.selectbox(
         'What would you like to analyse?',
        ('payment_type', 'payment_installments')
    )

    # -- GROUP DATAFRAME
    output_columns = ['payment_sequential', 'payment_value']
    df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_columns].sum()

    # -- PLOT DATAFRAME
    fig = px.bar(
        df_grouped,
        x=groupby_column,
        y='payment_sequential',
        color='payment_value',
        color_continuous_scale=['red', 'yellow', 'green'],
        template='plotly_white',
        title=f'<b>payment_sequential & payment_value by {groupby_column}</b>'
    )
    st.plotly_chart(fig)

