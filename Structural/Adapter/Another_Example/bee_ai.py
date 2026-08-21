class BeeAiClient: # adaptee class (new service no modify)

    def __init__(self):
        self.headers = ["id", "date", "final_price"]

        self.rows = [
            [1337, "2026-08-01", 1000.00],
            [1338, "2026-08-02", 4000.50],
            [1339, "2026-08-03", 1500.00]
        ]