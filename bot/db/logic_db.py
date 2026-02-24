from abc import ABC, abstractmethod

from redis.asyncio import Redis




class DataBase(ABC):
    @abstractmethod 
    async def create_user(self, username : str, user_id, email : str) -> bool:
        pass
    
    @abstractmethod 
    async def delete_user(self, user_id : str) -> bool:
        pass
    
    @abstractmethod
    async def update_user(self, new_balance : int, user_id : int) -> bool:
        pass
    
    @abstractmethod
    async def get_user(self, user_id : int) -> dict:
        pass
    
    
class RedisDataBase(DataBase):
    def __init__(self, redis_client : Redis):
        self.redis_client = redis_client
    
    async def create_user(self, username, user_id, email, number) -> bool:
        try:
            await self.redis_client.hset(name=f"user:{user_id}",
                                     mapping={
                                         "username" : username,
                                         "email" : email,
                                         "balance" : 0,
                                         "number" : number
                                     })
            
            return True
        except Exception as e:
            return False
       
    
    
    async def delete_user(self, user_id):
        try:
            await self.redis_client.delete(f"user:{user_id}")
        
            return True
        except Exception as e:
            return False
        
        
    async def get_user(self, user_id) -> dict:
        result = await self.redis_client.hgetall(f"user:{user_id}")
        
        return result
    
    async def update_user(self, user_id: int, new_balance=None, email=None) -> bool:
        key = f"user:{user_id}"
        
        try:
            if new_balance is None and email is None:
                return False

            if not await self.redis_client.exists(key):
                return False

            mapping = {}

            if new_balance is not None:
                mapping["balance"] = new_balance

            if email is not None:
                mapping["email"] = email

            await self.redis_client.hset(user_id, mapping=mapping)

            return True
        except Exception as e:
            return False