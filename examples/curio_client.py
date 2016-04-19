# hello.py
import curio
from hyper.http20.connection import HTTP20Connection

async def test_http20():
    conn = HTTP20Connection('http2bin.org:443')
    await conn.request('GET', '/get')
    resp = await conn.get_response()
    print(await resp.read())

if __name__ == '__main__':
    kernel = curio.Kernel()
    kernel.run(test_http20())
