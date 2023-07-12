# milvus-openai
This project creates a simple streamlit UI to upload PDFs and then directly ask questions about the uploaded PDFS.

# Technologies used
- Streamlit
- Langchain
- Milvus
- Docker

# API Key
It's expected to setup an .env file with your own OpenAI api key to use this project.

# Setting up docker
Refer to the following Milvus [documentation](https://milvus.io/docs/install_standalone-docker.md) to set up your local docker container

# Uploading Documents
Add PDFs to the root project and then update the documents list in the file to include your list
``` python
documents = []
```
# Running the Application
```
streamlit run app.py
```

# Clearing Collections From Milvus
To clear collections from Milvus, use the Jupiter Notebook and run the first and third cell. You can confirm if there is an existing collection using the 2nd cell. The default naming convention is 'LangChainCollection'

# Example
![Screenshot 2023-07-12 at 12 17 48 PM](https://github.com/johnrspence/milvus-openai/assets/139377890/73fba59e-96ac-4b80-9e98-07a2b2f63e45)
