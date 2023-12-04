import re

greedyRegex = re.compile(r"(Ha){3,5}")
greedy = greedyRegex.search("HaHaHaHaHa")
print(greedy.group())

nonGreedyRegex = re.compile(r"(Ha){3,5}?")
nonGreedy = nonGreedyRegex.search("HaHaHaHaHa")
print(nonGreedy.group())
