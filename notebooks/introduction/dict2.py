#!/usr/bin/env python3

city = {"Vienna": 1.741, "London": 8.539, "Paris": 2.244, "Berlin": 3.502, "Zurich": 0.378}

city["Hamburg"] = 1.734

print(city["Hamburg"])

del city["Paris"]

print(city)

