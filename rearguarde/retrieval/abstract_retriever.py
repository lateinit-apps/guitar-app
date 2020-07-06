from abc import ABC, abstractmethod
from sys import stderr


class AbstractRetriever(ABC):
    underlying_class = None
    _substring_fields = []

    def __init__(self, session):
        self.session = session

    def _process_parameter_values(self, parameter_values):
        return [(
            'substring' if key in self._substring_fields else 'exact', key, parameter_values[key]
        ) for key in parameter_values]

    def _apply_filters(self, query, filters_list):
        """Get modified query with applied filters.

        :param query: base query
        :param filters_list: collection of triplets like (match_strategy, 'field', 'value'),
            where `match_strategy` can be either 'exact' or 'substring'
        :type query: sqlalchemy.orm.query.Query
        :type filters_list: list(tuple)
        :return: query with applied modifications
        """
        entity = type(self).underlying_class
        for pair in filters_list:
            match_strategy = pair[0]
            if match_strategy not in ['exact', 'substring']:
                print(f'{key} is not found for class {entity}', file=stderr)
                continue
            field, value = pair[1], pair[2]
            if not hasattr(entity, field):
                print(f'{field} is not found for class {entity}', file=stderr)
                continue
            query = query.filter(getattr(entity, field) == value) if match_strategy == 'exact' \
                else query.filter(getattr(entity, field).ilike(f'%{value}%'))
            # no sense in further filtering of an empty result set
            if not query.count():
                break
        return query

    @abstractmethod
    def _dictionarize_objects(self, query):
        """Prepare data for further JSON incapsulation.

        :param query: query to use for joining and retrieval
        :type query: sqlalchemy.orm.query.Query
        :return: dictionary w/ desired fields
        """
        raise NotImplementedError

    def get_objects(self, parameter_values={}):
        query = self._apply_filters(self.session.query(type(self).underlying_class),
            self._process_parameter_values(parameter_values))
        return self._dictionarize_objects(query)
