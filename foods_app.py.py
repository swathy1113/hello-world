import streamlit as st 
st.title("This is my project")

st.header("This is a header")
st.subheader("This is a subheader")


st.text("This is plain text")
st.markdown("### This is a markdown text")


# Input Widgets
name = st.text_input("Enter your name")
feedback = st.text_area("Provide your feedback")



# Buttons and Checkboxes
if st.button("Submit"):
    st.success(f"Hello {name}, thanks for your feedback!")


agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("You agreed!")

choice = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {choice}")

# Selectbox and Multiselect
color = st.selectbox("Select a color", ["Red", "Green", "Blue"])
st.write(f"You chose: {color}")

hobbies = st.multiselect("Select your hobbies", ["Reading", "Coding", "Gaming"])
st.write(f"Your hobbies: {', '.join(hobbies)}")

# Sliders and Number Input
age = st.slider("Select your age", 1, 100, 25)
st.write(f"Your age is: {age}")
