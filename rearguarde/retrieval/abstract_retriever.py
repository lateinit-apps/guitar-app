from abc import ABC, abstractmethod
from re import match
from sys import stderr

from sqlalchemy import asc, desc


class QueryManipulator:

    def __init__(self, query, underlying_class):
        self.query = query.add_entity(underlying_class)
        self.underlying_class = underlying_class

    def apply_filters(self, parameter_values, substring_fields):
        """
        Get query with applied filters extracted from query string parameters.
        """
        filters_list = [(
            'substring' if key in substring_fields else 'exact', key, parameter_values[key]
        ) for key in parameter_values]

        entity = self.underlying_class
        for pair in filters_list:

            match_strategy = pair[0]
            if match_strategy not in ['exact', 'substring']:
                print('inapplicable match strategy has been passed', file=stderr)
                continue
            field, value = pair[1], pair[2]
            if not hasattr(entity, field):
                print(f'{field} field is not found for class {entity}', file=stderr)
                continue

            self.query = self.query.filter(getattr(entity, field) == value) \
                if match_strategy == 'exact' \
                else self.query.filter(getattr(entity, field).ilike(f'%{value}%'))
            # no sense in further filtering of an empty result set
            if not self.query.count():
                break
        return self

    def apply_sorting(self, parameter_values):
        """
        Get query with applied sorting according to the query string parameters.
        """
        if 'sort_by' in parameter_values \
            and match('(\w+!(asc|desc))(,\w+!(asc|desc))*$', parameter_values['sort_by']):

            comma_separated = parameter_values['sort_by'].split(',')
            for item in [x for x in comma_separated if x]:

                key, order = item.split('!')[0], item.split('!')[1]
                if not hasattr(self.underlying_class, key):
                    print(f'{key} cannot be used as a sorting key', file=stderr)
                    continue

                self.query = self.query.order_by(asc(getattr(self.underlying_class, key))) \
                    if order == 'asc' \
                    else self.query.order_by(desc(getattr(self.underlying_class, key)))
        return self

    def withdraw_query(self):
        return self.query


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
        query = QueryManipulator(self.session.query(), type(self).underlying_class) \
            .apply_filters(parameter_values, self._substring_fields) \
            .apply_sorting(parameter_values) \
            .withdraw_query()
        return self._dictionarize_objects(query)
