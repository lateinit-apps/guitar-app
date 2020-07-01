def normalize_parameters(parameter_values: dict):
    result = dict()
    for key in parameter_values:
        value = parameter_values[key]
        if not value:
            continue
        print(f'{key}:{value}')
    return result
