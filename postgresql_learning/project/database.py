import psycopg2
from psycopg2 import pool

# Connection Pool
class Database:
    connection_pool = None

    @classmethod
    def initialise(cls):
        cls.connection_pool = pool.SimpleConnectionPool(1,
                                                        10,
                                                        user='ofrance002',
                                                        password='',
                                                        database='test_db',
                                                        host='localhost')

    @classmethod
    def get_connection(cls):
        return cls.connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        Database.connection_pool.putconn(connection)

    @classmethod
    def close_all_connections(cls):
        Database.connection_pool.closeall()


# Class Connection pool
class CursorFromConnectionFromPool:
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection = Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val is not None: # e.g. TypeError, AttributeError, ValueError
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
        Database.return_connection(self.connection)
