import redis
import logging
import config

r = None


def connect_to_db():
    global r
    try:
        r = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, db=0)
        ping = r.ping()

        if ping == "True":
            logging.info(f"Successful connected to Database")
    except redis.ConnectionError as e:
        print(f"Failed to connect to Redis at {config.REDIS_HOST}: {e}")
        exit(1)
