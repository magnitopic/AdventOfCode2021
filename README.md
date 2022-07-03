# Advent of code 2021

Coding challenges, one for every day of December.

Challenges can be solved using whatever programming language you wish.

🇪🇸 Spanish version of these challenges can be found [here](https://github.com/financieras/AdventOfCode2021/blob/master/retos.ipynb).

# Challenges

## Day1

### Divisors of a series of numbers

-   The user specifies the range of numbers, indicating the start and end of the series
-   Calculate the divisors of all the numbers in that series
-   The program prints, next to each number in the range, all the divisors that each of those numbers has

**Example**

-   Bettwen 100 and 110

    -   100 -> [1,2,4,5,10,20,25,50,100]
    -   101 -> [1,101]
    -   102 -> [1,2,3,6,17,34,51,102]
    -   103 -> [1,103]
    -   104 -> [1,2,4,8,13,26,52,104]
    -   105 -> [1,3,5,7,15,21,35,105]
    -   106 -> [1,2,53,106]
    -   107 -> [1,107]
    -   108 -> [1,2,3,4,6,9,12,18,27,36,54,108]
    -   109 -> [1,109]
    -   110 -> [1,2,5,10,11,22,55,110]

## Day2

### Character frequency in a book

-   Analyze the frequency of all the characters in a book
    -   I'll be using: Frankenstein; Or, The Modern Prometheus by Mary Wollstonecraft Shelley
    -   It can be obtained freely from [proyect Guttember](https://www.gutenberg.org/ebooks/84).
    -   Or [from this repository](https://raw.githubusercontent.com/magnitopic/AdventOfCode2021/master/Frankenstein.txt) in txt format

## Day3

### Find the different number

-   Generate an array of integers with a random length between 3 and 15
-   The integers of the array are random between -99 and +99
-   Every number of the array will be odd or even, except for one, that will be the odd one out
-   Define a function that recives the generated array as an argument
-   The funtion returns the odd one out
-   Print the array and the retured value

**Example**

-   [2, 4, 0, 100, 4, 11, 2602, 36]
    -   Returned value should be 11, since it is the only odd value in the array
-   [160, 3, 1719, 19, 11, 13, -21]
    -   Returned value should be 160, since it is the only even number

## Day 4

### Sum of odd numbers in a triangle

-   Using a triangle of odd number like this one:

```
				1
			3		5
		7		9		11
	13		15		17		19
21		23		25		27		29
```

-   User is asked how many rows the triangle should have
-   The program generates each row and passes it as an argument to a function that sums its values

**Example**

-   1st row -> 1
-   2st row -> 3 + 5 = 8
-   3st row -> 7 + 9 + 11 = 27

## Day5

### Distribute text into diferent rows

-   Create a function that receives two arguments:
    -   A string that is not empty
    -   An integer between 1 and the length of the string
-   The function must print the string with only the intiger number of characters per row

**Example**

-   Inputs:
    -   "ABCDEFG @HIJKLIMNOQRSTUVWXYZ"
    -   6
-   Output:

    `ABCDEF`  
    `G @HIJ`  
    `KLIMNO`  
    `QRSTUV`  
    `WXYZ`

## Day6

### Stepped Array

-   Given the parameter number of rows (n) create an array:
    -   The number of rows (n) can vary between 1 and 20
    -   The number of columns is always three times the number of rows.
    -   The matrix is composed of zeros and ones according to the distribution shown in the image, depending on the value of the parameter n.
-   It is about printing the matrix in the terminal based on the value of n that they give us.

![matriz.png](https://drive.google.com/uc?id=1yff9bW_yu-U1aTdbR2mTmWkD31ZPrqnc)

-   If n = 5 you would get the following result:

![matriz.png](https://drive.google.com/uc?id=1Pz5wbwCls6DAwOh2SI0Nes-011nSLTjC)
