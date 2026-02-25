import concurrent.futures
import time


CONCURRENT=True


def countdown():
    n = 100000000
    while n > 0:
        n -= 1
    return True


if __name__ == "__main__":
    start = time.time()
    if not CONCURRENT:
        for i in range(4):
            countdown()
        end = time.time()
    if CONCURRENT:
        with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
            jobs= []
            for i in range(4):
                print("Submission ", i)
                job = executor.submit(countdown)
                jobs.append(job)
        end = time.time()
        for job in jobs:
            print(job.result())
    print("Execution Time: ", end - start)
