from habit_tracker import HabitTracker

def main():
    ht = HabitTracker()

    habits = ht.load("habits.json")

    print("Loaded habits:")
    for h in habits:
        print("-", h["name"])

