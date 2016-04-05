#!/usr/bin/env python3

city = {"Vienna":1.741, "London":8.539, "Paris":2.244, "Berlin":3.502, "Zurich":0.378}

if city["Vienna"] < city["London"]:
    print("There are")
    print("less people in Vienna")

elif city["Vienna"] == city["London"]:
    print("There are")
    print("the same amount of people in London and in Vienna")

elif city["Vienna"] > city["London"]:
    print("There are")
    print("less people in London")
