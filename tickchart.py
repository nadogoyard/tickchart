import unicorn_binance_websocket_api
import numpy as np

ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
ubwa.create_stream(['trade'], ['ethusdt'], output="UnicornFy")

while True:
    oldest_data_from_stream_buffer = ubwa.pop_stream_data_from_stream_buffer()
    if oldest_data_from_stream_buffer:
        price = np.array(oldest_data_from_stream_buffer.get('price'))
        quantity = np.array(oldest_data_from_stream_buffer.get('quantity'))
        print(f"{price},{quantity}")