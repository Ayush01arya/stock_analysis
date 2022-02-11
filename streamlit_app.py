import streamlit as st
import pandas as pd
import yfinance as yf
import datetime
from datetime import date, timedelta
from PIL import Image
img =Image.open('ayushlogo.png')
st.set_page_config(page_title='STOCK APPLICATION By Kabir Arya',page_icon=img)
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown('<center><h1 class="font">STOCK PREDICTION APPLICATION</center></h1>',unsafe_allow_html=True)
stock=st.text_input('Enter the Stock Name ....?')
if st.button('CHECK'):
    import time

    with st.spinner('Loading......'):

        time.sleep(5)


    today = date.today()

    d1 = today.strftime("%Y-%m-%d")
    end_date = d1
    d2 = date.today() - timedelta(days=730)
    d2 = d2.strftime("%Y-%m-%d")
    start_date = d2

    data = yf.download(stock,
                       start=start_date,
                       end=end_date,
                       progress=False)
    data["Date"] = data.index
    data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
    data.reset_index(drop=True, inplace=True)
    print(data.head())
    import plotly.graph_objects as go

    figure = go.Figure(data=[go.Candlestick(x=data["Date"],
                                            open=data["Open"],
                                            high=data["High"],
                                            low=data["Low"],
                                            close=data["Close"])])
    figure.update_layout(title=f"Stock Analysis of {stock}",
                         xaxis_rangeslider_visible=False)
    #figure.show()
    st.plotly_chart(figure,use_container_width=True)
    st.markdown('<center><h1 class="font">@kabir_arya001</center></h1>',unsafe_allow_html=True)