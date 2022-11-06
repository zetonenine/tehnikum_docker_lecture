import psycopg2


class PostgresClient:

    def __init__(self, user="tehnikum", password="tehnikum", dbname="tehnikum", host="localhost"):  # host="database" for deploy, database - name of container
        self.connection = psycopg2.connect(
            user=user,
            password=password,
            dbname=dbname,
            host=host
        )
        self.cursor = self.connection.cursor()

    def create(self):
        commands = (
            """
            CREATE TABLE IF NOT EXISTS book (
                id INTEGER NOT NULL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
                name VARCHAR(64) NOT NULL
            )
            """
        )
        with self.connection:
            return self.cursor.execute(commands)

    def add_book(self, book):
        with self.connection:
            return self.cursor.execute("INSERT INTO book (name) VALUES (%s)", (book,))
