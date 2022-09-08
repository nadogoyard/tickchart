import unicorn_binance_websocket_api
import numpy as np
import matplotlib.pyplot as plt
import asyncio

fig = plt.figure()
ax = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
fig.show()

best_bid = []
best_ask = []

def update_graph():
    ax.plot(best_bid, drawstyle='steps-pre', color='green')
    ax.plot(best_ask, drawstyle='steps-pre', color='red')
    ax2.plot(np.subtract(best_ask, best_bid))

    fig.canvas.draw()
    plt.pause(0.001)

async def main():
    ubwa = unicorn_binance_websocket_api.BinanceWebSocketApiManager(exchange="binance.com")
    ubwa.create_stream(['bookTicker'], ['ethusdt'], output="UnicornFy")
    while True:
        oldest_data_from_stream_buffer = ubwa.pop_stream_data_from_stream_buffer(mode='LIFO')
        if oldest_data_from_stream_buffer:
            best_bid_price = np.array(oldest_data_from_stream_buffer.get('best_bid_price'))
            best_ask_price = np.array(oldest_data_from_stream_buffer.get('best_ask_price'))

            if best_bid_price == None:
                pass
            else:
                best_bid.append(round(float(best_bid_price), 3))

            if best_ask_price == None:
                pass
            else:
                best_ask.append(round(float(best_ask_price), 3))

            update_graph()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
