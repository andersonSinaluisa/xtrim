from abc import (
    ABCMeta,
    abstractmethod
)

class AuditRepositoryInterface:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def create(self, audit):
        raise NotImplementedError
    
    
    @abstractmethod
    def get_all(self):
        raise NotImplementedError