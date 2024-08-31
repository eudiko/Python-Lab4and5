from abc import ABC, abstractmethod

class DataAnalyzer(ABC):
    @abstractmethod
    def analyze(self, data):
        pass

class AnalysisError(Exception):
    """Custom exception for errors in data analysis."""
    pass

class SubscriberDataAnalyzer(DataAnalyzer):
    def analyze(self, data):
        try:
            if not isinstance(data, dict) or "subscribers" not in data:
                raise KeyError("Data must contain a 'subscribers' key.")
            print(f"Analyzing subscriber data: {data['subscribers']}")
        except KeyError as e:
            print(f"KeyError encountered: {e}")
        except TypeError as e:
            print(f"TypeError encountered: {e}")
        except ValueError as e:
            print(f"ValueError encountered: {e}")
        except AnalysisError as e:
            print(f"Custom AnalysisError encountered: {e}")

class RewardsDataAnalyzer(DataAnalyzer):
    def analyze(self, data):
        try:
            if not isinstance(data, dict) or "rewards" not in data:
                raise KeyError("Data must contain a 'rewards' key.")
            print(f"Analyzing rewards data: {data['rewards']}")
        except KeyError as e:
            print(f"KeyError encountered: {e}")
        except TypeError as e:
            print(f"TypeError encountered: {e}")
        except ValueError as e:
            print(f"ValueError encountered: {e}")
        except AnalysisError as e:
            print(f"Custom AnalysisError encountered: {e}")

analyzers = [SubscriberDataAnalyzer(), RewardsDataAnalyzer()]

data_entries = [
    {"subscribers": ["User1", "User2", "User3"]},
    {"rewards": ["Reward1", "Reward2"]},
    None,
    {"invalid_key": "Invalid data"},
    {"subscribers": "Not a list"}
]

for analyzer in analyzers:
    for data in data_entries:
        try:
            analyzer.analyze(data)
        except Exception as e:
            print(f"Exception during analysis: {e}")
