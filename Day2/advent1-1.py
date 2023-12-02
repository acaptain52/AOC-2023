#!/bin/bash python3
import re

path = "C:\\Users\\acapt\\Python Code\\python\\2023\\Day2\\advent_txt.txt"

with open(path, "r") as file:
    sum = 0
    file_list = file.readlines()
    for line in file_list:
        red = re.findall(r"(\d+) red", line)
        blue = re.findall(r"(\d+) blue", line)
        green = re.findall(r"(\d+) green", line)
        game = re.findall("Game (\d+)", line)
        for x in red:
            if int(x) > 12:
                red = False
        for x in green:
            if int(x) > 13:
                green = False
        for x in blue:
            if int(x) > 14:
                blue = False
        if red and green and blue:
            sum += int(game[0])
    print(sum)
file.close()




    