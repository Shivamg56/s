import streamlit as st
from altair import selection, sequence
from select import select
from streamlit import selectbox

st.title('Loan Calculater1 App')
st.write('Welcome Guest :')
x=st.selectbox('Do you want Loan:',options=['Yes','NO'])
if x=='Yes':
    Amount=st.number_input('How Much Amount Do you want? :')
    Time_Period=st.number_input('Time period(Years) :')
    Interest_Rate=st.number_input('Annual Interest Rate :')
    Interest=0
    Total_Amount=0
    if Interest>=0:
        Interest=(Amount*Time_Period*Interest_Rate)/100
        st.write('Total Interest To Be Paid In Selected Time Period Is:',Interest)
    if Total_Amount>=0:
        Total_Amount=Amount+Interest
        st.write('Total Amount To Be Paid In Selected Time Period Is:',Total_Amount)
        st.write('Thank you for using Loan Calculater App')
else:
    st.write('Thank You for Your Visit.')