from langchain_community.embeddings.ollama import OllamaEmbeddings
from langchain_community.embeddings.bedrock import BedrockEmbeddings
import logging

logger = logging.getLogger("EmbeddingFunction")

def get_embedding_function(model_name="nomic-embed-text", fallback=True):
    """
    Get embedding function with fallback options
    
    Args:
        model_name: Name of the Ollama embedding model to use
        fallback: Whether to try alternative models if the primary fails
        
    Returns:
        An embedding function compatible with LangChain
    """
    try:
        logger.info(f"Initializing embedding model: {model_name}")
        embeddings = OllamaEmbeddings(model=model_name)
        
        # Test the embedding function with a simple input
        test_result = embeddings.embed_query("test")
        if test_result and len(test_result) > 0:
            logger.info(f"Successfully initialized {model_name} embedding model")
            return embeddings
        else:
            raise ValueError("Embedding model returned empty embeddings")
            
    except Exception as e:
        logger.warning(f"Error initializing {model_name}: {str(e)}")
        
        if fallback:
            # Try alternative models
            alternative_models = ["all-MiniLM-L6-v2", "gte-small"]
            
            for alt_model in alternative_models:
                try:
                    logger.info(f"Trying alternative embedding model: {alt_model}")
                    embeddings = OllamaEmbeddings(model=alt_model)
                    test_result = embeddings.embed_query("test")
                    if test_result and len(test_result) > 0:
                        logger.info(f"Successfully initialized {alt_model} embedding model")
                        return embeddings
                except Exception as alt_e:
                    logger.warning(f"Error initializing {alt_model}: {str(alt_e)}")
            
            # If all Ollama models fail, try Bedrock as last resort
            try:
                logger.info("Trying Bedrock embeddings as fallback")
                embeddings = BedrockEmbeddings(
                    credentials_profile_name="default", 
                    region_name="us-east-1"
                )
                return embeddings
            except Exception as bedrock_e:
                logger.error(f"Error initializing Bedrock embeddings: {str(bedrock_e)}")
                
            # If all else fails, raise the original error
            raise e
        else:
            # If fallback is disabled, just raise the original error
            raise e
