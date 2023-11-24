import streamlit as st
import cv2
import numpy as np
import pickle
from tensorflow.keras.models import load_model
from preprocess import preprocess_image
from streamlit_drawable_canvas import st_canvas

# Set the page title and favicon
st.set_page_config(page_title="BN-HW-DSNd",
                   page_icon="figures/plot_words.png", layout="wide", initial_sidebar_state="expanded")
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# open css file
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load the trained CNN model
model = load_model("CNN_model.h5", compile=False)
lb = pickle.load(open("label_binarizer.pkl", "rb"))

# Streamlit app


def main():
    st.markdown(
        """
    <style>
        section[data-testid="stSidebar"] {
            width: 245px !important; # Set the width to your desired value
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    # Top bar with blue background and white text
    st.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #4CAF50;">
      <a class="navbar-brand text-center" style="color: white;    margin: auto;">Welcome to Our Detection System using Streamlit</a>
    </nav>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;top:2px;padding:7px;width:244px;">
         <a class="navbar-brand" style="color: white;text-align: center;margin:auto;">BN-HW-DSNd</a>
    </nav>
    """, unsafe_allow_html=True)

    # Introduction and instructions
    st.write("<h3 style='text-align: center;'>Welcome to our Handwritten Bangla District Name Detection using DL Techniques !</h3>",
        unsafe_allow_html=True)

    st.write("With this system, you can easily predict the district name from hand-written Bengali (Bangladeshi) text images. It utilizes a powerful Deep Learning model that has been trained on a diverse dataset of hand-written district names to provide accurate predictions.")

    # How to Use the System
    st.markdown("### How to Use the System:")
    st.markdown(
        "- Upload an image of a hand-written Bengali district name. Or, draw a Bengali district name on the whiteboard.")
    st.markdown(
        "- To adjust the drawing stroke width, you can find an option on the left sidebar.")
    st.markdown(
        "- Click the \"Predict\" button to get the district name prediction.")
    st.write("To help you understand the system better, we have provided some example images on the left.You can easily interact with the system by dragging and dropping these example images or by uploading your own hand-written district name image.")

    # drawing stroke width
    stroke_width = st.sidebar.slider("Stroke Width:", 1, 20, 2)

    # Add example images in the sidebar
    st.sidebar.markdown(
        "<p style='color: red;'>Example Images:</p>", unsafe_allow_html=True)
    example_image_paths = [
        "figures/word_62_AH_19.jpg",
        "figures/word_6_AC_01.jpg",
        "figures/word_13_AB_01.jpg",
        "figures/word_28_AH_18.jpg"
    ]
    for i, image_path in enumerate(example_image_paths):
        image = cv2.imread(image_path)
        st.sidebar.image(
            image, caption=f"Example {i+1}", use_column_width=False, width=150)

    # input field
    col1, col2 = st.columns(2)
    # input field
    col1, col2 = st.columns(2)
    # From for predict draw word
    with col1:
        with st.form('Form1', clear_on_submit=False):
            # Free drawing board
            st.markdown(
                "<h3 style='color: #3366cc;'>Draw District Name:</h3>", unsafe_allow_html=True)
            # st.title("Canvas")
            drawing = st_canvas(
                fill_color="rgba(255, 255, 255, 1)",
                stroke_width=stroke_width,
                stroke_color="black",
                background_color="white",
                height=100,
                width=300,
                key="full_app",
            )
            submitted2 = st.form_submit_button('Predict')

            if submitted2 and drawing is not None:
                image = np.array(drawing.image_data)
                preprocessed_image = preprocess_image(image)
                # Make predictions using the loaded model
                prediction = model.predict(preprocessed_image)
                predicted_label = lb.inverse_transform(prediction)[0]
                confidence = prediction.max()
                if confidence > 0.9:
                    col1_1, col1_2 = st.columns(2)
                    # Display the input image
                    col1_1.markdown(
                        "<p style='color: #3366cc;'>Input Image:</p>", unsafe_allow_html=True)
                    col1_1.image(image, caption="",
                                 use_column_width=True)
                    # The model predicts
                    col1_2.markdown(
                        f"<p style='color: green;'>Predicted District:</p>", unsafe_allow_html=True)
                    col1_2.markdown(
                        f"<span style='color: red;font-size: 3rem;'>{predicted_label}</span>", unsafe_allow_html=True)
                    # Max probability
                    # st.markdown(f"<p>Confidence Level: {confidence:.2f}</p>", unsafe_allow_html=True)
                else:
                    st.warning('Please Input Appropriate Word', icon="⚠️")

    # From for predict input image
    with col2:
        with st.form('Form2', clear_on_submit=False):
            # Image Input field
            st.markdown(
                "<h3 style='color: #3366cc;'><center>Upload an Image:</center></h3>", unsafe_allow_html=True)
            file = st.file_uploader("", type=[
                                    "jpg", "jpeg", "png", "gif", "bmp"], key="fileUploader", help="Accepted formats: JPG, JPEG, PNG, GIF")
            submitted1 = st.form_submit_button('Predict')
            if submitted1:
                if file is not None:
                    # If the user uploaded an image, read and preprocess it
                    image = cv2.imdecode(np.fromstring(
                        file.read(), np.uint8), cv2.IMREAD_COLOR)
                    preprocessed_image = preprocess_image(image)
                    # Make predictions using the loaded model
                    prediction = model.predict(preprocessed_image)
                    predicted_label = lb.inverse_transform(prediction)[0]
                    confidence = prediction.max()
                    if confidence > 0.9:
                        col2_1, col2_2 = st.columns(2)
                        # Display the results
                        col2_1.markdown(
                            "<p style='color: #3366cc;'>Inout Image:</p>", unsafe_allow_html=True)
                        col2_1.image(image, caption="",
                                     use_column_width=True)
                        # The model predicts the character as:
                        col2_2.markdown(
                            f"<p style='color: green;'>Predicted District:</p>", unsafe_allow_html=True)
                        col2_2.markdown(
                            f"<span style='color: red;font-size: 3rem;'>{predicted_label}</span>", unsafe_allow_html=True)
                    else:
                        st.warning('Please Input Appropriate Image', icon="⚠️")
                else:
                    st.warning('Please Input an Image', icon="⚠️")

    st.write("We hope you enjoy using our Hand-Written Bengali District Name Recognition System! Feel free to explore the example images, test the model with your own inputs, and experience the efficiency of our Deep Learning model.")
    st.write("Please note that this system is intended for educational and demonstration purposes. If you have any questions or feedback, don't hesitate to reach out to us. Happy predicting!")

    # Copyright text in bottom middle
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #3366cc;
            color: white;
            text-align: center;
            padding: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<div class='footer'>© 2023 Zisad . All rights reserved.</div>",
                unsafe_allow_html=True)


if __name__ == "__main__":
    main()
