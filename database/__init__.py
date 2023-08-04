import env

from database.mongo import Mongo

DB = Mongo(env.MONGO_URL) 