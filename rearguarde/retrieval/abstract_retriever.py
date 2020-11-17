from abc import ABC, abstractmethod
from re import match
from sys import stderr

from sqlalchemy import asc, desc, func


class QueryManipulator:

    SORTING_FUNCTIONS = {'len': func.char_length}

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
        ident = r'[0-9a-z\_]+'
        ident_with_parentheses = r'[0-9a-z\_\(\)]+'
        if 'sort_by' in parameter_values \
            and match(rf'({ident_with_parentheses}!(asc|desc))' \
                      rf'(,{ident_with_parentheses}!(asc|desc))*$',
                      parameter_values['sort_by']):

            comma_separated = parameter_values['sort_by'].split(',')
            for item in [x for x in comma_separated if x]:

                format_match = match(
                    rf'((?P<func_call>(?P<func_name>{ident})\((?P<func_arg>{ident})\))' \
                    rf'|(?P<raw>{ident}))!(?P<order>\w+)',
                    item)

                # TODO change all that `continue`-trailing boilerplate into exception throwing
                if not format_match:
                    print(f'"{item}" does not satisfy the required sort_by format', file=stderr)
                    continue

                patterns = format_match.groupdict()
                if patterns['func_call']:

                    if patterns['func_name'] not in self.SORTING_FUNCTIONS:
                        print(f'\"{patterns["func_name"]}\" sorting function is not allowed',
                              file=stderr)
                        continue
                    if not hasattr(self.underlying_class, patterns['func_arg']):
                        print(f'\"{patterns["func_arg"]}\" is not in the attributes list of the ' \
                              f'"{self.underlying_class.__name__}"',
                              file=stderr)
                        continue
                    key = self.SORTING_FUNCTIONS[patterns['func_name']](getattr(
                        self.underlying_class, patterns['func_arg']))

                else:
                    if not hasattr(self.underlying_class, patterns['raw']):
                        print(f'\"{patterns["raw"]}\" is not in the attributes list of the ' \
                              f'"{self.underlying_class.__name__}"',
                              file=stderr)
                        continue
                    key = getattr(self.underlying_class, patterns['raw'])

                self.query = self.query.order_by(asc(key)) if patterns['order'] == 'asc' \
                    else self.query.order_by(desc(key))
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
