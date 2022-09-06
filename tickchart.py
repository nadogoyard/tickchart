import unicorn_binance_websocket_api
import numpy as np
import matplotlib.pyplot as plt
import asyncio

fig = plt.figure()
ax = fig.add_subplot(111)
fig.show()

pricedata = []
timedata = []

def update_graph():
    ax.plot(timedata, pricedata, color='red')
    ax.legend(f"Last price: {pricedata[-1]}")

    fig.canvas.draw()
    plt.pause(0.1)

async def main():
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['trade'], ['ethusdt'], output="UnicornFy")
    while True:
        oldest_data_from_stream_buffer = ubwa.pop_stream_data_from_stream_buffer()
        if oldest_data_from_stream_buffer:
            price = np.array(oldest_data_from_stream_buffer.get('price'))
            trade_time = np.array(oldest_data_from_stream_buffer.get('trade_time'))
            pricedata.append(price)
            timedata.append(trade_time)

            update_graph()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
