import asyncio
async def do_some_work(loop, x):
    print('Waiting ' + str(x))
    await asyncio.sleep(x)
    print('Done')

def done_callback(loop, futu):
    loop.stop()

loop = asyncio.get_event_loop()

futus = asyncio.gather(do_some_work(loop, 1), do_some_work(loop, 3))
futus.add_done_callback(functools.partial(done_callback, loop))

loop.run_forever()