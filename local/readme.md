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
