from dataclasses import dataclass

@dataclass
class ProgressEvent:
    scanned: int
    total: int

    @property
    def percent(self):
        if self.total == 0:
            return 0.0
        return self.scanned / self.total


@dataclass
class ResultEvent:
    result: object