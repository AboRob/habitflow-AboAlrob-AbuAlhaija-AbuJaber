import json


class StatsReporter:

    def print_table(self, stats):

        print("  Habit           Streak   30-Day Rate   Total Logs")
        print("  --------------- -------- ------------ ------------")

        for s in stats:
            print(f"  {s['name']:<15} {s['current_streak']:>7}d {s['completion_rate']:>10}% {s['total_logs']:>12}")

    def best_habit(self, stats):

        return max(stats, key=lambda s: s["completion_rate"])

    def save_json(self, stats, filepath):

        with open(filepath, "w") as f:
            json.dump(stats, f, indent=2)

        print(f"Report saved: {filepath}")
