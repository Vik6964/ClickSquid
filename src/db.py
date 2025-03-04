import clickhouse_connect

class DB:
    def __init__(self, config):
        self.__client = clickhouse_connect.get_client(
            host = config['host'],
            database = config['database'],
            username = config['user'],
            password = config['pass'],
        )
        
    def insert(self, values):
        self.__client.query(f"INSERT INTO access_logs SETTINGS async_insert=1, wait_for_async_insert=1 VALUES ({values})")
