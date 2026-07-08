from concurrent.futures import ThreadPoolExecutor, as_completed

from scanner.tcp_scan import TCPScanner
from scanner.port_utils import parse_ports
from scanner.events import ProgressEvent, ResultEvent


class ScanEngine:

    def __init__(
        self,
        workers=200,
        progress_callback=None,
        result_callback=None,
    ):

        self.workers = workers
        self.progress_callback = progress_callback
        self.result_callback = result_callback

        self.scanner = TCPScanner()

        self._cancel = False

    def stop(self):
        self._cancel = True

    def scan(self, target, port_text):

        self._cancel = False

        ports = parse_ports(port_text)

        results = []

        with ThreadPoolExecutor(max_workers=self.workers) as executor:

            futures = {
                executor.submit(
                    self.scanner.scan,
                    target,
                    port
                ): port

                for port in ports
            }

            completed = 0
            total = len(futures)

            for future in as_completed(futures):

                if self._cancel:
                    break

                completed += 1

                result = future.result()

                if result:

                    results.append(result)

                    if self.result_callback:

                        self.result_callback(
                            ResultEvent(result)
                        )

                if self.progress_callback:

                    self.progress_callback(
                        ProgressEvent(
                            completed,
                            total
                        )
                    )

        results.sort(key=lambda r: r.port)

        return results