import asyncio


async def hello():
    print("Hello world!")
    r = await asyncio.sleep(1)
    print("Hello again!")
    
asyncio.run(hello())


async def fetch_data():
    # 模拟网络请求
    await asyncio.sleep(2)
    return {"data": "example"}

async def process():
    result = await fetch_data()  # 等待 fetch_data 完成
    print(f"Received: {result}")
    
asyncio.run(process())


async def example():
    print("Start")
    result = await asyncio.sleep(1, "result")  # 挂起点
    print(f"Resumed with: {result}")  # 恢复点
    return "done"

asyncio.run(example())


async def get_user_id():
    await asyncio.sleep(0.1)
    return 123

async def get_user_info(user_id):
    await asyncio.sleep(0.2)
    return {"name": "Alice", "profile_id": 456}

async def get_user_profile(profile_id):
    await asyncio.sleep(0.3)
    return {"age": 25, "city": "Beijing"}

async def fetch_user():
    # 模拟异步操作链
    user_id = await get_user_id()
    user_info = await get_user_info(user_id)
    user_profile = await get_user_profile(user_info["profile_id"])
    return user_profile

res = asyncio.run(fetch_user())
print(res)

