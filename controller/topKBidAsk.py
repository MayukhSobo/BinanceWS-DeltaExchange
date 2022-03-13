import json
import numpy as np

class JSONUnmarshall:
    def __init__(self, json_data: str):
        self.json_dict = json.loads(json_data)

    def get_bids_asks(self, what: tuple = ("T", "s", "b", "a")):
        return [self.json_dict["data"][w] for w in what]

    def get_top_k(self, data, k, criteria="volume"):
        if criteria == "volume":
            dataN = np.array(data)
            data_numeric = dataN.astype(np.float64)
            volumes = data_numeric[:, 0] * data_numeric[:, 1]
            index = np.argsort(-volumes)
            return dataN[index[0:k], :]
        else:
            raise NotImplementedError(f"Given criteria {criteria} is not implemented")


def create_handler(json_data, k):
    jm = JSONUnmarshall(json_data)
    time, symbol, buys, asks = jm.get_bids_asks()
    top_asks = jm.get_top_k(asks, k)
    top_buys = jm.get_top_k(buys, k)
    return time, symbol, \
           top_asks.reshape(top_asks.shape[0] * 2).tolist(), \
           top_buys.reshape(top_buys.shape[0] * 2).tolist()
    # print(top_asks.reshape(top_asks.shape[0] * 2))


def FactoryHandler():
    return create_handler
