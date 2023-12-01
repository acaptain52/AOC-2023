#!/bin/bash

path = "C:\\Users\\acapt\\Python Code\\python\\2023\\Day1\\advent_txt.txt"

with open(path, "r") as file:
    num_list = []
    new_list = []
    new_list2 = []
    num_dict_combined = {"nineight": "98", "sevenine": "79", "fiveight": "58", "eighthree": "83", "threeight": "38", "eightwo": "82", "twone": "21", "oneight": "18"}
    num_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    file_list = file.readlines()
    #Begin day 2
    for line in file_list:          #This loop replaces combined number-words, like oneight, with numbers
        for k in num_dict_combined.keys():
            if k in line:
                line = line.replace(k, num_dict_combined[k])
        new_list.append(line)
    for line in new_list:           #This look replaces left over single number words with numbers
        for k in num_dict.keys():
            if k in line:
                line = line.replace(k, num_dict[k])
        new_list2.append(line)
    #End day 2

    for line in new_list2:         #This loop creates a list of numbers from each line
        num = ""
        for i in range(len(line)):
            try:
                int(line[i])
                num += line[i]
            except:
                pass
        num_list.append(num)
    sum = 0
    for item in num_list:
        if len(item) == 1:
            new_num = item * 2
            sum += int(new_num)
            #print(new_num, sum)
        elif len(item) >= 2:
            new_num = item[0] + item[-1]
            sum += int(new_num)
            #print(new_num, sum)
    print(sum)
file.close()