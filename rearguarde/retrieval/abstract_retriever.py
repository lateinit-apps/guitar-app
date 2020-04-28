from abc import ABC, abstractmethod
from sys import stderr


class AbstractRetriever(ABC):
    underlying_class = None

    def __init__(self, session):
        self.session = session

    def _apply_filters(self, query, desired_values):
        entity = type(self).underlying_class
        for key in desired_values:
            if not hasattr(entity, key):
                print(f'{key} is not found for class {entity}', file=stderr)
                continue
            query = query.filter(getattr(entity, key) == desired_values[key])
        return query

    @abstractmethod
    def get_objects(self, desired_values={}):
        """Retrieve elements with fields satisfying constraints passed as an argument

        Parameters:
            desired_values (dict): key-value map for filter conditions

        Returns:
            satisfied_objects(list): list of objects which met a conjunction of filter entries
        """
        raise NotImplementedError
