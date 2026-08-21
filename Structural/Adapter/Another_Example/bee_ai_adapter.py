from data_loader import DataLoader


class BeeAiAdapter(DataLoader): # Adapter Class

    def __init__(self, client):
        self.client = client

    def load(self) -> list[dict]:

        return [
            dict(zip(self.client.headers, row)) # -> Translator
            for row in self.client.rows
        ]