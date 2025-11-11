import asyncio
import aiofiles

async def read_large_file(filename):
    async with aiofiles.open(filename, mode='r') as file:
        async for line in file:
            yield line.strip()
            
async def main():
    async for line in read_large_file("abc.yml"):
        print(line)  # Process each line efficiently


if __name__ == "__main__": 
    asyncio.run(main())
