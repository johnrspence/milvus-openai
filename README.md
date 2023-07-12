# milvus-openai
This project creates a simple streamlit UI to upload PDFs and then directly ask questions about the uploaded PDFS.

# Technologies used
- Streamlit
- Langchain
- Milvus
- Docker

# Setting up docker
Refer to the following Milvus [documentation](https://milvus.io/docs/install_standalone-docker.md) to set up your local docker container

# Uploading Documents
Add PDFs to the root project and then update the documents list in the file to include your list
``` python
documents = []
```

# Clearing Collections From Milvus
To clear collections from Milvus, use the Jupiter Notebook and run the first and third cell. You can confirm if there is an existing collection using the 2nd cell. The default naming convention is 'LangChainCollection'
