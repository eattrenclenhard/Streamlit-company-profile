import streamlit as st
from module.send_email import send_email
import pandas

df = pandas.read_csv('database/topics.csv')

with st.form(key='email_form'):
    visitor_email = st.text_input('Your email address')
    st.selectbox('What topic do you want to discuss?', df['topic'])
    raw_message = st.text_area('Your message')
    message_body = f"""\
Subject: Streamlit Company Profile Practice: New email from {visitor_email}

{raw_message}
From: {visitor_email}
"""
    button = st.form_submit_button('Submit')
    if button:
        try:
            send_email(message_body)


            @st.dialog('✅Email successfully sent!')
            def instruction_modal():
                st.write('Thank you for contacting us! We will get in touch with you soon.')


            instruction_modal()

        except:
            print('There was an error sending the email.')
