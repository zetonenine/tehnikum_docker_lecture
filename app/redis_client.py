import redis


class RedisClient:
	def __init__(self, host='redis', port=6379, db=0):  # host="redis" for deploy
		self.redis_instance = redis.Redis(
			host=host,
			port=port,
			db=db
		)
		if not self.redis_instance.exists("count"):
			self.redis_instance.set(
				"count",
				"0"
			)

	def counter(self):
		count = int(self.redis_instance.get("count"))

		self.redis_instance.set(
			"count",
			str(count + 1)
		)
		return count + 1
