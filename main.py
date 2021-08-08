from app.services.postgresWriter import *
from app.services.text_reader import TextHandler


txt_clear = TextHandler("base_teste.txt")
data = txt_clear.read()
person = Db()
person.insert_lines(data)
