import asyncio 
import logging
from motor.motor_asyncio import AsyncIOMotorClient


class Mongo:

    def __init__(self, url):
        self.mongo = AsyncIOMotorClient(url)
        self.db = self.mongo.FileDb
        self.usersdb = self.db.usersdb
        self.filedb = self.db.filedb
        self._cache = {}
        self._group_media_cache = []
        asyncio.ensure_future(self.load_file_id())

    def add_group_media(self, id):
        self._group_media_cache.append(id)
        return 

    def get_group_media(self):
        return self._group_media_cache
        
    def get_msg_ids(self, file_id):
        return self._cache.get(file_id, False)

    async def load_file_id(self):
        file_ids = self.filedb.find()
        if not file_ids:
            return 
        _file_ids = await file_ids.to_list(length=1000000000)
        for i in _file_ids:
            self._cache[i['file_id']] = i['msg_ids']
        logging.info('File ids Initialised Successfully')
        
    async def add_file_id(self, file_id, msg_ids):
        self._cache[file_id] = msg_ids
        await self.filedb.insert_one({'file_id': file_id, 'msg_ids': msg_ids})
        
    async def get_users(self) -> list:
        user = self.usersdb.find()
        if not user:
            return []
        user_list = []
        for user in await user.to_list(length=1000000000):
            user_list.append(user)
        return user_list

    async def is_user(self, user_id: int) -> bool:
        user = await self.usersdb.find_one({"user_id": user_id})
        if not user:
            return False
        return True

    async def add_user(self, user_id: int):
        is_served = await self.is_user(user_id)
        if is_served:
            return
        return await self.usersdb.insert_one({"user_id": user_id})
        
