import asyncio
import aiohttp


async def simulate_io():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as resp:
            await resp.text()


async def coro(name):
    await simulate_io()
    print(f'{name}-1')
    await simulate_io()
    print(f'{name}-2')


async def main():
    await asyncio.gather(coro('A'), coro('B'))

loop = asyncio.get_event_loop()
loop.run_until_complete(main())