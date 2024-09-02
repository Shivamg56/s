import streamlit as st
st.title('loan calculater')
Amount=st.number_input('How Much Amount Do you want?')
Time_Period=st.number_input('Time period(Years)')
Intrest_Rate=st.number_input('Annual Intrest Rate')
Intrest=0
Total_Amount=0
if Intrest>=0:
    Intrest=(Amount*Time_Period*Intrest_Rate)/100
st.write('Total Intrest To Be Paid In Selected Time Period Is:',Intrest)
if Total_Amount>=0:
    Total_Amount=Amount+Intrest
st.write('Total Amount To Be Paid In Selected Time Period Is:',Total_Amount)