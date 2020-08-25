from sys import stderr


class QueryManipulator:
    def __init__(self, query, underlying_class):
        self.query = query
        # TODO investigate whether the underlying class can be extracted from the query
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
        return query


    def apply_sorting(self, parameter_values):
        """
        Get query with applied sorting according to the query string parameters.
        """
        return query
