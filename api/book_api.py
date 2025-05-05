
from fastapi import APIRouter, HTTPException
from typing import List
from models.book import Book
from services.book_service import BookService
from repositories.book_repository import BookRepository

router = APIRouter(prefix="/api/books", tags=["Books"])

book_service = BookService(BookRepository())

@router.post("/", response_model=Book)
def create_book(book: Book):
    return book_service.create_book(book)

@router.get("/", response_model=List[Book])
def get_all_books():
    return book_service.get_all_books()

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: str):
    try:
        return book_service.get_book(book_id)
    except ValueError:
        raise HTTPException(status_code=404, detail="Book not found")

@router.put("/{book_id}", response_model=Book)
def update_book(book_id: str, book: Book):
    try:
        return book_service.update_book(book_id, book)
    except ValueError:
        raise HTTPException(status_code=404, detail="Book not found")

@router.delete("/{book_id}")
def delete_book(book_id: str):
    try:
        book_service.delete_book(book_id)
        return {"message": "Book deleted"}
    except ValueError:
        raise HTTPException(status_code=404, detail="Book not found")
