from abc import ABC, abstractmethod
from sys import stderr


class AbstractRetriever(ABC):
    def __init__(self, session):
        self.session = session

    @staticmethod
    def underlying_class():
        return None

    def _apply_filters(self, query, desired_values):
        for key in desired_values:
            if not hasattr(self.underlying_class(), key):
                print(f'{key} is not found for class {self.underlying_class()}', file=stderr)
                continue
            query = query.filter_by(key=desired_values[key])
        return query

    @abstractmethod
    def get_objects(self, desired_values={}):
        """Retrieve elements with fields satisfying constraints passed as an argument

        Parameters:
            desired_values (dict): key-value map for filter conditions

        Returns:
            satisfied_objects(list): list of objects which met a conjunction of filter entries
        """
        print('Not implemented', file=stderr)
