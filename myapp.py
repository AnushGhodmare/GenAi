import streamlit as st
import numpy as np
import pandas as pd

st.title("Hello Streamlit")
st.write("This is your first Streamlit app")
st.text("Let's get started")

# Conditional logic with widgets
name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello, {name}!")

# Displaying data and charts 
df = pd.DataFrame(np.random.rand(10, 2), columns=['A', 'B'])
st.line_chart(df)
st.bar_chart(df)

# Media layout and advanced widgets 
st.sidebar.title("Navigation")
st.image(
    "https://tse1.explicit.bing.net/th/id/OIP.tGq2V-jYrBmm_r0qgA910QHaFj?rs=1&pid=ImgDetMain&o=7&rm=3",
    caption="Sample Image"
)
st.video("https://youtu.be/9T-Zbxg9X_4")

# File uploading
uploaded_file = st.file_uploader("Upload a CSV", type="csv")
if uploaded_file is not None:
    df_uploaded = pd.read_csv(uploaded_file)
    st.dataframe(df_uploaded)

st.title("Text and Markdown Demo")
st.header("This is header")
st.subheader("This is subheader")

# Fixed markdown syntax
st.markdown("**Bold**, *Italic*, `code`, [Link](https://streamlit.io)")

# Fixed code block syntax
st.code("for i in range(5):\n    print(i)", language="python")

st.text_input("What is your name?")
st.text_area("Write Something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)

# Fixed selectbox list items
st.selectbox("Select a fruit", ["Apple", "Mango", "Banana"])

st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])
st.checkbox("I agree to the terms")

# Checkbox example
if st.checkbox("Show Details"):
    st.info("Here are more details")

# Radio button example
option = st.radio("Choose a view", ["Show chart", "Show table"])

if option == "Show chart":
    st.write("Chart would appear here")
else:
    st.write("Table would appear here")

# Form example
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        st.success(f"Welcome, {username}!")
