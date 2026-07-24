#import pavkages 
import streamlit as st 
import numpy as np
import pandas as pd 

st.title("Hello , streamlit")
st.write(":streamlit: This is your first streamlit app")
st.text("Let go started")
st.write("my bhavika")

# conditional logic
name = st.text_input("Enter your name :")
if st.button("Greet"):
    st.success(f"Hello {name}")

#Displaying Data and charts
df = pd.DataFrame(np.random.randn(10,2), columns=["A","B"])
st.line_chart(df)
st.bar_chart(df)

# file uploadering and caching 
upload_file = st.file_uploader("upload file",type="cvs")
if upload_file:
       df = pd.read_csv(upload_file)
       st.dataframe(df)

# all the 
st.header("this is a header")
st.subheader(" This is a subheader")
st.markdown("**Bold**,*Italic*,[Link]()")
st.number_input("pick a number",min_value=0,max_value=100)
st.selectbox("Select a friut",["Apple","banana","Mango"])
st.multiselect("choose topping",["cheese","tomato","olives"])
st.radio("pick one",["option A","option B"])
st.checkbox("I agree terms and condition")

# form code 
with st.form("login form"):
      username = st.text_input("username")
      password = st.text_input("password",type="password")
      submitted = st.form_submit_button("Logic")

      if submitted:
            st.success(f"welcome , {username}")

#
# check radio button
option = st.radio("choose view",["Show Table"])
if option =="Show chart":
      st.write("chart would be appear heare")
else:
      st.write("Table would be apper heare")


      if st.checkbox("Show details"):
            st.info("here are more detailes")

# media layout and advance widget
st.sidebar.title("New Chart")
st.image("https://static.vecteezy.com/system/resources/thumbnails/057/068/323/small/single-fresh-red-strawberry-on-table-green-background-food-fruit-sweet-macro-juicy-plant-image-photo.jpg")
st.video("https://youtu.be/HUYwcg9OPWI?si=hOJl7Wno29gDgOCf")

