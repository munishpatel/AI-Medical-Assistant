from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

# Extract the data from the source (pdf) documents


def load_pdf_file(data):
    loader = DirectoryLoader(data, glob="*.pdf", loader_cls=PyPDFLoader)
    # Here *.pdf means only loading pdf's
    documents = loader.load()
    return documents


# Splitting the data into small text chunks
def text_split(extracted_data):
    test_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=20)
    text_chunks = test_splitter.split_documents(extracted_data)
    return text_chunks


# Downloading the embedding from hugging face
def get_embedding_model():
    embedding_model = HuggingFaceEmbeddings(
        model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embedding_model
