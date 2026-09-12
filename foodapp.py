import streamlit as st
from google import genai
from PIL import Image
import io

# Initialize the GenAI client
# Make sure GEMINI_API_KEY is set in your environment
client = genai.Client(api_key="AQ.Ab8RN6IVV4T-C1_IvXCX0dht2pE2_NlNcDFFTznqe6byBw6__A")

st.title("AI Food Calorie Counter")

# Capture photo using the phone's camera
camera_image = st.camera_input("Take a picture of your food")

if camera_image is not None:
    # Convert the captured image to a PIL Image
    img = Image.open(camera_image)

    # Display the captured image
    st.image(img, caption="Your Food", use_container_width=True)

    if st.button("Analyze Calories"):
        with st.spinner("Analyzing food..."):
            try:
                # Create a chat session
                chat = client.chats.create(model="gemini-3.6-flash")

                # Send the image and prompt
                response = chat.send_message(
                    message=[
                        img,
                        "Describe this food and give its estimated calories and nutritional information."
                    ]
                )

                st.subheader("Nutritional Analysis:")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
