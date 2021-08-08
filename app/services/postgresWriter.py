import psycopg2 as db
from decouple import config


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

    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()


class Db(Connection):
    def __init__(self):
        Connection.__init__(self)

    def insert(self, values):
        try:

            sql = "INSERT INTO neoway_case_tbl (" \
                  "cpf," \
                  "private," \
                  "incompleto," \
                  "data_ultima_compra," \
                  "ticket_medio," \
                  "ticket_ultima_compra," \
                  "loja_mais_frequente," \
                  "loja_ultima_compra) " \
                  "VALUES ({cpf}, {private}, {incompleto}, {data_ultima_compra}, {ticket_medio}, " \
                  "{ticket_ultima_compra}, {loja_mais_frequente}, {loja_ultima_compra})".format(
                    cpf=values[0],
                    private=values[1],
                    incompleto=values[2],
                    data_ultima_compra=values[3],
                    ticket_medio=values[4],
                    ticket_ultima_compra=values[5],
                    loja_mais_frequente=values[6],
                    loja_ultima_compra=values[-1])

            self.execute(sql)
            self.commit()

        except Exception as e:
            print("Erro ao inserir", e)

    def insert_lines(self, data):
        try:
            for row in data:
                self.insert(row)
        except Exception as e:
            print(e)
