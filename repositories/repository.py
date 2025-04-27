from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Optional, List

T = TypeVar('T')  # Entity type
ID = TypeVar('ID')  # ID type (could be str, int, etc.)

class Repository(Generic[T, ID], ABC):
    @abstractmethod
    def save(self, entity: T) -> None:
        """Create or Update an entity"""
        pass
    
    @abstractmethod
    def find_by_id(self, id: ID) -> Optional[T]:
        """Find entity by ID"""
        pass
    
    @abstractmethod
    def find_all(self) -> List[T]:
        """Find all entities"""
        pass
    
    @abstractmethod
    def delete(self, id: ID) -> None:
        """Delete an entity by ID"""
        pass