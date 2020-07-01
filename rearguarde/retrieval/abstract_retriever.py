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

        Parameters:
            query (sqlalchemy.orm.query.Query): base query
            filters_list (list): collection of tuples like (match_strategy, 'field', 'value'),
                where `match_strategy` can be either 'exact' or 'substring'
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
                else query.filter(getattr(entity, field).like(f'%{value}%'))
            # no sense in further filtering of an empty result set
            if not query.count():
                break
        return query

    @abstractmethod
    def get_objects(self, parameter_values={}):
        """Retrieve elements with fields satisfying constraints passed as an argument.

        Parameters:
            parameter_values (dict): key-value map for filter conditions

        Returns:
            satisfied_objects (list): list of objects which met a conjunction of filter entries
        """
        raise NotImplementedError
