import streamlit as st
from PIL import Image
import os
import google.generativeai as genai

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Configure Generative AI
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Function to generate response for the given question
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

def main():
    st.title("Brand Detection App")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    submit = st.button("Analyze")
    
    if submit and uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
        question = st.text_input("Ask: What brands?")
        ask_question = st.button("Ask")
      
        if ask_question and question:
            response = get_gemini_response(question)
            st.subheader("The Response is")
            st.write(response)

if __name__ == "__main__":
    main()
