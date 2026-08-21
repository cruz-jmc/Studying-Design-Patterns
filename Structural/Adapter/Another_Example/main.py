from bee_ai import BeeAiClient
from bee_ai_adapter import BeeAiAdapter
from report_analyzer import ReportAnalyzer
# Import all pieces we need


def main():

    client = BeeAiClient()

    adapter = BeeAiAdapter(client)

    analyzer = ReportAnalyzer(adapter)

    print(analyzer.average())


if __name__ == "__main__":
    main()