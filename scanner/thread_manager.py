from concurrent.futures import ThreadPoolExecutor


class ThreadManager:

    def __init__(self, workers=200):

        self.pool = ThreadPoolExecutor(
            max_workers=workers
        )