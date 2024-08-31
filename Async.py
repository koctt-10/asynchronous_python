import requests
from time import time



def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r


def write_file(responce):
    filename = responce.url.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(responce.content)
        
        
def main():
    t0 = time()
    
    url = 'https://loremflicker.com/320/240'
    
    for i in range(10):
        write_file(get_file(url))
            
    print(time() - t0)
        

#if __name__ == '__main__':
#    main()
    
    
##########################################################
import asyncio
import aiohttp


def write_image(data):
    filename = 'file-{}.jpeg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as responce:
        data = await responce.read()
        write_image(data)
        
        
async def main2():
    url = 'https://loremflicker.com/320/480'
    tasks = []
    
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)
            
        await asyncio.gather(*tasks)
        
        
if __name__ == '__main__':
    t0 = time()
    asyncio.run(main2())
    print(time() - t0)