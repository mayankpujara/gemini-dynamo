from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_vertexai import VertexAI
from vertexai.generative_models import GenerativeModel
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from tqdm import tqdm
import logging

# Configure log

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class GeminiProcessor:
    
    def __init__(self, model_name, project):
        self.model =    VertexAI(model_name=model_name, project=project)
    
    def generate_document_summary(self, documents: list, **args):

        chain_type = "map_reduce" if len(documents) > 10 else "stuff"
        chain = load_summarize_chain(
            llm = self.model,
            chain_type=chain_type,
            
            **args
            )
        
        return chain.run(documents)
    
    def count_tokens(self, docs:list):
        temp_model = GenerativeModel("gemini-1.0-pro")
        total = 0
        logger.info("Counting total tokens")
        for doc in tqdm(docs):
            total += temp_model.count_tokens(doc.page_content).total_tokens

    def get_model(self):
        return self.model

class YoutubeProcessor:
    # Retrieve the full transcript

    def __init__(self, genai_processor: GeminiProcessor):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=0
        )
        self.GeminiProcessor = genai_processor
    
    def retrive_youtube_documents(self, video_url:str, verbose=False):

        loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=True)
        docs = loader.load()
        result = self.text_splitter.split_documents(docs)   
        
        author = result[0].metadata['author']
        length = result[0].metadata['length']
        title = result[0].metadata['title']
        total_size = len(result)

        if verbose:
            logger.info(f"{author}\n{length}\n{title}\n{total_size}")

        return result

    def find_key_concepts(self, documents:list, group_size: int = 2):
        # Iterate through all the documents of group size N and find the key concepts
        if group_size > len(documents):
            raise ValueError("Group size is larger than the number of documents")
        
        # Find number of documents in each group
        num_docs_per_group = len(documents) // group_size + (len(documents) % group_size >0)

        # Split the documents into chunks of size num_docs_per_group
        groups = [documents[i:i+num_docs_per_group] for i in range(0, len(documents), num_docs_per_group)]

        batch_concepts = []

        logger.info("Finding the key concepts...")
        for group in tqdm(groups):
            # Combine contents of documents per group [Group 1 | Group 2 ...]
            group_content = ""

            for doc in group:
                group_content += doc.page_content

            # Prompt for finding the concepts
            prompt = PromptTemplate(
                template = """
                Find and define key concepts or terms found in the text:
                {text}

                Respond in the following format as a string separating each concept with a comma:
                "concept": "definition"
                """,
                input_variables=["text"]
            )

            # Chain creation
            chain = prompt | self.GeminiProcessor.model

            # Run Chain
            concept = chain.invoke({"text": group_content})
            batch_concepts.append(concept)

        return batch_concepts




