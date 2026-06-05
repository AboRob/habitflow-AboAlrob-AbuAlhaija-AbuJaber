import json
from datetime import date, timedelta


class HabitTracker:

    def load(self, filepath):
        try:
            with open(filepath, "r") as f:
                data = json.load(f)
            return data["habits"]

        except FileNotFoundError:
            return []

    def save(self, habits, filepath):
        data = {"habits": habits}

        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

        print(f"Habits saved to {filepath}")

        
