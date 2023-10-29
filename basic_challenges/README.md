<img align='right' src='https://user-images.githubusercontent.com/5713670/87202985-820dcb80-c2b6-11ea-9f56-7ec461c497c3.gif' width='100'><!--@schambig-->

[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
![GitHub last commit](https://img.shields.io/github/last-commit/schambig/python_workout)

# Basic Python Challenges<!--@schambig-->


[Description](#description) • [File Structure](#file-structure)

---

## Description<!--@schambig-->

Python is an interpreted, high-level, general-purpose programming language, it has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.


## File structure<!--@schambig-->

This table contains a brief description of the working files of the project, click on the names to get the source code:

* All these files were interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.10)

| Filename | Description/Task |
| --- | --- |
| <pre>[1-value_type.py](1-value_type.py)</pre><!--@schambig--> | In this challenge, you will find a function called `found_type` that takes a parameter called `value`. Your task is to determine the data type of the value parameter and return it from the `found_type` function.|
```
Input:
found_type(1)
found_type("Salo")
found_type(True)

Output:
'int'
'str'
'bool'
```

| Filename | Description/Task |
| --- | --- |
| <pre>[2-caculate_tip.py](2-caculate_tip.py)</pre><!--@schambig--> | In this challenge, you will need to calculate the tip that restaurant customers should leave based on their bill. The `calculate_tip` function will receive two parameters: `bill_amount`, representing the total cost of what was consumed, and `tip_percentage`, representing the percentage of the tip to leave. Both values will be of type float and will always be positive, including 0. The function should return the tip amount as a number.|
```
Input: calculate_tip(100, 10)
Output: 10

Input: calculate_tip(1524.33, 25)
Output: 381.08
```

| Filename | Description/Task |
| --- | --- |
| <pre>[3-is_leap_year.py](3-is_leap_year.py)</pre><!--@schambig--> | In this Python challenge, you need to create the logic for the `is_leap_year` function, which determines whether a year is a leap year or not. A year is a leap year if it meets the following conditions:<br> • It is divisible by 4, but not by 100.<br> • If it is divisible by 100, it must also be divisible by 400.<br> The `is_leap_year` function takes a single parameter, which is the year to evaluate. It should return True if the year is a leap year or False if it is not. Keep in mind that the function should be able to handle non-integer or negative values. |
```
Input: is_leap_year(2000)
Output: True

Input: is_leap_year(-2024)
Output: False

Input: is_leap_year(1984.25)
Output: False
```

| Filename | Description/Task |
| --- | --- |
| <pre>[4-print_triangle.py](4-print_triangle.py)</pre><!--@schambig--> | In this challenge, you need to draw an triangle using loops. You will receive two parameters: `size` and `char`, which define the number of rows the triangle will have and the character with which the triangle should be constructed, respectively. Additionally, the triangle should be centered, which means the same number of characters should be on both sides. Remember that to create a line break, you should use "\n". Don't forget to remove it from the last part, and you should return all of this in a variable. |
```
Input: printTriangle(3, "*")
Output:
  *
 ***
*****

Input: printTriangle(6, "$")
Output:
     $
    $$$
   $$$$$
  $$$$$$$
 $$$$$$$$$
$$$$$$$$$$$
```

| Filename | Description/Task |
| --- | --- |
| <pre>[]()</pre><!--@schambig--> |  |
```
```


<!-- <pre><br><br></pre> • <br>•-->


<p align="center">
  <img alt="schambig" src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
