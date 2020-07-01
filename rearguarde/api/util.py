def sieve_parameters(parameter_values: dict):
    return {key: parameter_values[key] for key in parameter_values if parameter_values[key]}
