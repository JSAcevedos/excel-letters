# EXCEL TO LETTERS

In this exercise, we need to find the column number representation of a set of letters in an Excel sheet. In Excel, the first column is represented by the letter 'A', the second column by 'B', and so on. For example, 'A' corresponds to column number 1, 'Z' corresponds to column number 26, 'AA' corresponds to column number 27, and so on.

The program should be able to convert a column number to its corresponding letter representation, or convert a set of letters to its corresponding column number. To solve this problem, we can treat the letters as a set of numbers, where each position represents the units, tens, and hundreds place, but instead of using a decimal system from 0 to 9, we use a system from 1 to 26. By applying this logic, we can convert both ways: from letters to numbers and from numbers to letters.

**Input**
The input can be either a column number or a set of letters representing a column in Excel.

**Output**
The output will depend on the input. If the input is a column number, the program should print its corresponding letter representation. If the input is a set of letters, the program should print its corresponding column number.

**Examples**

Example 1

Input:

Column Number: 5

Output:

Column Representation: E

Example 2

Input:

Column Letters: AB

Output:

Column Number: 28

Example 3

Input:

Column Letters: XFD

Output:

Column Number: 16384

Please note: The program should handle inputs within the valid range of Excel column representation (i.e., column numbers should be positive integers, and column letters should consist of uppercase letters only).
