# import ollama

# res = ollama.chat(
#     model = 'llava:13b',
#     messages = [
#         {
#             'role': 'user',
#             'content': 'Describe the image',
#             'images': ['images\image1.jpg']
#         }
#     ]
# )

# print(res['message']['content'])

# --------------------------- GUI ------------------------------ #

import streamlit as st
import ollama
import os

def process_image_and_content(image_path, prompt):
    res = ollama.chat(
        model='llava:13b',
        messages=[
            {
                'role': 'user',
                'content': prompt,
                'images': [image_path]
            }
        ]
    )
    return res['message']['content']

st.title('Image Chat')

image = st.file_uploader('Upload an image', type=['jpg', 'jpeg', 'png'])

prompt = st.text_input('Enter prompt')

if st.button('Process') and image and prompt:
    temp_dir = 'temp'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    
    image_path = os.path.join(temp_dir, image.name)
    with open(image_path, 'wb') as f:
        f.write(image.getbuffer())

    result = process_image_and_content(image_path, prompt)

    st.write(result)