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

        
    def add_habit(self, habits, name):

        for habit in habits:
            if habit["name"].lower() == name.lower():
                raise ValueError("Habit already exists")

        new_habit = {
            "name": name,
            "created": date.today().strftime("%Y-%m-%d"),
            "logs": []
        }

        habits.append(new_habit)

        return habits


    def log_today(self, habits, habit_name):

        today = date.today().strftime("%Y-%m-%d")

        for habit in habits:

            if habit["name"].lower() == habit_name.lower():

                if today not in habit["logs"]:
                    habit["logs"].append(today)

                return habits

        raise ValueError("Habit not found")

