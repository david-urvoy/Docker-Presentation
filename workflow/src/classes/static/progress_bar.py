from time import sleep

def progress_bar(delay = 8, length = 10):
    for i in range(0, length):
        print("[{loaded}>{not_loaded}]".format(loaded = ('=' * i), not_loaded = (' ' * (length - 1 - i))), end = "\r")
        sleep(delay / length)
    print()
