import streamlit as st
st.title('My first webapp')
# You have to write a program that determine whether you will accept loan application or reject. 
# You will determine acceptence based on annual salary and year of work. Acceptance standard is annual salary >= 500,000 yuan and >= 5 year of work in current work
annual_salary = st.number_input("Enter your annual salary:")
year_work = st.number_input("Enter your year of work:")
if st.button("Submit"):
    if annual_salary >= 500000:
        if year_work >= 5:
            st.write("Your application is accepted.")
        else:
            st.write("Sorry, your year work is not qualified, so your application is rejected.")
    else:
        if year_work >=5:    
            st.write("Sorry, your anuual salary is not qualified, so your application is rejected.")