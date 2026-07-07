from math import sqrt


def dot_product(vec1: list[float], vec2: list[float]) -> float:
    """
        Calculate the dot product of two vectors.
    """
    
    if len(vec1) != len(vec2):
        raise ValueError('Vector dimension must match')

    return sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    

def magnitude(vec: list[float]) -> float:
    """
        Calculate the magnitude of a vector.
    """
    return sqrt(dot_product(vec, vec))


def cosine_similarity(vec1: list[float], vec2: list[float]) -> float:
    """
        Calculate the cosine similarity of two vectors.
    """

    dot_prod = dot_product(vec1, vec2)
    
    mag1 = magnitude(vec1)
    
    mag2 = magnitude(vec2)
    
    if dot_prod == 0 or mag1 == 0 or mag2 == 0:
        return 0
        
    return dot_prod / (mag1 * mag2)


def most_similar_chunks(
    query_vec: list[float],
    chunk_embeddings: list[dict],
    top_k: int = 3
) -> list[dict]:
    """
        Return the top K most similar chunks to the query vector.
    """
    