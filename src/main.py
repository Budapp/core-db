from services import db as db_service


USERNAME = 'postgres'
PASSWORD = 'postgres'
HOST = 'localhost'
DATABASE = 'budapp'


def get_or_create_database(username, password, host, database_name):
    engine_instance = db_service.DatabaseCore(
        USERNAME,
        PASSWORD,
        HOST,
        DATABASE)

    if not engine_instance.exist_database():
        # Create db
        engine_instance.create_database(engine_instance.url)

    return engine_instance

# Example
engine = get_or_create_database(USERNAME, PASSWORD, HOST, DATABASE)

