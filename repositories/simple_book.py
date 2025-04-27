
class Book:
    def __init__(self, id: str, title: str, author: str, year: str):
        self.id = id
        self.title = title
        self.author = author
        self.year = year

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data['id'],
            title=data['title'],
            author=data['author'],
            year=data['year']
        )