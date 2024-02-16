from abc import (
    ABCMeta,
    abstractmethod
)



class UserRepositoryInterface:
    __metaclass__ = ABCMeta
    @abstractmethod
    def create(self, user):
        raise NotImplementedError

    @abstractmethod
    def get_user_by_email(self, email):
        raise NotImplementedError

    
    @abstractmethod
    def get_user_by_id(self, user_id):
        raise NotImplementedError
    
    
    @abstractmethod
    def validate_credentials(self, email, password):
        raise NotImplementedError