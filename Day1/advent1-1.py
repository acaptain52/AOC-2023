#!/bin/bash

path = "C:\\Users\\acapt\\Python Code\\python\\2023\\Day1\\advent_txt.txt"

with open(path, "r") as file:
    num_list = []
    file_list = file.readlines()
    for line in file_list:         #This loop creates a list of numbers from each line
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
        elif len(item) >= 2:
            new_num = item[0] + item[-1]
            sum += int(new_num)
    print(sum)
file.close()


    