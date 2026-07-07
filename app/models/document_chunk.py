from dataclasses import dataclass, field , asdict
from typing import Optional


@dataclass
class DocumentChunk:
    """
    Represents a chunk throughout the entire RAG pipeline.
    """
    chunk_id: int
    document: str
    text: str
    word_count: int
    metadata: dict = field(default_factory=dict)
    embedding: Optional[list[float]] = None
    similarity_score: Optional[float] = None

    def to_dict(self)->dict:
        """Convert object to dictionary."""
        return asdict(self)

    
    @classmethod
    def from_dict(cls, data: dict):
        """Create object from dictionary."""
        return cls(**data)