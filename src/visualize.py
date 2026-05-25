import sys
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from configs.config import FINAL_DIR, BASE_DIR


FIGURES_DIR = BASE_DIR / "reports" / "figures"


def main():
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    input_path = FINAL_DIR / "group_f_summary.csv"

    if not input_path.exists():
        print(f"No existe el archivo: {input_path}")
        return

    df = pd.read_csv(input_path)

    df = df.sort_values("Points_Form", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(df["team"], df["Points_Form"])
    plt.title("Group G - Recent Form Ranking")
    plt.xlabel("Points in Last 10 Matches")
    plt.ylabel("Team")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "ranking_form.png", dpi=300)
    plt.close()

    df = df.sort_values("Goal_Difference", ascending=True)

    plt.figure(figsize=(10, 6))
    plt.barh(df["team"], df["Goal_Difference"])
    plt.title("Group G - Goal Difference")
    plt.xlabel("Goal Difference")
    plt.ylabel("Team")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "goal_difference.png", dpi=300)
    plt.close()

    plt.figure(figsize=(8, 6))
    plt.scatter(df["Avg_Goals_For"], df["Avg_Goals_Against"])

    for _, row in df.iterrows():
        plt.text(
            row["Avg_Goals_For"],
            row["Avg_Goals_Against"],
            row["team"],
            fontsize=9
        )

    plt.title("Group G - Attack vs Defense")
    plt.xlabel("Average Goals For")
    plt.ylabel("Average Goals Against")
    plt.tight_layout()
    plt.savefig(FIGURES_DIR / "attack_vs_defense.png", dpi=300)
    plt.close()

    print(f"Gráficos guardados en: {FIGURES_DIR}")


if __name__ == "__main__":
    main()

