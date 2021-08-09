import psycopg2 as db
from decouple import config
from psycopg2.extras import execute_values


class Config:
    def __init__(self):
        self.config = {
            "postgres": {
                "user": config('USER'),
                "password": config('PASSWORD'),
                "host": config('HOST'),
                "port": config('PORT'),
                "database": config('DATABASE')
            }
        }


class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro na conexão", e)
            exit(1)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn

    @property
    def cursor(self):
        return self.cur

    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def execute(self, values):
        execute_values(self.cursor,
                       "INSERT INTO neoway_case_tbl VALUES %s", values)

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


class Db(Connection):
    def __init__(self):
        Connection.__init__(self)

    def insert(self, values):
        try:
            print("this operation may take a few minutes...")
            self.execute(values)
            self.commit()

            print("job finished")

        except Exception as e:
            print("Erro ao inserir", e)

