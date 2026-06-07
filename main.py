from habit_tracker import HabitTracker
from stats_reporter import StatsReporter
from visualizer import Visualizer

def main():

    DATA_FILE = "habits.json"

    ht = HabitTracker()
    sr = StatsReporter()
    viz = Visualizer()

   
    print("[1] Loading habits...")
    habits = ht.load(DATA_FILE)
    print("Found", len(habits), "habits")

    
    print("\n[2] Calculating stats...")
    stats = ht.get_all_stats(habits)

    sr.print_table(stats)

    best = sr.best_habit(stats)
    print("\nBest Habit:", best["name"], f"({best['completion_rate']}%)")

    
    print("\n[3] Saving report...")
    sr.save_json(stats, "habit_report.json")

   
    print("\n[4] Showing charts...")

    viz.completion_chart(stats)
    viz.streak_chart(stats)
    viz.daily_activity(habits)

    print("\nDone!")

if __name__ == "__main__":
    main()
