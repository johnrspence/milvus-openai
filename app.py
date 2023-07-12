import os
import streamlit as st
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain import OpenAI
from langchain.vectorstores import Milvus
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from decouple import config

os.environ['OPENAI_API_KEY'] = config('KEY')

llm = OpenAI(temperature=0.5)
embeddings = OpenAIEmbeddings(model="ada")

documents = ['taxlaw2023.pdf']

for docs in documents:
    loader = UnstructuredPDFLoader(docs)

is_loaded = loader.load_and_split()

vector_db = Milvus.from_documents(
    is_loaded,
    embedding=embeddings,
    connection_args={"host":"127.0.0.1", "port":"19530"}
)

st.title("Tax Law 2023")
prompt = st.text_input("Enter Question Here")

chain = load_qa_with_sources_chain(llm, chain_type="map_reduce", return_intermediate_steps=False)

if prompt:
    searched = vector_db.similarity_search(prompt)
    st.write(chain({"input_documents": searched, "question": prompt}, return_only_outputs=True))
