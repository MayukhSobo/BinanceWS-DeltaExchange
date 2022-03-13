import asyncio
import websockets


class TickerTrack:
    def __new__(cls, _loop, uri, handler, writer, topK=10, file_name=None, interval=1):
        this = super().__new__(cls)
        this.interval = interval
        this.uri = uri
        this.task = _loop.create_task(this.run())
        this.handler = handler
        this.writer = writer
        this.file_name = file_name
        this.topK = topK

        return this.task

    async def run(self):
        async with websockets.connect(self.uri) as self.ws:
            while True:
                await self.do(self.handler, self.writer)
                await asyncio.sleep(self.interval)

    async def do(self, handler, writer=None):
        data = await self.ws.recv()
        res = handler()(data, self.topK)
        # print(res)
        if self.writer and self.file_name:
            print(res)
            await writer()(res, self.file_name)
            # asyncio.run(writer()(res, self.file_name))

    def stop(self):
        self.task.cancel()
