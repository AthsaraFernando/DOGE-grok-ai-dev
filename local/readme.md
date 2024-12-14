# MultiPDF Chat App

## Introduction

---

The MultiPDF Chat App is a Python application that allows you to chat with multiple PDF documents. You can ask questions about the PDFs using natural language, and the application will provide relevant responses based on the content of the documents. This app utilizes a language model to generate accurate answers to your queries. Please note that the app will only respond to questions related to the loaded PDFs.

## How to Run the Program

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

## How It Works

---

![MultiPDF Chat App Diagram](./docs/PDF-LangChain.jpg)

The application follows these steps to provide responses to your questions:

1. PDF Loading: The app reads multiple PDF documents and extracts their text content.

2. Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

3. Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

## License

---

The MultiPDF Chat App is released under the [MIT License](https://opensource.org/licenses/MIT).
