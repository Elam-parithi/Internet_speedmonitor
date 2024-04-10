
import streamlit as st
import pandas as pd

st.set_page_config()
st.title("Internet speed monitor Dashboard")
st.write("By Elamparithi")
ip_addr = "192.168.0.152"

l_column, r_column = st.columns(2)
r_column.write(f"Your IP: {ip_addr}")
r_column.write(f"Your ISP: BarathFiber")

option = l_column.selectbox('View by:', ('Date', 'Time', 'Charted', 'Custom'))
st.write('You selected:', option)



