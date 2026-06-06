from habit_tracker import HabitTracker
from stats_reporter import StatsReporter

def main():
    ht = HabitTracker()
    sr = StatsReporter()

    habits = ht.load("habits.json")

    stats = ht.get_all_stats(habits)

    print("\nHabit Statistics:\n")
    sr.print_table(stats)

    best = sr.best_habit(stats)
    print("\nBest Habit:", best["name"], best["completion_rate"], "%")

if __name__ == "__main__":
    main()
