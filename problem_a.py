# ============================================================
#  Problem A — Library circulation
#  Work through the exercises in order.
#  Do NOT import any modules.
# ============================================================


# Exercise 1 — Keep an independent copy
# `shelf` holds [title, copies_available] pairs.
#   1) Build `backup`, an INDEPENDENT copy of shelf.
#      Later edits to shelf must NOT change backup.
#   2) In shelf only, set "Neuromancer" to 0 copies.
#   3) Print every entry in shelf as "Title: N", one per line.
shelf = [["Dune", 3], ["Neuromancer", 1], ["Snow Crash", 4]]

# your code here


# Exercise 2 — Longest run
# Write a function named longest_run(counts) that RETURNS the length of the
# longest group of EQUAL values sitting next to each other.
#   longest_run([1, 2, 2, 3])    -> 2
#   longest_run([4, 4, 4, 1, 4]) -> 3
#   longest_run([])              -> 0
# Do not use itertools.
checkouts = [3, 5, 5, 2, 7, 1, 4, 4, 4, 4]

# your code here


# Exercise 3 — Group by author
# Write a function named by_author(records) that RETURNS a dict mapping each
# author to a LIST of their titles, in the order they appear.
#   by_author([("A", "X"), ("B", "X")]) -> {"X": ["A", "B"]}
records = [
    ("Dune", "Herbert"),
    ("Neuromancer", "Gibson"),
    ("Children of Dune", "Herbert"),
    ("Count Zero", "Gibson"),
    ("Ubik", "Dick"),
]

# your code here
