#EsoPrint A unnecicarly stupid way to print the paragaph for fun 
#Griffin Corniea 8-27-2025

import threading
import time

charArray = ['D', 'o', ' ', 'y', 'o', 'u', ' ', 's', 'e', 'e', ' ', 'a', ' ', 'm', 'a', 'n', ' ', 's', 'k', 'i', 'l', 'l', 'f', 'u', 'l', ' ', 'i', 'n', ' ', 'h', 'i', 's', ' ', 'w', 'o', 'r', 'k', '?', '\n', 'H', 'e', ' ', 'w', 'i', 'l', 'l', ' ', 's', 't', 'a', 'n', 'd', ' ', 'b', 'e', 'f', 'o', 'r', 'e', ' ', 'k', 'i', 'n', 'g', 's', ';', '\n', 'h', 'e', ' ', 'w', 'i', 'l', 'l', ' ', 'n', 'o', 't', ' ', 's', 't', 'a', 'n', 'd', ' ', 'b', 'e', 'f', 'o', 'r', 'e', ' ', 'o', 'b', 's', 'c', 'u', 'r', 'e', ' ', 'm', 'e', 'n', '.”', '\n', ' ', ' ', ' ', ' ', ' ', '(', 'P', 'r', 'o', 'v', 'e', 'r', 'b', 's', ' ', '2', '2', ':', '2', '9', ')']


def delayedPrint(ch, delay_ms):
    time.sleep((delay_ms + 1 ) / 100)
    print(ch, end="", flush=True)

threads = []


for i, ch in enumerate(charArray):
    threder = threading.Thread(target=delayedPrint, args=(ch, i))
    threder.start()

