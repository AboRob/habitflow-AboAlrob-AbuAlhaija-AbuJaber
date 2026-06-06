import matplotlib.pyplot as plt
from datetime import date, timedelta

class Visualizer:

    def completion_chart(self, stats):
        names = [s["name"] for s in stats]
        rates = [s["completion_rate"] for s in stats]
        colors = []

        for r in rates:
            if r >= 70:
                colors.append("green")
            elif r >= 40:
                colors.append("orange")
            else:
                colors.append("red")
        
        fig, ax = plt.subplots(figsize=(9, 5))
        ax.barh(names, rates, color=colors, edgecolor="black")
        ax.axvline(x=70, color="green", linestyle="--", alpha=0.6, label="70% target")
        ax.set_xlim(0, 110)
        ax.set_xlabel("Completion Rate (%)")
        ax.set_title("30-Day Habit Completion Rates")
        ax.legend()
        plt.show()
