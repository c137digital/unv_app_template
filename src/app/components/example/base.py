import asyncio


async def main():
    counter = 1
    while True:
        print(f'Echo from example component. Counter: {counter}')
        await asyncio.sleep(1)

        if counter == 5:
            break

        counter += 1

    print('Main loop executed')
