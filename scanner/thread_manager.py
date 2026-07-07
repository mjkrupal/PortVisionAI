from concurrent.futures import ThreadPoolExecutor


class ThreadManager:

    def __init__(self, workers=100):

        self.workers = workers

    def run(self, func, target, ports):

        results = []

        with ThreadPoolExecutor(
            max_workers=self.workers
        ) as executor:

            futures = [
                executor.submit(
                    func,
                    target,
                    port
                )

                for port in ports
            ]

            for future in futures:

                result = future.result()

                if result:

                    results.append(result)

        return results