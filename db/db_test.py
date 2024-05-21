from db_conn import dbConnection


db = dbConnection()

db.connect()
q = "INSERT INTO users(name, email, password, active, last_login) VALUES('Testowy2', 'testowy2@exmaple.com', 'dupa66', TRUE, now()) ;"
rows = db.insert(q)
print(rows)
db.close