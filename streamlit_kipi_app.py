import streamlit as st

st.title('Welcome')


col1, col2, col3, col4 = st.columns([1, 1, 1,1])

with col1:
  col1.write('Tagged tables')

with col2:
  col2.write('Tables with a row access policy')

with col3:
  col3.write('Tagged columns')

with col4:
  col4.write('Columns with a masking policy')
