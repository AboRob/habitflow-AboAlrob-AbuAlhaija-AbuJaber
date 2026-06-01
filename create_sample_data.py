import json
from datetime import date, timedelta
import random

def create_sample_data(filepath="habits.json"):
    today = date.today()

    def random_logs(days_back=30, chance=0.7):
        logs = []
        for i in range(days_back, 0, -1):
            day = today - timedelta(days=i)

            if random.random() < chance:
                logs.append(day.strftime("%Y-%m-%d"))

        return logs

    data = {
        "habits": [
            {
                "name": "Exercise",
                "created": (today - timedelta(days=30)).strftime("%Y-%m-%d"),
                "logs": random_logs(30, 0.65)
            },
            {
                "name": "Reading",
                "created": (today - timedelta(days=30)).strftime("%Y-%m-%d"),
                "logs": random_logs(30, 0.80)
            },
            {
                "name": "Meditation",
                "created": (today - timedelta(days=30)).strftime("%Y-%m-%d"),
                "logs": random_logs(30, 0.50)
            },
            {
                "name": "Study",
                "created": (today - timedelta(days=30)).strftime("%Y-%m-%d"),
                "logs": random_logs(30, 0.75)
            }
        ]
    }

    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Sample habits saved to {filepath}")

if __name__ == "__main__":
    create_sample_data()