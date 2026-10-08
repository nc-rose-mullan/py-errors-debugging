import time

while True:
    try:
        time.sleep(1)
        print("still here")
    except ValueError:
        pass
