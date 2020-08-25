from abc import ABC, abstractmethod
from retrieval.query_manipulator import QueryManipulator


class AbstractRetriever(ABC):
    underlying_class = None
    _substring_fields = []

    def __init__(self, session):
        self.session = session

    @abstractmethod
    def _dictionarize_objects(self, query):
        """Prepare data for further JSON incapsulation.

        :param query: query to use for joining and retrieval
        :type query: sqlalchemy.orm.query.Query
        :return: dictionary w/ desired fields
        """
        raise NotImplementedError

    def get_objects(self, parameter_values={}):
        entity = type(self).underlying_class
        query = QueryManipulator(self.session.query(entity), entity) \
            .apply_filters(parameter_values, self._substring_fields) \
            .apply_sorting(parameter_values)
        return self._dictionarize_objects(query)
