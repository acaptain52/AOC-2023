#!/bin/bash python3
import re

path = "C:\\Users\\acapt\\Python Code\\python\\2023\\Day2\\advent_txt.txt"

with open(path, "r") as file:
    sum = 0
    file_list = file.readlines()
    #Create list of reds, greens and blues for each line
    for line in file_list:
        red = re.findall(r"(\d+) red", line)
        blue = re.findall(r"(\d+) blue", line)
        green = re.findall(r"(\d+) green", line)
        game = re.findall("Game (\d+)", line)
    
        #Find largest red
        while len(red) > 1:
            if int(red[0]) > int(red[1]):
                red.remove(red[1])
            else:
                red.remove(red[0])

        #Find largest green
        while len(green) > 1:
            if int(green[0]) > int(green[1]):
                green.remove(green[1])
            else:
                green.remove(green[0])

        #Find largest blue
        while len(blue) > 1:
            if int(blue[0]) > int(blue[1]):
                blue.remove(blue[1])
            else:
                blue.remove(blue[0])

        #Add product of red, geen, and blue to sum
        sum += (int(red[0]) * int(green[0]) * int(blue[0]))
    
    print(sum)
file.close()




    