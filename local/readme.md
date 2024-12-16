# AI Tax Agent App - DOGE Grok AI

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen)](https://huggingface.co/spaces/Athsara/DOGE-grok-ai-dev)

https://huggingface.co/spaces/Athsara/DOGE-grok-ai-dev

## Introduction

---

An AI-driven chatbot to assist citizens with tax inquiries, provide accurate information from a knowledge base, and facilitate appointment bookings for audits and inquiries efficiently.

## How to Run the Program Locally

To set up and run the program, follow these steps:

1. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install the required dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Obtain an API key from GrokAI and add it to the `.env` file in the project directory.

```commandline
GROK_API_KEY=your_secrit_api_key
```

5. Run the application:
   ```bash
   streamlit run app.py
   ```

Once completed, the app will open in your default web browser. If it doesn't, check the terminal for the link (usually `http://localhost:8501`).

## How the Code Works

---

The application is built using Python and Streamlit and integrates various technologies like GrokAI, HuggingFace, and FAISS to create a conversational AI chatbot capable of answering tax-related queries. Here is a breakdown of the code’s major components and their functionalities:

### 1. **Text Extraction from PDFs**

The `get_pdf_text` function is responsible for extracting raw text from PDF documents. It utilizes the `PdfReader` class from the PyPDF2 library to read each page of the PDF and extract its text content. This function:

- Iterates through all uploaded PDF files.
- Reads each page using `PdfReader`.
- Concatenates the extracted text into a single string for further processing.

**Optimization Techniques:**

- Batch reading of files to minimize I/O overhead.
- Filtering out empty pages to save processing time.

### 2. **Splitting Text into Chunks**

The `get_text_chunks` function breaks the raw text into manageable chunks to enhance processing efficiency. It uses the `CharacterTextSplitter` from the LangChain library, which:

- Splits the text based on a configurable `separator` (newline by default).
- Ensures that chunks do not exceed a specified size (`chunk_size`), with optional overlap (`chunk_overlap`) to maintain context between chunks.
- Uses the `length_function` parameter to measure chunk sizes accurately.

**Optimization Techniques:**

- Overlapping chunks ensure better context retention in conversation.
- Splitting based on logical separators (e.g., newlines) to preserve readability.

### 3. **Creating a Vector Store**

The `get_vectorstore` function creates a vector database using HuggingFace embeddings and FAISS. This step involves:

- Generating text embeddings with the HuggingFace `sentence-transformers/all-MiniLM-L6-v2` model.
- Storing these embeddings in a FAISS index for efficient similarity search and retrieval.
- Using the HuggingFace API key for authentication when accessing the model.

**Optimization Techniques:**

- The FAISS library ensures fast similarity search and indexing, even with large datasets.
- Pretrained HuggingFace models reduce computational overhead.

### 4. **Conversational Retrieval Chain**

The `get_conversation_chain` function initializes the conversational retrieval chain using LangChain and GrokAI. It:

- Configures the GrokAI language model (`ChatOpenAI`) with a specified API key, base URL, and temperature settings.
- Uses `ConversationBufferMemory` to store and manage chat history, enabling contextual conversations.
- Combines the language model and vector retriever in a `ConversationalRetrievalChain` for seamless integration.

**Optimization Techniques:**

- Memory buffering reduces redundant queries by maintaining context across conversations.
- GrokAI’s LLM configuration allows fine-tuning of response behavior (e.g., temperature adjustment).

### 5. **Handling User Input**

The `handle_userinput` function processes user queries by:

- Validating the availability of the conversation chain.
- Passing the user’s question to the chain and retrieving responses.
- Updating the session’s chat history for display.

### 6. **Real-Time Chat Interface**

The `display_chat_history` function renders the chat history in the Streamlit app. It:

- Iterates through the chat history stored in the session state.
- Uses HTML templates (`bot_template` and `user_template`) for consistent formatting.
- Injects JavaScript to enable automatic scrolling to the latest message.

### 7. **Automated Document Processing**

The `load_and_process_pdfs` function handles the entire workflow of processing PDFs. It:

- Scans a specified folder for PDF files.
- Extracts text, splits it into chunks, and creates a vector store.
- Initializes the conversation chain using the vector store and LLM.

**Optimization Techniques:**

- Automated file handling minimizes manual intervention.
- Sequential progress indicators improve user experience during processing.

### 8. **Streamlit Application Structure**

The `main` function ties everything together and initializes the Streamlit app. It:

- Loads environment variables from a `.env` file (e.g., API keys).
- Configures session state for chat history and conversation chain.
- Automatically processes PDF documents on startup.
- Renders the chat interface and input box for user interaction.

**Key Features:**

- Automatic loading and processing of documents ensure the app is ready for queries immediately.
- Integration with Streamlit’s `text_input` widget for smooth user input handling.

## Technologies Used

![Grok AI](https://img.shields.io/badge/Grok_AI-563D7C?style=for-the-badge&logo=GrokAI&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-000000?style=for-the-badge&logo=langchain&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-F9DC3E?style=for-the-badge&logo=huggingface&logoColor=black)
![FAISS](https://img.shields.io/badge/FAISS-2E3440?style=for-the-badge)
![Dotenv](https://img.shields.io/badge/Dotenv-007ACC?style=for-the-badge&logo=dotenv&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![NLP](https://img.shields.io/badge/NLP-FF5722?style=for-the-badge)
![AI Chatbot](https://img.shields.io/badge/AI_Chatbot-4CAF50?style=for-the-badge)

**Note:** Some technologies like Grok AI and LangChain might not have official logos available on Shields.io. In such cases, you can create custom badges or use alternative visual representations.

### Detailed List with Descriptions

```markdown
## Technologies Used

- **Grok AI**: API used for interfacing with the GrokAI language model, facilitating the generation of conversational responses and enhancing the chatbot's ability to understand and process user queries effectively.
- **Streamlit**: Framework used for building the interactive web application interface.
- **Python**: The primary programming language utilized for development.
- **LangChain**: Framework facilitating the integration and management of language models within the application.
- **HuggingFace**: Platform used for deploying the application online, leveraging Hugging Face’s infrastructure and services.
- **FAISS**: Vector search library for efficient similarity search and indexing of embeddings.
- **Dotenv**: Manages environment variables securely, keeping sensitive information like API keys safe.
- **HTML/CSS**: Technologies used for frontend customization and styling of the web application.
- **JavaScript**: Adds interactivity and dynamic behavior to the frontend components.
- **Conversational AI**: Core technology enabling the chatbot to engage in interactive dialogues based on user input.
- **Natural Language Processing (NLP)**: Field of AI focused on the interaction between computers and human language, underpinning the chatbot's functionality.
- **Vector Databases**: Manage and query vectorized data efficiently, essential for handling embeddings and similarity searches.
- **AI Chatbot**: The primary functionality of the application, enabling interactive conversations based on the content of multiple PDFs.

## License

---

The AI Tax Agent App is released under the [MIT License](https://opensource.org/licenses/MIT).
```
