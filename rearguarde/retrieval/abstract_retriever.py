from abc import ABC, abstractmethod
from sys import stderr


class AbstractRetriever(ABC):
    def __init__(self, session):
        self.session = session

    @abstractmethod
    def get_objects(self, desired_values={}):
        """Retrieve elements with fields satisfying constraints passed as an argument

        Parameters:
            desired_values (dict): key-value map for filter conditions

        Returns:
            satisfied_objects(list): list of objects which met a conjunction of filter entries
        """
        print("Not implemented", file=stderr)
