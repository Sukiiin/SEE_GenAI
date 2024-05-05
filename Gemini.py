import streamlit as st

# Title and description
st.title("Meet Your AI Assistant - Get Answers & Insights Instantly")
st.write("Your one-stop shop for information and image analysis. Ask anything or upload an image, and I'll be your helpful guide.")

# Feature section with columns
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Ask Me Anything")
    st.write("Got a burning question?  Curious about a fact?  I can access and process information from a vast knowledge base to answer your inquiries in a comprehensive and informative way.")

with col2:
    st.header("Image Analysis Power")
    st.write("Upload an image and unlock hidden details. I can identify objects, describe scenes, and even answer questions based on the visual content, giving you a deeper understanding of your pictures.")

with col3:
    st.header("Boost Your Productivity")
    st.write("Free yourself from time-consuming tasks. I can research topics, provide summaries of complex information, and generate different creative text formats, streamlining your workflow and saving you valuable time.")

# Display additional information (optional)
st.write("---")
st.subheader("What Makes Me Unique?")
st.write("* Constantly Learning: I am continuously updated with the latest information, ensuring my responses are accurate and relevant.")
st.write("* User-Friendly Interface:  Interact with me seamlessly through a simple and intuitive interface.")
st.write("* Secure and Private: Your data remains confidential. I prioritize user privacy and security.")
st.write("---")


