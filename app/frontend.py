import streamlit as st
import requests

# Initialize Session State
if "uploaded_filename" not in st.session_state:
    st.session_state["uploaded_filename"] = ""

if "extracted_filename" not in st.session_state:
    st.session_state["extracted_filename"] = ''

if "embedding_file" not in st.session_state:
    st.session_state["embedding_file"] = ''

st.title("PDF Uploader Portal")
st.header("Step 1 : Upload PDF")
st.write("Upload your PDF below to send it to the FastAPI backend.")

# File uploader widget restricting input to PDFs
uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    st.info(f"File selected: {uploaded_file.name}")
    
    if st.button("Upload to Backend"):
        # FastAPI endpoint URL
        backend_url = "http://127.0.0.1:8000/upload/"
        
        # Prepare the file payload
        # Passing a tuple: (filename, file_bytes, content_type)
        files = {
            "file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")
        }
        
        with st.spinner("Uploading..."):
            try:
                response = requests.post(backend_url, files=files)
                
                if response.status_code == 201:
                    data = response.json()
                    st.session_state["uploaded_filename"] = data["filename"]
                    st.success(f"🎉 File uploaded successfully!\n\nFilename: {data['filename']}")
                else:
                    st.error(f"❌ Error: {response.json().get('detail', 'Unknown backend error')}")
            except requests.exceptions.ConnectionError:
                st.error("❌ Could not connect to the FastAPI backend. Is it running?")

st.divider()

st.header("Step 2 : Extract PDF")
default_filename = st.session_state.get(
    "uploaded_filename",
    ""
)

st.write(
    f"Current PDF: {st.session_state['uploaded_filename']}"
)

if st.button("Extract PDF"):

    response = requests.post(

        "http://127.0.0.1:8000/extract_pdf",

         params={
            "filename": st.session_state["uploaded_filename"]
        }

    )

    if response.status_code == 200:

        data = response.json()

        st.success("Extraction completed")

        st.write(f"Pages : {data['pages']}")

        st.write(f"Saved : {data['text_file']}")
        st.session_state["extracted_filename"] = data["text_file"]

    else:

        st.error(response.json()["detail"])

st.divider()

st.header("Step 3 : Chunk and Embed")
default_filename = st.session_state.get(
    "extracted_filename",
    ""
)

st.write(
    f"Current Text file: {st.session_state['extracted_filename']}"
)

if st.button("Chunk"):

    response = requests.post(

        "http://127.0.0.1:8000/chunk_api",

        params={
            "filename": st.session_state["extracted_filename"]
        }

    )

    if response.status_code == 200:

        data = response.json()

        st.success("Chunking completed")

        #st.write(f"Total chunks : {data['total_chunks']}")

        st.write(f"Saved : {data['embedding_file']}")
        st.session_state["embedding_file"] = data["embedding_file"]

    else:

        st.write("Status Code:", response.status_code)
        st.write("Response Text:", response.text)



st.divider()

st.header("Step 4 : Ask a Question")
question = st.text_input(
    "Question",
    placeholder="Ask something about the document..."
)

if st.button("Ask"):

    response = requests.post(

        "http://127.0.0.1:8000/ask",

        json={
            "filename": st.session_state["embedding_file"],
            "question": question
        }

    )

    if response.status_code == 200:

        data = response.json()

        st.success("Answer")

        st.write(data["answer"])

    else:

        st.error(response.json()["detail"])