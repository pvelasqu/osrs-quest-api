import os

CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUDSQL_CONNECTION_NAME')
CLOUDSQL_USER = os.environ.get('CLOUDSQL_USER')
CLOUDSQL_PASSWORD = os.environ.get('CLOUDSQL_PASSWORD')


def database_connection_string():
    if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        connection_string = 'mysql+pymsql://{username}:{password}@127.0.0.1:3306/{database_name}'.format(
            username=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD, database_name=CLOUDSQL_CONNECTION_NAME
        )
    else:
        connection_string = 'local'

    return connection_string
