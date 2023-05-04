# -*- coding:utf-8 -*-

# import pandas as pd
import streamlit as st
# from pathlib import Path
# from utils import date_select
# from eda import show_data

submenu = st.sidebar.selectbox("Submenu", ['데이터', '전처리'])
datachoice=st.sidebar.selectbox("데이터",['Train', 'Stores', 'Oil', 'Transactions', 'Holidays_events' ])
