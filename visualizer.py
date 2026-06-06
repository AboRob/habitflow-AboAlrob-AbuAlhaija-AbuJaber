import matplotlib.pyplot as plt
from datetime import date, timedelta


class Visualizer:

    def completion_chart(self, stats):
        names = [s["name"] for s in stats]
        rates = [s["completion_rate"] for s in stats]

        colors = [
            "green" if r >= 70 else "orange" if r >= 40 else "red"
            for r in rates
        ]

        fig, ax = plt.subplots(figsize=(9, 5))
        ax.barh(names, rates, color=colors, edgecolor="black")

        ax.axvline(x=70, color="green", linestyle="--", alpha=0.6, label="70% target")

        ax.set_xlim(0, 110)
        ax.set_xlabel("Completion Rate (%)")
        ax.set_title("30-Day Habit Completion Rates")
        ax.legend()

       
        for i, r in enumerate(rates):
            ax.text(r + 1, i, f"{r}%", va="center", fontsize=10)

        plt.tight_layout()
        plt.show()

    def streak_chart(self, stats):
        names = [s["name"] for s in stats]
        streaks = [s["current_streak"] for s in stats]

        colors = ["gold" if s >= 7 else "steelblue" for s in streaks]

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.bar(names, streaks, color=colors, edgecolor="black")

        ax.axhline(y=7, color="gold", linestyle="--", alpha=0.7, label="7-day milestone")

        ax.set_ylabel("Current Streak (days)")
        ax.set_title("Current Habit Streaks")
        ax.legend()

       
        for i, s in enumerate(streaks):
            ax.text(i, s + 0.1, str(s), ha="center", fontsize=11)

        plt.tight_layout()
        plt.show()

    def daily_activity(self, habits):
        today = date.today()

        
        dates = [
            (today - timedelta(days=i)).strftime("%Y-%m-%d")
            for i in range(29, -1, -1)
        ]

        daily_counts = []
        for d in dates:
            count = sum(1 for h in habits if d in h["logs"])
            daily_counts.append(count)

        fig, ax = plt.subplots(figsize=(12, 5))

        ax.plot(range(30), daily_counts, marker="o", linewidth=2)
        ax.fill_between(range(30), daily_counts, alpha=0.2)

        ax.set_title("Daily Habit Completions (Last 30 Days)")
        ax.set_xlabel("Day (0 = 30 days ago, 29 = today)")
        ax.set_ylabel("Habits Completed")

        ax.set_ylim(0, len(habits) + 1)

   
        ax.axhline(y=len(habits), color="green", linestyle="--", alpha=0.5, label="Perfect day")

        ax.legend()
        plt.tight_layout()
        plt.show()
