from data_loader import DataLoader

class ReportAnalyzer: # Client class (no modify)

    def __init__(self, loader: DataLoader):
        self.loader = loader

    def average(self) -> float:
        data = self.loader.load()

        total = sum(item["final_price"] for item in data)

        return total / len(data)