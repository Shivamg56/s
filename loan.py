import streamlit as st
st.title('loan calculater')
amount=st.number_input('needed amount')
year=st.text_input('enter years')
interestrate=st.write('interest rate per annum=8%')
for