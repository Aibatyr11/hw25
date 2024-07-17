import threading
import time

def file(filename):
    time.sleep(1)
    with open(filename, 'w') as f:
        f.write('ffff')

def run():
    startt = time.time()
    for i in range(10): # 100
        file(f"file{i}.txt")
    endd = time.time()
    print(f"Sequential: {endd - startt} sec")

def rrun():
    threads = []
    startt = time.time()
    for i in range(10): #100
        thread = threading.Thread(target=file, args=(f"file{i}.txt",))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    endd = time.time()
    print(f"Multithreaded: {endd - startt} sec")

if __name__ == "__main__":
    run()
    rrun()
