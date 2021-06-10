CONFIG = {
    'version': 1,  # Currently the only supported version, left for backwards compatibility
    'disable_existing_loggers': False,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s %(levelname)-8s:: %(name)s - %(message)s',
        },
    },
    'handlers': { 
        'standard': { 
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
    },
    'root': {
        'handlers': ['standard'],
        'level': 'DEBUG',  # TODO change to INFO in prod
        'propagate': True,
    },
}
