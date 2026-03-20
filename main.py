import io
import base64
import streamlit as st
import os
import fitz  # PyMuPDF for PDF processing
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the Google Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Custom CSS for enhancing the layout
def add_custom_css():
    st.markdown(
        """
        <style>
        /* Page background and content styling */
        body {
            background-color: #9c38bf;
        }

        /* Subheaders */
        .stApp .stMarkdown h2 {
            color: #9c38bf;
            font-weight: bold;
            margin-top: 20px;
        }

        /* Buttons */
        .stButton>button {
            background-color: #9c38bf;
            color: white;
            padding: 10px 20px;
            margin: 10px 0;
            border-radius: 5px;
            border: none;
            font-size: 16px;
            cursor: pointer;
        }

        .stButton>button:hover {
            background-color: #7b1a98;
        }

        /* Text input area */
        .stTextArea textarea {
            border-radius: 10px;
            padding: 10px;
            border: 2px solid #7b1a98;
        }

        /* Uploaded file text */
        .stFileUploader {
            margin-bottom: 20px;
        }

        /* Space between elements */
        .stApp .element-container {
            margin-bottom: 20px;
        }

        /* Footer */
        footer {
            text-align: center;
            padding: 20px;
            font-size: 14px;
            color: #888;
            margin-top: 40px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# Function to get the Gemini API response
def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, pdf_content[0], prompt])
    return response.text


# Convert the PDF into image using PyMuPDF (fitz)
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_data = uploaded_file.read()
        pdf_document = fitz.open(stream=pdf_data, filetype="pdf")

        # Get the first page
        first_page = pdf_document.load_page(0)

        # Convert to a pixmap (image)
        pix = first_page.get_pixmap()

        # Convert to a PIL image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Save the image to bytes
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='JPEG')
        img_byte_arr = img_byte_arr.getvalue()

        # Convert image to base64
        pdf_parts = [
            {
                "mime_type": "image/jpeg",
                "data": base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("No file uploaded")


# Streamlit app setup
st.set_page_config(page_title="Resume Analyzer")
add_custom_css()  # Add custom CSS styles

# Header section
st.header("ATS Tracking System - Analyze Your Resume with Expert AI")

# Input fields
st.markdown("<h2>Job Description</h2>", unsafe_allow_html=True)
input_text = st.text_area("Paste the job description here:", key="input")

st.markdown("<h2>Upload Resume (PDF)</h2>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Your Resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

# Define the prompts for the buttons
input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description. 
Please share your professional evaluation on whether the candidate's profile aligns with the role. 
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a career development expert. Your task is to analyze the provided resume and job description, then suggest specific skills 
the candidate should improve or acquire to better match the job description. Focus on the technical and soft skills required for the role.
List missing skills and provide advice on how the candidate can improve in those areas.
"""

input_prompt3 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
the job description. First, the output should come as a percentage and then list the missing keywords, followed by final thoughts.
"""

# Buttons for user interactions
submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improve my Skills")
submit3 = st.button("Percentage Match")

# Logic for "Tell Me About the Resume"
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Logic for "How Can I Improve my Skills"
elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("Skill Improvement Suggestions")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Logic for "Percentage Match"
elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

# Footer
st.markdown("<footer>Powered by Google Gemini AI and Streamlit Created By- Abhinandan Patil</footer>", unsafe_allow_html=True)



# import io
# import base64
# from dotenv import load_dotenv
# import streamlit as st
# import os
# from PIL import Image
# import pdf2image
# import google.generativeai as genai
#
# # Load environment variables
# load_dotenv()
#
# # Configure the Google Gemini API
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#
#
# # Custom CSS for enhancing the layout
# def add_custom_css():
#     st.markdown(
#         """
#         <style>
#         /* Page background and content styling */
#         body {
#             background-color: #9c38bf;
#         }
#
#
#         /* Subheaders */
#         .stApp .stMarkdown h2 {
#             color: #9c38bf;
#             font-weight: bold;
#             margin-top: 20px;
#         }
#
#         /* Buttons */
#         .stButton>button {
#             background-color: #9c38bf;
#             color: white;
#             padding: 10px 20px;
#             margin: 10px 0;
#             border-radius: 5px;
#             border: none;
#             font-size: 16px;
#             cursor: pointer;
#         }
#
#         .stButton>button:hover {
#             background-color: #7b1a98;
#         }
#
#         /* Text input area */
#         .stTextArea textarea {
#             border-radius: 10px;
#             padding: 10px;
#             border: 2px solid #7b1a98;
#         }
#
#         /* Uploaded file text */
#         .stFileUploader {
#             margin-bottom: 20px;
#         }
#
#         /* Space between elements */
#         .stApp .element-container {
#             margin-bottom: 20px;
#         }
#
#         /* Footer */
#         footer {
#             text-align: center;
#             padding: 20px;
#             font-size: 14px;
#             color: #888;
#             margin-top: 40px;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
#
#
# # Function to get the Gemini API response
# def get_gemini_response(input, pdf_content, prompt):
#     model = genai.GenerativeModel('gemini-1.5-flash')
#     response = model.generate_content([input, pdf_content[0], prompt])
#     return response.text
#
#
# # Convert the PDF into image for processing
# def input_pdf_setup(uploaded_file):
#     if uploaded_file is not None:
#         images = pdf2image.convert_from_bytes(uploaded_file.read())
#         first_page = images[0]
#
#         # Convert to bytes
#         img_byte_arr = io.BytesIO()
#         first_page.save(img_byte_arr, format='JPEG')
#         img_byte_arr = img_byte_arr.getvalue()
#
#         pdf_parts = [
#             {
#                 "mime_type": "image/jpeg",
#                 "data": base64.b64encode(img_byte_arr).decode()  # encode to base64
#             }
#         ]
#         return pdf_parts
#     else:
#         raise FileNotFoundError("No file uploaded")
#
#
#
#
# # Streamlit app setup
# st.set_page_config(page_title="Resume Analyzer")
# add_custom_css()  # Add custom CSS styles
#
# # Header section
# st.header("ATS Tracking System - Analyze Your Resume with Expert AI")
#
# # Input fields
# st.markdown("<h2>Job Description</h2>", unsafe_allow_html=True)
# input_text = st.text_area("Paste the job description here:", key="input")
#
# st.markdown("<h2>Upload Resume (PDF)</h2>", unsafe_allow_html=True)
# uploaded_file = st.file_uploader("Upload Your Resume (PDF)...", type=["pdf"])
#
# if uploaded_file is not None:
#     st.write("PDF Uploaded Successfully")
#
# # Define the prompts for the buttons
# input_prompt1 = """
# You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.
# Please share your professional evaluation on whether the candidate's profile aligns with the role.
# Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
# """
#
# input_prompt2 = """
# You are a career development expert. Your task is to analyze the provided resume and job description, then suggest specific skills
# the candidate should improve or acquire to better match the job description. Focus on the technical and soft skills required for the role.
# List missing skills and provide advice on how the candidate can improve in those areas.
# """
#
# input_prompt3 = """
# You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality.
# Your task is to evaluate the resume against the provided job description. Give me the percentage of match if the resume matches
# the job description. First, the output should come as a percentage and then list the missing keywords, followed by final thoughts.
# """
#
# # Buttons for user interactions
# submit1 = st.button("Tell Me About the Resume")
# submit2 = st.button("How Can I Improve my Skills")
# submit3 = st.button("Percentage Match")
#
# # Logic for "Tell Me About the Resume"
# if submit1:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt1, pdf_content, input_text)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.write("Please upload the resume")
#
# # Logic for "How Can I Improve my Skills"
# elif submit2:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt2, pdf_content, input_text)
#         st.subheader("Skill Improvement Suggestions")
#         st.write(response)
#     else:
#         st.write("Please upload the resume")
#
# # Logic for "Percentage Match"
# elif submit3:
#     if uploaded_file is not None:
#         pdf_content = input_pdf_setup(uploaded_file)
#         response = get_gemini_response(input_prompt3, pdf_content, input_text)
#         st.subheader("The Response is")
#         st.write(response)
#     else:
#         st.write("Please upload the resume")
#
# # Footer
# st.markdown("<footer>Powered by Google Gemini AI and Streamlit Created By- Abhinandan Patil</footer>", unsafe_allow_html=True)

