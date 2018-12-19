import asyncio
import time
def get_time():
    dt = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
    return dt
async def do_some_work(x):
    print("Waiting " + str(x))
    print(get_time())
    await asyncio.sleep(x)
    print(get_time())

def done_callback(futu):
    print(get_time())
    print('Done')



loop = asyncio.get_event_loop()
# loop.run_until_complete(do_some_work(2))
# futu = asyncio.ensure_future(do_some_work(3))
# futu.add_done_callback(done_callback)
# loop.run_until_complete(futu)

# loop.run_until_complete(asyncio.gather(do_some_work(1), do_some_work(3)))
# 多个协程
futus = [asyncio.ensure_future(do_some_work(1)),
             asyncio.ensure_future(do_some_work(3))]
coros = [do_some_work(1), do_some_work(3)]
loop.run_until_complete(asyncio.gather(*coros))