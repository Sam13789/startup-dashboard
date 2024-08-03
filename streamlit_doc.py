import streamlit as st
import pandas as pd
import time

st.title('Startup Dashboard')
st.header("I'm learning streamlit")
st.subheader("And I'm loving it !")
st.write('This is a normal text')
st.markdown('''
### My favourite Movies:
- Moana
- 3 Idiots
- K.G.F
''')
st.code('''
def foo(x):
    return x**2
x = 2
print(foo(x))
''')
st.latex('x^2 + y^2 = 1')

df = pd.DataFrame({
    'Name': ['Sam', 'Nonu', 'Monu'],
    'Marks': ['90', '80', '30'],
    'Package': ['80', '60', '40']
})
st.dataframe(df)
st.metric('Revenue', 'Rs 3L', '3%')
st.json({
    'Name': ['Sam', 'Nonu', 'Monu'],
    'Marks': ['90', '80', '30'],
    'Package': ['80', '60', '40']
})
st.sidebar.title('Sidebar ka title')
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader('first sub header')

with col2:
    st.subheader('sec sub header')

with col3:
    st.subheader('third sub header')

st.error('login Failed')
st.success('Login successful')
st.info('information')
st.warning('warning message')

bar = st.progress(0)

for i in range(1,101):
    time.sleep(0.1)
    bar.progress(i)

email = st.text_input("Enter Email")
age = st.number_input('Enter Age')
date = st.date_input('Enter Date')

password = st.text_input('Enter Password')
gender = st.selectbox('Gender', ['Male', 'Female', 'Other'])
file = st.file_uploader('Upload a csv file')

btn = st.button('Login')

if btn:
    if email == 'simarjeet1378@gmail.com' and password == '1234':
        st.balloons()
        st.success('login success')
    else:
        st.error('login failed')

if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df.describe())
