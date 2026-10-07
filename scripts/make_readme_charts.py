"""Generate the README charts in images/.

The figures are the final results of the analysis, taken from the presentation
(job postings, salaries, survey counts from the Looker Studio long table).
Run from the repository root:  python scripts/make_readme_charts.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib import font_manager

OUT = Path(__file__).resolve().parents[1] / "images"
INK, MUTED, BLUE, ORANGE = "#14213D", "#4A5568", "#2A78D6", "#EB6834"

# Carlito is metric-compatible with Calibri, the font used in the deck
if any("Carlito" in f.name for f in font_manager.fontManager.ttflist):
    plt.rcParams["font.family"] = "Carlito"
plt.rcParams.update({"axes.edgecolor": "#D9DFE8", "text.color": INK, "axes.labelcolor": MUTED,
                     "xtick.color": MUTED, "ytick.color": INK, "font.size": 12})


def hbar(ax, labels, values, color, title, fmt="{:,.0f}"):
    y = range(len(labels))
    ax.barh(y, values, color=color, height=0.68)
    ax.set_yticks(list(y), labels)
    ax.invert_yaxis()
    ax.set_title(title, loc="left", fontsize=14, fontweight="bold", pad=10)
    for i, v in enumerate(values):
        ax.text(v + max(values) * 0.01, i, fmt.format(v), va="center", fontsize=11, color=INK)
    ax.set_xlim(0, max(values) * 1.18)
    ax.xaxis.set_visible(False)
    for side in ("top", "right", "bottom"):
        ax.spines[side].set_visible(False)
    ax.tick_params(axis="y", length=0)


def paired(name, title, current, upcoming):
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.2))
    hbar(axes[0], *zip(*current), BLUE, "Current year: used")
    hbar(axes[1], *zip(*upcoming), ORANGE, "Next year: desired")
    fig.suptitle(title, x=0.01, ha="left", fontsize=17, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT / name, dpi=150, facecolor="white")
    plt.close(fig)


paired("chart_language_trends.png", "Top 10 programming languages: used today vs. desired next year",
       [("JavaScript", 14943), ("SQL", 12602), ("HTML/CSS", 12410), ("TypeScript", 10709), ("Python", 9590),
        ("Bash/Shell", 7244), ("C#", 6340), ("Java", 5982), ("PHP", 4644), ("PowerShell", 3438)],
       [("JavaScript", 11541), ("SQL", 10944), ("TypeScript", 10437), ("HTML/CSS", 10016), ("Python", 8919),
        ("Go", 5661), ("Rust", 5597), ("C#", 5590), ("Bash/Shell", 5582), ("Java", 4048)])

paired("chart_database_trends.png", "Top 10 databases: used today vs. desired next year",
       [("PostgreSQL", 11514), ("MySQL", 8556), ("SQLite", 7021), ("MongoDB", 5930), ("MS SQL Server", 5870),
        ("Redis", 5814), ("MariaDB", 3994), ("Elasticsearch", 3491), ("DynamoDB", 2268), ("Oracle", 1907)],
       [("PostgreSQL", 12193), ("Redis", 6384), ("SQLite", 6295), ("MySQL", 6204), ("MongoDB", 5618),
        ("MS SQL Server", 4345), ("Elasticsearch", 3665), ("MariaDB", 3078), ("DynamoDB", 2154), ("Supabase", 1623)])

fig, axes = plt.subplots(1, 2, figsize=(12, 5.2))
hbar(axes[0], ["Washington DC", "Detroit", "Seattle", "New York", "Los Angeles", "San Francisco", "Austin"],
     [5316, 3945, 3375, 3226, 640, 435, 434], BLUE, "Job postings by city")
hbar(axes[1], ["Swift", "Python", "C++", "JavaScript", "Java", "Go", "R", "C#", "SQL", "PHP"],
     [130801, 114383, 113865, 110981, 101013, 94082, 92037, 88726, 84793, 84727], BLUE,
     "Average annual salary by language", fmt="${:,.0f}")
fig.suptitle("Where the jobs are and what each language pays", x=0.01, ha="left", fontsize=17, fontweight="bold")
fig.tight_layout(rect=(0, 0, 1, 0.94))
fig.savefig(OUT / "chart_jobs_and_salaries.png", dpi=150, facecolor="white")
plt.close(fig)
print("Charts written to", OUT)
