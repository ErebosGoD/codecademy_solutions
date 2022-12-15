from collections import namedtuple

country = namedtuple("country", ["name", "capital", "continent"])

france = country("France", "Paris", "Europe")
germany = country("Germany", "Berlin", "Europe")
japan = country("Japan","Tokyo", "Asia")

countries = (japan, france, germany)