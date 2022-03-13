from socketClinet.WSocket import TickerTrack
from controller.topKBidAsk import FactoryHandler
from writer.writer import FactoryCSVWriter
import asyncio

if __name__ == "__main__":
    uri = "wss://fstream.binance.com/stream?streams=btcusdt@depth"
    loop = asyncio.get_event_loop()
    task = TickerTrack(loop, uri, interval=10, topK=5, handler=FactoryHandler,
                       writer=FactoryCSVWriter, file_name="test.log.csv")
    loop.run_until_complete(task)