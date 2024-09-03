import streamlit as st
from streamlit import selectbox

st.title('Loan Calculater')
st.write('Welcome Guest :')
x=st.selectbox('Do you want Loan:',options=['N/A','Yes','NO'])
if x=='Yes':
    Amount=selectbox('How Much Amount Do you want? :',options=['0','1000','5000','10000','50000','100000','500000','1000000','1500000','2000000'])
    Time_Period=selectbox('Time Period(in years) :',options=['0','1','2','3','4','5','6','7','8','9','10'])
    Interest_Rate=selectbox('Annual Interest Rate(in %) :',options=['5','8','11','13','15','19'])
    Interest=0
    Total_Amount=0
    A=int(Amount)
    T=int(Time_Period)
    I=int(Interest_Rate)
    if Interest>=0:
        Interest=(A*T*I)/100
        st.write('Total Interest To Be Paid In Selected Time Period Is:',Interest)
    if Total_Amount>=0:
        Total_Amount=A+Interest
        st.write('Total Amount To Be Paid In Selected Time Period Is:',Total_Amount)
    if Interest>0:
        st.write('Thank you for using Loan Calculater App')
elif x=='N/A':
    st.write('')
else:
    st.write('Thank You for Your Visit.')
