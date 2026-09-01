# ============================================================
#  Problem B — Fitness tracker
#  Work through the exercises in order.
#  Do NOT import any modules.
# ============================================================


# Exercise 1 — Keep an independent copy
# `weeks` holds [day, step_count] pairs.
#   1) Build `backup`, an INDEPENDENT copy of weeks.
#      Later edits to weeks must NOT change backup.
#   2) In weeks only, correct Tuesday's reading to 5000.
#   3) Print every entry in weeks as "Day: N", one per line.
weeks = [["Mon", 4200], ["Tue", 8100], ["Wed", 6500]]

# your code here


# Exercise 2 — Longest streak
# Write a function named longest_streak(readings, goal) that RETURNS the length
# of the longest group of consecutive readings that are >= goal.
#   longest_streak([5, 1, 6, 7], 5) -> 2
#   longest_streak([1, 2], 9)       -> 0
readings = [4200, 8100, 3000, 9500, 2000, 8800, 9100, 9900, 10200]

# your code here


# Exercise 3 — Group by intensity
# Write a function named by_band(records) that RETURNS a dict mapping a band
# label to a LIST of day names:
#     "low"  for readings below 5000
#     "mid"  for 5000 up to and including 8999
#     "high" for 9000 and above
# Only include bands that actually have days.
#   by_band([("Mon", 100)]) -> {"low": ["Mon"]}
log = [("Mon", 4200), ("Tue", 8100), ("Wed", 6500), ("Thu", 9800), ("Fri", 3300)]

# your code here
