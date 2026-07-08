"""
PortVision AI
Scan Controller

Coordinates the GUI and Scan Engine.
"""

from threading import Thread

from scanner.scan_engine import ScanEngine


class ScanController:

    def __init__(
        self,
        progress_callback=None,
        result_callback=None,
        finished_callback=None,
    ):

        self.engine = ScanEngine(
            progress_callback=progress_callback,
            result_callback=result_callback,
        )

        self.finished_callback = finished_callback

        self.thread = None

    def start_scan(
        self,
        target,
        ports,
    ):

        self.thread = Thread(
            target=self._run,
            args=(target, ports),
            daemon=True,
        )

        self.thread.start()

    def _run(
        self,
        target,
        ports,
    ):

        results = self.engine.scan(
            target,
            ports,
        )

        if self.finished_callback:
            self.finished_callback(results)

    def stop_scan(self):

        self.engine.stop()