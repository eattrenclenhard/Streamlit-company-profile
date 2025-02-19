import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.title('The Best Company')

st.write(
    'I must not fear. Fear is the mind killer. Fear is the little death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see it s path. Where the fear has gone there will be nothing. Only I will remain.')

st.header('Our Team')

col1, col2, col3 = st.columns(3)
df = pandas.read_csv('database/data.csv')
personnel = list(df.iterrows())

with col1:
    for i in range(0, len(personnel), 3):
        st.header(personnel[i][1]['first name'].title().strip() + ' ' + personnel[i][1]['last name'].title().strip())
        st.write(personnel[i][1]['role'])
        st.image(f'images/{personnel[i][1]['image']}')

with col2:
    for i in range(1, len(personnel), 3):
        st.header(personnel[i][1]['first name'].title().strip() + ' ' + personnel[i][1]['last name'].title().strip())
        st.write(personnel[i][1]['role'])
        st.image(f'images/{personnel[i][1]['image']}')

with col3:
    for i in range(2, len(personnel), 3):
        st.header(personnel[i][1]['first name'].title().strip() + ' ' + personnel[i][1]['last name'].title().strip())
        st.write(personnel[i][1]['role'])
        st.image(f'images/{personnel[i][1]['image']}')

# with col2:
#     for i in range(1, len(personnel), 3):
#         st.header(personnel[i][1]['first name'].title(), personnel[i][1]['last name'].title())
#         st.divider()
#
# with col3:
#     for i in range(2, len(personnel), 3):
#         st.header(personnel[i][1]['first name'].title(), personnel[i][1]['last name'].title())
#         st.divider()
