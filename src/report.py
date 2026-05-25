import sys
from pathlib import Path

import pandas as pd

sys.path.append(str(Path(__file__).resolve().parents[1]))

from configs.config import FINAL_DIR, BASE_DIR


REPORTS_DIR = BASE_DIR / "reports"


def main():
    input_path = FINAL_DIR / "group_f_summary.csv"

    if not input_path.exists():
        print(f"No existe el archivo: {input_path}")
        return

    df = pd.read_csv(input_path)

    leader = df.iloc[0]

    report = f"""# Group G Team Performance Analysis - FIFA World Cup 2026

## Project Overview

This project analyzes the recent performance of the national teams in Group G of the FIFA World Cup 2026.

The analysis is based on each team's last 10 matches and focuses on form, attacking performance, defensive performance, and goal difference.

## Teams Analyzed

{", ".join(df["team"].tolist())}

## Key Findings

The team with the strongest recent form is **{leader["team"]}**, with **{leader["Points_Form"]} points** from the last 10 matches.

{leader["team"]} also recorded a goal difference of **{leader["Goal_Difference"]}**, scoring **{leader["Goals_For"]}** goals and conceding **{leader["Goals_Against"]}**.

## Summary Table

{df.to_markdown(index=False)}

## Visualizations

The project includes the following visualizations:

- Recent form ranking
- Goal difference comparison
- Attack vs defense comparison

## Data Notes

The data was collected from locally saved FBref HTML files. This method was used to avoid request blocks and improve reproducibility.

## Output Files

- `data/processed/group_f_last_10_clean.csv`
- `data/final/group_f_summary.csv`
- `reports/figures/ranking_form.png`
- `reports/figures/goal_difference.png`
- `reports/figures/attack_vs_defense.png`
"""

    output_path = REPORTS_DIR / "group_f_report.md"
    output_path.write_text(report, encoding="utf-8")

    print(f"Reporte guardado en: {output_path}")


if __name__ == "__main__":
    main()

