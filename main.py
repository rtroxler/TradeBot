import tkinter as tk
import logging

from bitmex import get_contracts

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
    logger.info("")
    logger.info("")
    logger.info("Starting TradeBot application, initializing . . .")
    logger.info("Event loop start.")

    bitmex_contracts = get_contracts()

    root = tk.Tk()

    row = 0
    col = 0
    for contract in bitmex_contracts:
        label_widget = tk.Label(root, text=contract)
        label_widget.grid(row=row, column=col)

        if row == 4:
            row = 0
            col += 1
        else:
            row += 1

    root.mainloop()

