from flask_restx import Api

INVALID_PARAMS_STATUS_CODE = 400


def abort_on_invalid_parameters(api: Api, request_parameters: dict):
    for key in request_parameters:
        if key.endswith('_id') and int(request_parameters[key]) < 1:
            api.abort(INVALID_PARAMS_STATUS_CODE, 'Input payload validation failed',
                      **{key: f'Invalid {key}: {request_parameters[key]}. '
                              + f'{key} must be a positive integer' for key in request_parameters})


def remove_empty_parameters(parameter_values: dict):
    return {key: parameter_values[key] for key in parameter_values if parameter_values[key]}
