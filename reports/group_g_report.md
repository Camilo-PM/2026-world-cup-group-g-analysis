# FIFA World Cup 2026 - Group G Analysis

## Project Overview

This project analyzes the recent form of the national teams in Group G of the FIFA World Cup 2026.

The analysis is based on each team's most recent available matches, using data collected from local FBref HTML files.

Teams analyzed:

Belgium, New Zealand, Egypt, Iran

---

## Key Findings

- Highest Power Score: Belgium with 24.21.
- Best attacking record: Belgium with 35.0 goals scored.
- Best defensive record: Egypt with 5.0 goals conceded.
- Best recent form: Egypt with 23 points.

---

## Team Summary

| Team | Matches | Wins | Draws | Losses | GF | GA | GD | Points Form | Form Index | Power Score |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Belgium | 10 | 6 | 4 | 0 | 35.0 | 10.0 | 25.0 | 22 | 73.33 | 24.21 |
| New Zealand | 9 | 5 | 1 | 3 | 31.0 | 7.0 | 24.0 | 16 | 59.26 | 20.94 |
| Egypt | 10 | 7 | 2 | 1 | 17.0 | 5.0 | 12.0 | 23 | 76.67 | 17.87 |
| Iran | 10 | 6 | 2 | 2 | 20.0 | 10.0 | 10.0 | 20 | 66.67 | 15.91 |


---

## Visualizations

The project generates the following visualizations:

- ranking_form.png
- goal_difference.png
- attack_vs_defense.png

These charts are saved in:

reports/figures/

---

## Notes

New Zealand has 9 matches available in the collected dataset, while the other teams have 10. This should be considered when comparing form and performance indicators.

---

## Methodology

1. Local HTML files are collected from FBref.
2. Match data is extracted and cleaned with Python.
3. Team-level metrics are calculated.
4. Visualizations are generated with Matplotlib.
5. A Markdown report is created automatically.
