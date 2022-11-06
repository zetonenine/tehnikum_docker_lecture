from flask import Flask, render_template
from app.postgres_client import PostgresClient
from app.redis_client import RedisClient

app = Flask(__name__)

r = RedisClient()
db = PostgresClient()
db.create()


@app.route('/')
def index():
	count = r.counter()
	return render_template(
		'index.html',
		count=count
	)


@app.route('/add/<book>')
def add(book):
	db.add_book(book)
	return render_template(
		'add.html',
		book=book
	)


if __name__ == '__main__':
	app.run(host="0.0.0.0")
