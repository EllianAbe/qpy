from datetime import datetime

initial: list[dict] = [
    {
        'data': {
            'name': 'test 1',
        },
        'creation_date': datetime.now(),
        'status': 'pending'
    },
    {
        'data': {
            'name': 'test 2',
        },
        'creation_date': datetime.now(),
        'status': 'pending'
    },
    {
        'data': {
            'name': 'test 3',
        },
        'creation_date': datetime.now(),
        'status': 'pending'
    },
    {
        'data': {
            'name': 'test 4',
        },
        'creation_date': datetime.now(),
        'status': 'success',
        'output_data': {
            'name': 'product 4',
        }
    }
]
