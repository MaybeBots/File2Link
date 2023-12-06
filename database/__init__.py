import env

from database.mongo import Mongo

if env.MONGO_URL:
    DB = Mongo(env.MONGO_URL)
else:
    DB = None
