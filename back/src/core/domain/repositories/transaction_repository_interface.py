
from abc import (
    ABCMeta,
    abstractmethod
)

class TransactionRepositoryInterface:
    
    __metaclass__ = ABCMeta
    
    
    @abstractmethod
    def create(self, transaction):
        raise NotImplementedError