from factories.repository_factory import RepositoryFactory
from models.book import Book

def main():
    # Get repository (switch between "MEMORY" and "JSON")
    repo = RepositoryFactory.get_book_repository("MEMORY")
    
    # Create some books
    books = [
        Book(id="1", title="Clean Code", author="Robert Martin"),
        Book(id="2", title="Design Patterns", author="GoF"),
        Book(id="3", title="Python Crash Course", author="Eric Matthes")
    ]
    
    # Save books
    for book in books:
        repo.save(book)
    
    # Query books
    print("All books:")
    for book in repo.find_all():
        print(f"- {book.title} by {book.author}")
    
    # Find specific book
    print("\nSearch results for 'Python':")
    for book in repo.find_by_title("Python"):
        print(f"- {book.title}")

if __name__ == "__main__":
    main()

from fastapi import FastAPI
from api.book_api import router as book_router
from api.user_api import router as user_router
from api.order_api import router as order_router

app = FastAPI(
    title="Online Bookstore API",
    description="REST API for books, users, and orders",
    version="1.0.0"
)

app.include_router(book_router)
app.include_router(user_router)
app.include_router(order_router)
