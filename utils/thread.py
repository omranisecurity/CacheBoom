import threading

class ThreadManager:
    def __init__(self, max_threads):
        self.max_threads = max_threads
        self.lock = threading.Lock()
        self.active_threads = 0

    def run_task(self, task, *args, **kwargs):
        with self.lock:
            while self.active_threads >= self.max_threads:
                self.lock.release()
                threading.Event().wait(0.1)
                self.lock.acquire()
            self.active_threads += 1

        try:
            task(*args, **kwargs)
        finally:
            with self.lock:
                self.active_threads -= 1

    def wait_for_completion(self):
        with self.lock:
            while self.active_threads > 0:
                self.lock.release()
                threading.Event().wait(0.1)
                self.lock.acquire()