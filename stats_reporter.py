def save_json(self, stats, filepath):

        with open(filepath, "w") as f:
            json.dump(stats, f, indent=2)

        print(f"Report saved: {filepath}")
