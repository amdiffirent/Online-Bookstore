from dataclasses import dataclass

@dataclass
class Book:
    id: str
    title: str
    author: str
    isbn: Optional[str] = None
    price: Optional[float] = None
    stock: int = 0
    
    def __post_init__(self):
        if not self.id:
            raise ValueError("Book ID cannot be empty")
        if not self.title:
            raise ValueError("Title cannot be empty")