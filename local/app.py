import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings  # Changed to HuggingFace
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI  # For LLM
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template

# Function to extract text from PDF documents
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text
    return text

# Function to split text into manageable chunks
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# Function to create a vector store using HuggingFace embeddings
def get_vectorstore(text_chunks, huggingface_api_key):
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",  # Choose an appropriate model
        model_kwargs={"use_auth_token": huggingface_api_key}
    )
    
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

# Function to initialize the conversational retrieval chain with GrokAI
def get_conversation_chain(vectorstore, grok_api_key, grok_api_base):
    llm = ChatOpenAI(
        openai_api_key=grok_api_key,
        openai_api_base=grok_api_base,
        model_name="grok-beta",  # Specify GrokAI's model
        temperature=0.5
    )
    
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True
    )
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,  # Use the configured GrokAI LLM
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

# Function to handle user input and generate responses
def handle_userinput(user_question):
    if st.session_state.conversation is None:
        st.warning("Documents are still being processed. Please wait.")
        return

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

# Function triggered when the user presses Enter in the input box
def on_enter():
    user_question = st.session_state.user_question
    if user_question:
        handle_userinput(user_question)
        st.session_state.user_question = ""  # Clear the input box

# Function to load and process PDF documents
def load_and_process_pdfs(folder_path, huggingface_api_key, grok_api_key, grok_api_base):
    pdf_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.pdf')]
    if not pdf_files:
        st.error(f"No PDF files found in the directory: {folder_path}")
        return

    pdf_docs = []
    for file in pdf_files:
        file_path = os.path.join(folder_path, file)
        pdf_docs.append(file_path)

    with st.spinner("Processing documents..."):
        # Extract text from PDFs
        with st.spinner("Extracting text from PDFs..."):
            pdf_file_objects = [open(file, 'rb') for file in pdf_docs]
            raw_text = get_pdf_text(pdf_file_objects)
            # Close the files after reading
            for f in pdf_file_objects:
                f.close()

        # Split text into chunks
        with st.spinner("Splitting text into chunks..."):
            text_chunks = get_text_chunks(raw_text)

        # Create vector store using HuggingFace embeddings
        with st.spinner("Creating vector store..."):
            vectorstore = get_vectorstore(text_chunks, huggingface_api_key)

        # Initialize conversation chain with GrokAI LLM
        with st.spinner("Initializing conversation chain..."):
            st.session_state.conversation = get_conversation_chain(vectorstore, grok_api_key, grok_api_base)

    st.success("Documents processed successfully!")

# Function to display chat history with auto-scrolling
def display_chat_history():
    if st.session_state.chat_history:
        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.markdown(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.markdown(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        
        # Inject JavaScript to scroll the entire page to the bottom
        scroll_script = """
        <script>
            // Function to scroll to the bottom of the page
            function scrollToBottom() {
                window.scrollTo({ top: document.body.scrollHeight, behavior: 'smooth' });
            }
            // Delay to ensure the DOM is fully rendered
            setTimeout(scrollToBottom, 100);
        </script>
        """
        st.markdown(scroll_script, unsafe_allow_html=True)

# Main function to run the Streamlit app
def main():
    load_dotenv()
    
    # Retrieve credentials from .env
    grok_api_key = os.getenv("GROK_API_KEY")
    grok_api_base = "https://api.x.ai/v1"  # GrokAI's API base URL
    huggingface_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    
    st.set_page_config(page_title="Chat with AI Tax Agent", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Title Section
    st.header("Chat with AI Tax Agent :books:")

    # Automatically load and process PDFs on startup
    if st.session_state.conversation is None:
        documents_folder = "./documents/"  # Specify your documents folder path here
        load_and_process_pdfs(documents_folder, huggingface_api_key, grok_api_key, grok_api_base)

    # Chat History Section
    display_chat_history()

    # Input Box Section
    st.text_input(
        "Ask a question about your documents:",
        key='user_question',
        on_change=on_enter
    )

if __name__ == '__main__':
    main()
