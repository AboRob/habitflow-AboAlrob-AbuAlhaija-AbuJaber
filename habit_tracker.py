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

    def calculate_streak(self, habit):

        logs_set = set(habit["logs"])

        streak = 0
        current = date.today()

        while current.strftime("%Y-%m-%d") in logs_set:
            streak += 1
            current -= timedelta(days=1)

        return streak

    def get_all_stats(self, habits):

        today = date.today()
        results = []

        for habit in habits:

            logs_set = set(habit["logs"])

            last_30 = [
                (today - timedelta(days=i)).strftime("%Y-%m-%d")
                for i in range(30)
            ]

            completed_30 = sum(1 for d in last_30 if d in logs_set)

            rate = round(completed_30 / 30 * 100, 1)

            results.append({
                "name": habit["name"],
                "total_logs": len(habit["logs"]),
                "current_streak": self.calculate_streak(habit),
                "completion_rate": rate
            })

        return results