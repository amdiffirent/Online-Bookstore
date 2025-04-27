from factories.repository_factory import RepositoryFactory
from models.book import Book

def showcase_repository(repo_type: str):
    print(f"\n=== {repo_type.upper()} REPOSITORY DEMO ===")
    
    # Get repository
    repo = RepositoryFactory.get_book_repository(repo_type)
    
    # Create sample data
    books = [
        Book(id="1", title="The Python Handbook", author="John Doe", price=29.99),
        Book(id="2", title="Clean Code", author="Robert Martin", price=39.99),
        Book(id="3", title="Design Patterns", author="GoF", price=49.99)
    ]
    
    # Save books
    for book in books:
        repo.save(book)
        print(f"Saved: {book.title}")
    
    # Retrieve all
    print("\nAll books:")
    for book in repo.find_all():
        print(f"- {book.title} (${book.price})")
    
    # Search
    print("\nSearching for 'Python':")
    results = repo.find_by_title("Python")
    for book in results:
        print(f"- Found: {book.title}")
    
    # Stats
    print(f"\nTotal books: {repo.count()}")

if __name__ == "__main__":
    showcase_repository("MEMORY")
    showcase_repository("JSON")