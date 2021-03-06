"""
The list of exercises from: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises%20for%20Python%203.md
"""
from ast import fix_missing_locations
import doctest
from math import e, sqrt
from random import shuffle
from re import UNICODE


def q1():
    """ Question 1: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.
    >>> q1()
    2002, 2009, 2016, 2023, 2037, 2044, 2051, 2058, 2072, 2079, 2086, 2093, 2107, 2114, 2121, 2128, 2142, 2149, 2156, 2163, 2177, 2184, 2191, 2198, 2212, 2219, 2226, 2233, 2247, 2254, 2261, 2268, 2282, 2289, 2296, 2303, 2317, 2324, 2331, 2338, 2352, 2359, 2366, 2373, 2387, 2394, 2401, 2408, 2422, 2429, 2436, 2443, 2457, 2464, 2471, 2478, 2492, 2499, 2506, 2513, 2527, 2534, 2541, 2548, 2562, 2569, 2576, 2583, 2597, 2604, 2611, 2618, 2632, 2639, 2646, 2653, 2667, 2674, 2681, 2688, 2702, 2709, 2716, 2723, 2737, 2744, 2751, 2758, 2772, 2779, 2786, 2793, 2807, 2814, 2821, 2828, 2842, 2849, 2856, 2863, 2877, 2884, 2891, 2898, 2912, 2919, 2926, 2933, 2947, 2954, 2961, 2968, 2982, 2989, 2996, 3003, 3017, 3024, 3031, 3038, 3052, 3059, 3066, 3073, 3087, 3094, 3101, 3108, 3122, 3129, 3136, 3143, 3157, 3164, 3171, 3178, 3192, 3199
    """

    list = [str(num) for num in range(2000, 3201) if num % 7 == 0 and num % 5 != 0]
    print(", ".join(list))

# q1()

def q2(num):
    """Question 2: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320
    >>> q2(8)
    40320
    """
    res=1
    while num > 0:
        res, num = res*num, num-1
    print(res)

# q2(int(input("provide number to calculate factorial [8]: ") or "8"))

def q3(num):
    """With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    >>> q3(8)
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
    """
    print(dict([(k, k*k) for k in range(1, num+1)]))

# q3(int(input("provide number to produce dict with powers [8]: ") or "8"))

def q4(input):
    """Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
    >>> q4("34,67,55,33,12,98")
    ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
    """
    l = str(input).split(",")
    print(l, end=" ")
    print(tuple(l))

# q4(input("provide comma-separated list of numbers [34,67,55,33,12,98]: ") or "34,67,55,33,12,98")

def q5():
    """Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.
    """
    class myClass():
        def __init__(self):
            self.string = ""
        def getString(self):
            self.string = input("enter string: ")
        def printString(self):
            print(self.string.upper())

    i = myClass()
    i.getString()
    i.printString()

# q5()

def q6(input):
    """Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24
    >>> q6("100,150,180")
    18,22,24

    """
    import math
    output = []
    for D in input.split(","):
        output.append('{0:.0f}'.format(math.sqrt((2*50*int(D))/30)))
    print(",".join(output))

# q6(input("enter the comma-separated list of values [100,150,180]: ") or "100,150,180")

def q7(x, y):
    """
    Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    >>> q7(3,5)
    [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
    """
    # matrix = []
    # for i in range(x):
    #     line = []
    #     for j in range(y):
    #         line.append(i*j)
    #     matrix.append(line)
    # print(matrix)

    print([[i*j for j in range(y)] for i in range(x)])

# q7(int(input("enter array X size [3]: ") or "3"), int(input("enter array Y size [5]: ") or "5"))

def q8(input):
    """Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world
    >>> q8("without,hello,bag,world")
    bag,hello,without,world
    """
    print(",".join(sorted((input.split(",")))))

# q8(input("provide comma-separated list of words [without,hello,bag,world]: ") or "without,hello,bag,world")

def q9():
    """
     Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
    """
    data = []
    while True:
        new_sentence = input("enter a new line or press Enter to finish: ")
        if new_sentence:
            data.append(new_sentence)
        else:
            break

    for i in data:
        print(i.upper())

# q9()

def q10(data):
    """
    Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world
    >>> q10("hello world and practice makes perfect and hello world again")
    again and hello makes perfect practice world
    """
    print(" ".join(sorted(set(data.split()))))

# q10(input("enter a sentence [\"hello world and practice makes perfect and hello world again\"]: ") or "hello world and practice makes perfect and hello world again")


def q11(data):
    """
    Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence. Example: 0100,0011,1010,1001 Then the output should be: 1010 Notes: Assume the data is input by console.
    >>> q11("0100,0011,1010,1001")
    1010
    """
    result = [i for i in data.split(",") if (int(i,base=2) % 5 == 0)]
    print(",".join(result))

# q11(input("enter 4 digit binary numbers (comma-separated) [0100,0011,1010,1001]: ") or "0100,0011,1010,1001")

def q12():
    """
    Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
    >>> q12()
    2000,2002,2004,2006,2008,2020,2022,2024,2026,2028,2040,2042,2044,2046,2048,2060,2062,2064,2066,2068,2080,2082,2084,2086,2088,2200,2202,2204,2206,2208,2220,2222,2224,2226,2228,2240,2242,2244,2246,2248,2260,2262,2264,2266,2268,2280,2282,2284,2286,2288,2400,2402,2404,2406,2408,2420,2422,2424,2426,2428,2440,2442,2444,2446,2448,2460,2462,2464,2466,2468,2480,2482,2484,2486,2488,2600,2602,2604,2606,2608,2620,2622,2624,2626,2628,2640,2642,2644,2646,2648,2660,2662,2664,2666,2668,2680,2682,2684,2686,2688,2800,2802,2804,2806,2808,2820,2822,2824,2826,2828,2840,2842,2844,2846,2848,2860,2862,2864,2866,2868,2880,2882,2884,2886,2888
    """
    result = []
    for i in range (1000,3001):
        evenity=True
        for char in set(str(i)):
            if int(char) % 2 != 0:
                evenity=False
                break
        if evenity:
            result.append(str(i))

    print(",".join(result))

#q12()

def q13(data):
    """
    Question: Write a program that accepts a sentence and calculate the number of letters and digits. Suppose the following input is supplied to the program: hello world! 123 Then, the output should be: LETTERS 10 DIGITS 3
    >>> q13("hello world! 123")
    LETTERS 10 DIGITS 3
    """
    letters = 0
    digits = 0
    for i in data:
        if str(i).isalpha():
            letters+=1
        if str(i).isdigit():
            digits+=1
    print(f'LETTERS {letters} DIGITS {digits}')

# q13(input("enter a sentence to calc letters and digits [hello world! 123]: ") or "hello world! 123")

def q14(data):
    """
    Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
    >>> q14("Hello world!")
    UPPER CASE 1 LOWER CASE 9
    """
    upper = 0
    lower = 0
    for i in data:
        if str(i).isupper():
            upper+=1
        if str(i).islower():
            lower+=1
    print(f'UPPER CASE {upper} LOWER CASE {lower}')

# q14(input("enter a sentence to calc upper and lower case [Hello world!]: ") or "Hello world!")

def q15(data):
    """
    Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a. Suppose the following input is supplied to the program: 9 Then, the output should be: 11106
    >>> q15("9")
    11106
    """
    print(int(data)+int(2*data)+int(3*data)+int(4*data))

# q15(input("enter a number [9]: ") or "9")

def q16(data):
    """
    Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. Suppose the following input is supplied to the program: 1,2,3,4,5,6,7,8,9 Then, the output should be: 1,3,5,7,9
    >>> q16("1,2,3,4,5,6,7,8,9")
    1,3,5,7,9
    """
    odds = [i for i in data.split(",") if (int(i) % 2 != 0)]
    print(",".join(odds))

# q16(input("enter a comma-separated list [1,2,3,4,5,6,7,8,9]: ") or "1,2,3,4,5,6,7,8,9")

def q17(data):
    """
    Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following: D 100 W 200
    D means deposit while W means withdrawal. Suppose the following input is supplied to the program: D 300 D 300 W 200 D 100 Then, the output should be: 500
    # >>> q17("D 300 D 300 W 200 D 100")
    # 500
    """
    net = 0
    operations = data.split()
    for i in range(0,len(operations)-1,2):
        if operations[i] in "D":
            net += int(operations[i+1])
        if operations[i] in "W":
            net -= int(operations[i+1])
    print(net)

# q17(input("enter a bank account operations [D 300 D 300 W 200 D 100]: ") or "D 300 D 300 W 200 D 100")

def q18(data):
    """A website requires the users to input username and password to register. Write a program to check the validity of password input by users. Following are the criteria for checking the password:
    At least 1 letter between [a-z]
    At least 1 number between [0-9]
    At least 1 letter between [A-Z]
    At least 1 character from [$#@]
    Minimum length of transaction password: 6
    Maximum length of transaction password: 12 Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma. Example If the following passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then, the output of the program should be: ABd1234@1
    >>> q18("ABd1234@1,a F1#,2w3E*,2We3345")
    ABd1234@1
    """
    import re
    validPasswords = []
    for p in data.split(","):
        if re.match(".*[a-z].*",p) and re.match(".*[A-Z].*",p) and re.match(".*[0-9].*",p) and re.match(".*[$#@].*",p) and (6 <= len(p) <= 12):
            validPasswords.append(p)
    print(",".join(validPasswords))

# q18(input("enter comma-separated passwords [ABd1234@1,a F1#,2w3E*,2We3345]: ") or "ABd1234@1,a F1#,2w3E*,2We3345")

def q19(data: str) -> None:
    """
    You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is: 1: Sort based on name; 2: Then sort based on age; 3: Then sort by score. The priority is that name > age > score. If the following tuples are given as input to the program: Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85 Then, the output of the program should be: [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
    >>> q19("Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85")
    [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
    """
    from operator import itemgetter

    tuples = [tuple(element.split(",")) for element in data.split()]
    tuples.sort(key=itemgetter(0,1,2))
    print(tuples)

# q19(input("enter the (name, age, height) tuples [Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85]: ") or "Tom,19,80 John,20,90 Jony,17,91 Jony,17,93 Json,21,85")

def q20(data: int):
    """
    Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
    >>> q20(20)
    0,7,14
    """
    class MyClass():
        def __init__(self):
            pass
        def generator(self, n):
            for i in range(0,n+1):
                if i % 7 == 0:
                    yield i
    c = MyClass()
    list = [str(i) for i in c.generator(data)]
    print(",".join(list))

# q20(int(input("enter number [20]: ") or "20"))

def q21():
    """
    Question A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following: UP 5 DOWN 3 LEFT 3 RIGHT 2 ¡­ The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program: UP 5 DOWN 3 LEFT 3 RIGHT 2 Then, the output of the program should be: 2
    """
    import math
    pos: list[int] = [0, 0]
    while True:
        data: str = input("enter the step in a format of <direction> <distance>: ")
        if data:
            direction, step = data.split()
            if direction in "UP":
                pos[0]=pos[0]+int(step)
            if direction in "DOWN":
                pos[0]=pos[0]-int(step)
            if direction in "LEFT":
                pos[1]=pos[1]-int(step)
            if direction in "RIGHT":
                pos[1]=pos[1]+int(step)
            print("current position:", pos)
        else:
            distance = round(sqrt(pos[0]**2+pos[1]**2))
            print("finished, distance from 0,0:", distance)
            break

# q21()


def q22(data: str):
    """
    Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. Suppose the following input is supplied to the program: New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3. Then, the output should be: 2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1
    >>> q22("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")
    2:2 3.:1 3?:1 New:1 Python:5 Read:1 and:1 between:1 choosing:1 or:2 to:1 
    """
    words = {}
    for word in sorted(set(data.split())):
        words[word] = data.split().count(word)
        print(f'{word}:{words[word]}', end=" ")

# q22(input("enter the sentence to calulate words frequency [New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.]") or "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")


def q23(x: int):
    """
    Question: Write a method which can calculate square value of number
    >>> q23(5)
    25
    """
    return x**2

# print(q23(int(input("enter a number to square [5]: ") or "5")))

def q24():
    """
    Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
    Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
    And add document for your own function Hints: The built-in document method is doc
    """
    print(abs.__doc__)
    print(int.__doc__)
    print(input.__doc__)
    
# q24()
# print(q24.__doc__)

def q25():
    """
    Question: Define a class, which have a class parameter and have a same instance parameter.
    Hints: Define a instance parameter, need add it in init method You can init a object with construct parameter or set the value later
    """
    class MyClass():
        classParameter = "elo"
        def __init__(self, value):
            self.instanceParameter = value
    
    myInstance = MyClass("siema")
    print(myInstance.classParameter)
    print(myInstance.instanceParameter)

# q25()

def q26(x: int, y:int) -> int:
    """
    Define a function which can compute the sum of two numbers.
    Hints: Define a function with two numbers as arguments. You can compute the sum in the function and return the value.
    >>> q26(2,7)
    9
    """
    return x+y

# print(q26(int(input("input number one [2]: ") or "2"),int(input("input number two [9]: ") or "9")))

def q27(x: int):
    """
    Define a function that can convert a integer into a string and print it in console.
    >>> q27(2)
    2
    """
    print(str(x))

# q27(int(input("enter a number [12321]: ") or "12321"))

## question is a duplicate of 27
def q28(x: int):
    """
    Define a function that can convert a integer into a string and print it in console.
    >>> q28(213)
    213
    """
    print(str(x))

# q28(int(input("enter a number [1211321]: ") or "1211321"))

def q29(x: str, y: str):
    """
    Define a function that can receive two integral numbers in string form and compute their sum and then print it in console
    >>> q29("10","20")
    30
    """
    print(int(x)+int(y))

# q29(input("enter number one: "), input("enter number two: "))


def q30(x: str, y: str):
    """
    Define a function that can accept two strings as input and concatenate them and then print it in console.
    >>> q30("10","20")
    1020
    """
    print(x+y)

# q30(input("enter string one: "), input("enter string two: "))

def q31(x: str, y: str):
    """
    Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
    >>> q31("raz","osiem")
    osiem
    """
    if len(x)==len(y):
        print(x)
        print(y)
    elif len(x)>len(y):
        print(x)
    else:
        print(y)

# q31(input("input first string: "),input("input second string: "))

def q32(x: int):
    """
    Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".
    >>> q32(5)
    It is an odd number
    >>> q32(4)
    It is an even number
    """
    if x % 2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")

# q32(int(input("please enter number [5]: ") or "5"))

def q33():
    """
    Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
    >>> q33()
    {1: 1, 2: 4, 3: 9}
    """
    myDict = {}
    for i in range(1,4):
        myDict[i]=i**2
    print(myDict)

# q33()

def q34():
    """
    Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.
    >>> q34()
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225, 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}
    """
    myDict = {}
    for i in range(1,21):
        myDict[i]=i**2
    print(myDict)

# q34()

def q35():
    """
    Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.
    >>> q35()
    1 4 9 16 25 36 49 64 81 100 121 144 169 196 225 256 289 324 361 400
    """
    myDict = {}
    for i in range(1,21):
        myDict[i]=i**2
    print(" ".join([str(value) for key, value in myDict.items()]))

# q35()

def q36():
    """
    Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
    >>> q36()
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    """
    myDict = {}
    for i in range(1,21):
        myDict[i]=i**2
    print(" ".join([str(key) for key, value in myDict.items()]))

# q36()

def q37():
    """
    Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).
    >>> q37()
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
    """
    list = [i**2 for i in range(1,21)]
    print(list)

# q37()

def q38():
    """
    Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.
    >>> q38()
    [1, 4, 9, 16, 25]
    """
    list = [i**2 for i in range(1,21)]
    print(list[:5])

# q38()

def q39():
    """
    Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.
    >>> q39()
    [256, 289, 324, 361, 400]
    """
    list = [i**2 for i in range(1,21)]
    print(list[-5:])

# q39()    

def q40():
    """
    Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.
    >>> q40()
    [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
    """
    list = [i**2 for i in range(1,21)]
    print(list[5:])

# q40()

def q41():
    """
    Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
    >>> q41()
    (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)
    """
    tpl = tuple(i**2 for i in range(1,21))
    print(tpl)

# q41()

def q42():
    """
    With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
    >>> q42()
    (1, 2, 3, 4, 5)
    (6, 7, 8, 9, 10)
    """
    tpl = tuple((1,2,3,4,5,6,7,8,9,10))
    print(tpl[:round(len(tpl)/2)])
    print(tpl[round(len(tpl)/2):])

# q42()

def q43():
    """
    Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
    >>> q43()
    (2, 4, 6, 8, 10)
    """
    initTuple = tuple((1,2,3,4,5,6,7,8,9,10))
    outTUple = tuple(i for i in initTuple if i % 2 == 0)
    print(outTUple)

# q43()

def q44(x: str):
    """
    Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
    >>> q44("yes")
    yes
    >>> q44("Yes")
    yes
    >>> q44("YES")
    yes
    >>> q44("No")
    no
    >>> q44("awgdb")
    no
    """
    if x.lower() in "yes":
        print("yes")
    else:
        print("no")

# q44(input("yes or no?: "))

def q45():
    """
    Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].
    >>> q45()
    [2, 4, 6, 8, 10]
    """
    ## Ugly:
    # def isEven(i):
    #     if i%2==0:
    #         return True
    #     else:
    #         return False

    # list = [1,2,3,4,5,6,7,8,9,10]
    # newList = [j for j in filter(isEven, list)]
    # print(newList)

    ## Pretty:
    list = [1,2,3,4,5,6,7,8,9,10]
    newList = [j for j in filter(lambda i: i%2==0, list)]
    print(newList)

# q45()

def q46():
    """
    Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
    >>> q46()
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    """
    list = [1,2,3,4,5,6,7,8,9,10]
    newList = [el for el in map(lambda i: i**2, list)]
    print(newList)

# q46()

def q47():
    """
    Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
    >>> q47()
    [4, 16, 36, 64, 100]
    """
    list = [1,2,3,4,5,6,7,8,9,10]
    newList = [j for j in map(lambda i: i**2, filter(lambda i: i%2==0, list))]
    print(newList)

# q47()

def q48():
    """
    Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
    >>> q48()
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    """
    newList = [j for j in filter(lambda i: i%2==0, range(1,21))]
    print(newList)

# q48()

def q49():
    """
    Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
    >>> q49()
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
    """
    newList = [el for el in map(lambda i: i**2, range(1,21))]
    print(newList)

# q49()

def q50():
    """
    Define a class named American which has a static method called printNationality.
    >>> q50()
    american
    """
    class American():

        @staticmethod
        def printNationality():
            print("american")

    American.printNationality()

# q50()

def q51():
    """
    Define a class named American and its subclass NewYorker.
    >>> q51()
    american
    NY
    """
    class American():
        @staticmethod
        def printNationality():
            print("american")
    
    class NewYorker(American):
        @staticmethod
        def printCity():
            print("NY")

    NewYorker.printNationality()
    NewYorker.printCity()
    
# q51()

def q52():
    """
    Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
    >>> q52()
    314.16
    """
    class Circle():
        def __init__(self, radius: float):
            self.radius = radius
        
        def calcArea(self):
            import math
            return math.pi*(self.radius**2)

    myCircle = Circle(10)
    print(f'{myCircle.calcArea():.2f}')

# q52()

def q53():
    """
    Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
    >>> q53()
    125.0
    """
    class Rectangle():
        def __init__(self, length: float, width: float):
            self.length = length
            self.width = width 
        def computeArea(self):
            return self.length*self.width
        
    myRectangle = Rectangle(10, 12.5)
    print(myRectangle.computeArea())

# q53()

def q54():
    """
    Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
    >>> q54()
    16
    """
    class Shape():
        def area(self):
            return 0
    
    class Square(Shape):
        def __init__(self, length: float):
            self.length = length
        def area(self):
            return self.length**2

    mySquare = Square(4)
    print(mySquare.area())

# q54()

def q55():
    """
    Please raise a RuntimeError exception.
    >>> q55()
    Traceback (most recent call last):
    ...
    RuntimeError
    """
    raise RuntimeError

# q55()

def q56():
    """
    Write a function to compute 5/0 and use try/except to catch the exceptions.
    >>> q56()
    nie dziel przez zero kolego
    """
    try:
        5/0
    except ZeroDivisionError:
        print("nie dziel przez zero kolego")
    
# q56()

def q57():
    """
    Define a custom exception class which takes a string message as attribute.
    """ 

    class MyException(Exception):
        """
        Class with raises MyExpection.
        Attributes:
        - msg
        """
        def __init__(self, msg = None):
            self.message = msg

    raise MyException("coś poszło nie tak")

# q57()

def q58(data: str):
    """
    Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
    Example: If the following email address is given as input to the program:
    john@google.com
    Then, the output of the program should be:
    john
    In case of input data being supplied to the question, it should be assumed to be a console input.
    >>> q58("john@google.com")
    john
    """
    name=data.split("@")[0]
    print(name)

# q58(input("enter email address [john@google.com]: ") or "john@google.com")


def q59(data: str):
    """
    Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.
    Example: If the following email address is given as input to the program:
    john@google.com
    Then, the output of the program should be:
    google
    In case of input data being supplied to the question, it should be assumed to be a console input.
    >>> q59("john@google.com")
    google
    """
    import re
    if re.match(r"(\w+)@(\w+)\.(\w+)", data):
        print(data.split("@")[1].split(".")[0])

# q59(input("enter email address [john@google.com]: ") or "john@google.com")

def q60(data: str):
    """
    Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
    Example: If the following words is given as input to the program:
    2 cats and 3 dogs.
    Then, the output of the program should be:
    ['2', '3']
    In case of input data being supplied to the question, it should be assumed to be a console input.
    >>> q60("2 cats and 3 dogs")
    ['2', '3']
    """
    ## simple
    # print([i for i in data.split() if i.isdigit()])

    ## regex
    import re
    print(re.findall(r"\d+", data))

# q60(input("enter sentence [2 cats and 3 dogs]: ") or "2 cats and 3 dogs")

def q61():
    """
    Print a unicode string "hello world".
    >>> q61()
    hello world
    """
    print(u'hello world')

# q61()

def q62():
    """
    Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.
    """
    data = input("enter some data: ")
    print(data)
    ## everything is unicode in python3

# q62()

def q63():
    # -*- coding: ascii -*-
    """
    Write a special comment to indicate a Python source code file is in unicode.
    """

def q64(x: int):
    """
    Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
    Example: If the following n is given as input to the program:
    5
    Then, the output of the program should be:
    3.55
    In case of input data being supplied to the question, it should be assumed to be a console input.
    >>> q64(5)
    3.55
    """
    if x <= 0:
        print("n should be more than 0")
    else:
        acc = 0.0
        for i in range(1,x+1):
            acc += i/(i+1)
        print(f'{acc:.2f}')

# q64(int(input("enter a number [5]: ") or "5"))

def q65(x: int):
    """
    Write a program to compute:
    f(n)=f(n-1)+100 when n>0 and f(0)=1
    with a given n input by console (n>0).
    Example: If the following n is given as input to the program:
    5
    Then, the output of the program should be:
    500
    In case of input data being supplied to the question, it should be assumed to be a console input.
    >>> q65(5)
    500
    """
    def f(n):
        if n == 0:
            return 0
        else:
            return f(n-1)+100

    print(f(x))
    

# q65(int(input("enter a number [5]: ") or "5"))

def q66(x: int):
    """
    The Fibonacci Sequence is computed based on the following formula:
    f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1
    Please write a program to compute the value of f(n) with a given n input by console.
    Example: If the following n is given as input to the program:
    7
    Then, the output of the program should be:
    13
    In case of input data being supplied to the question, it should be assumed to be a console input.
    >>> q66(7)
    13
    """
    a, b = 0, 1
    for i in range(2,x+1):
        a, b = b, a+b
    print(b)

# q66(int(input("enter a number [7]: ") or "7"))


def q67(x: int):
    """
    The Fibonacci Sequence is computed based on the following formula:
    f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1
    Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.
    Example: If the following n is given as input to the program:
    7
    Then, the output of the program should be:
    0,1,1,2,3,5,8,13
    >>> q67(7)
    0,1,1,2,3,5,8,13
    """
    def fib(n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return fib(n-1)+fib(n-2)
    
    fibList = [str(fib(i)) for i in range(x+1)]
    print(",".join(fibList))

# q67(int(input("enter a number [7]: ") or "7"))

def q68(x: int):
    """
    Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.
    Example: If the following n is given as input to the program:
    10
    Then, the output of the program should be:
    0,2,4,6,8,10
    >>> q68(10)
    0,2,4,6,8,10
    """
    def getEven(n):
        for i in range(0,n+1):
            if i % 2 ==0:
                yield i
    list = [str(i) for i in getEven(x)]
    print(",".join(list))

# q68(int(input("enter a number [10]: ") or "10"))

def q69(x: int):
    """
    Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
    Example: If the following n is given as input to the program:
    100
    Then, the output of the program should be:
    0,35,70
    >>> q69(100)
    0,35,70
    """
    def getNums(n):
        for i in range(0,n+1):
            if i % 5 == 0 and i % 7 == 0:
                yield i
    list = [str(i) for i in getNums(x)]
    print(",".join(list))

# q69(int(input("enter a number [100]: ") or "100"))

def q70():
    """
    Please write assert statements to verify that every number in the list [2,4,6,8] is even.
    """
    for i in [2,4,6,8]:
        assert i % 2 == 0
# q70()

def q71(expr: str):
    """
    Please write a program which accepts basic mathematic expression from console and print the evaluation result.
    Example: If the following string is given as input to the program:
    35+3
    Then, the output of the program should be:
    38
    >>> q71("35+3")
    38
    """
    print(eval(expr))

# q71((input("enter an expression [35+3]: ") or "35+3"))

def q72(x: int):
    """
    Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
    """
    list = [0, 2, 3, 5, 6, 8, 11, 12, 14, 15, 16, 18, 19, 20, 21, 23, 24, 25, 26, 28, 30, 35, 36, 37, 40, 41, 42, 43, 44, 47, 49, 51, 52, 53, 54, 57, 58, 60, 63, 65, 66, 67, 69, 70, 71, 72, 73, 77, 79, 80, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98]

    left=0
    right=len(list)-1
    while True:
        index=round((left+right)/2)
        # print(f'interation {i}: lower_pos {lower_pos} upper_pos: {upper_pos} current_pos: {current_pos}')
        if list[index] == x:
            print(f"element {x} found at {index}")
            return index
        elif x > list[index]:
            left=index
        elif x < list[index]:
            right=index
        elif left==index or right==index:
            print("no element found")
            break

# q72(int(input("enter a number [37]: ") or "37"))

def q73():
    """Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.
    """
    list = [0, 2, 3, 5, 6, 8, 11, 12, 14, 15, 16, 18, 19, 20, 21, 23, 24, 25, 26, 28, 30, 35, 36, 37, 40, 41, 42, 43, 44, 47, 49, 51, 52, 53, 54, 57, 58, 60, 63, 65, 66, 67, 69, 70, 71, 72, 73, 77, 79, 80, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 98]

    left=0
    right=len(list)-1
    while True:
        index=round((left+right)/2)
        # print(f'interation {i}: lower_pos {lower_pos} upper_pos: {upper_pos} current_pos: {current_pos}')
        if list[index] == x:
            print(f"element {x} found at {index}")
            return index
        elif x > list[index]:
            left=index
        elif x < list[index]:
            right=index
        elif left==index or right==index:
            print("no element found")
            break

# q73(int(input("enter a number [37]: ") or "37"))

def q74():
    """Please generate a random float where the value is between 10 and 100 using Python math module."""
    import random
    print(10 + random.random()*90)

# q74()

def q75():
    """Please generate a random float where the value is between 5 and 95 using Python math module."""
    import random
    print(5 + random.random()*90)

# q75()

def q76():
    """Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension."""
    import random
    print(random.choice([i for i in range(0,11) if i % 2 == 0]))

# q76()

def q77():
    """Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension."""
    import random 
    print(random.choice([i for i in range(0,11) if i%5==0 and i%7==0]))

# q77()

def q78():
    """Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive."""
    import random
    list = random.sample(range(100,201),5)
    print(list)

# q78()

def q79():
    """Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive."""
    import random
    print(random.sample(range(0,202,2),5))

# q79()

def q80():
    """Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive."""
    import random
    print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))
    
# q80()

def q81():
    """Please write a program to randomly print a integer number between 7 and 15 inclusive."""
    import random
    print(random.randint(7,15))

# q81()


def q82():
    """ Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!". """
    import zlib
    myString = "hello world!hello world!hello world!hello world!"
    compressedData = zlib.compress(bytes(myString, 'utf-8'))
    print(compressedData)
    myDecompressedString = bytes.decode(zlib.decompress(compressedData),'utf-8')
    print(myDecompressedString)

# q82()

def q83():
    """Please write a program to print the running time of execution of "1+1" for 100 times. """ 
    from timeit import Timer
    print(Timer(stmt='1+1').timeit(number=100))

#q83()

def q84():
    """Please write a program to shuffle and print the list [3,6,7,8]."""
    import random
    list = [3,6,7,8]
    random.shuffle(list)
    print(list)

# q84()

def q85():
    """Please write a program to shuffle and print the list [3,6,7,8]."""
    import random
    list = [3,6,7,8]
    random.shuffle(list)
    print(list)

# q85()

def q86():
    """ Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"]. """ 
    subject = ["I", "You"]
    verb = ["Play", "Love"]
    object = ["Hockey","Football"]

    for s in subject:
        for v in verb:
            for o in object:
                print(s, v, o) 

# q86()

def q87():
    """ Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24]. """ 
    l = [5,6,77,45,22,12,24]
    print(list(filter(lambda x: x%2==1, l)))

# q87()

def q88():
    """ By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155]. """
    l = [12,24,35,70,88,120,155]
    l = [i for i in l if i % 5 != 0 and i % 7 != 0]
    print(l)

# q88()

def q89():
    """By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].""" 
    l = [12,24,35,70,88,120,155]
    l = [v for i, v in enumerate(l) if i % 2 != 0]
    print(l)

# q89() 

def q90():
    """By using list comprehension, please write a program generate a 358 3D array whose each element is 0."""
    from pprint import pprint as print
    ## Simple way
    a = [[[0] * 8] * 5] * 3
    print(a)
    ## Comprehension way 
    a = [[[0 for i in range(8)] for j in range(5)] for k in range(3)]
    print(a)

# q90()

def q91():
    """By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155]."""
    l = [12,24,35,70,88,120,155]
    l = [v for i, v in enumerate(l) if i not in [0, 4, 5]]
    print(l)

# q91()

def q92():
    """ By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]. """ 
    l = [12,24,35,70,88,120,155]
    l.remove(24)
    print(l)

# q92()

def q93():
    """With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists."""
    l = [1,3,6,78,35,55]
    k = [12,24,35,24,88,120,155]

    print(list(set(l).intersection(k)))

# q93()

def q94():
    """ With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved. """ 
    l = [12,24,35,24,88,120,155,88,120,155]
    k = []
    for i in l:
        if i not in k:
            k.append(i)
    print(k)

# q94()

def q95():
    """Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class."""
    class Person():
        pass
    class Male(Person):
        @staticmethod
        def getGender():
            print("Male")

    class Female(Person):
        @staticmethod
        def getGender():
            print("Female")
    
    Female.getGender()

# q95()

def q96(data: str):
    """Please write a program which count and print the numbers of each character in a string input by console.
    Example: If the following string is given as input to the program:
    abcdefgabc
    Then, the output of the program should be:
    a,2 c,2 b,2 e,1 d,1 g,1 f,1
    >>> q96("abcdefgabc")
    a,2 b,2 c,2 d,1 e,1 f,1 g,1
    """
    myDict = {}
    for i in sorted(set(data)):
        myDict[i]=data.count(i)
    print(" ".join([f'{k},{v}' for k, v in myDict.items()]))



# q96(input("enter string [abcdefgabc]: ") or "abcdefgabc")

def q97(data: str):
    """Please write a program which accepts a string from console and print it in reverse order.
    Example: If the following string is given as input to the program:
    rise to vote sir
    Then, the output of the program should be:
    ris etov ot esir
    >>> q97("rise to vote sir")
    ris etov ot esir
    """
    l = []
    for i in reversed(data.split()):
        reversedString = ""
        for s in reversed(i):
            reversedString += s
        l.append(reversedString)
    print(" ".join(l))

# q97(input("enter string [rise to vote sir]: ") or "rise to vote sir")

def q98(data: str):
    """ Please write a program which accepts a string from console and print the characters that have even indexes.
    Example: If the following string is given as input to the program:
    H1e2l3l4o5w6o7r8l9d
    Then, the output of the program should be:
    Helloworld
    >>> q98("H1e2l3l4o5w6o7r8l9d")
    Helloworld
    """
    print("".join([v for i, v in enumerate(data) if i%2==0]))
    


# q98(input("enter string [H1e2l3l4o5w6o7r8l9d]: ") or "H1e2l3l4o5w6o7r8l9d")

def q99():
    """ Please write a program which prints all permutations of [1,2,3] """
    ## With external module
    import itertools
    l = [1,2,3]
    print(list([i for i in itertools.permutations(l)]))

# q99()

def q100():
    """Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?"""
    heads = 35
    legs = 94

    ## loop way 
    for i in range(1,36):
        chickens = i
        rabbits = 36 - chickens
        legs = chickens*2 + rabbits*4
        if legs==94:
            print(f'above counts is possible if there is {chickens} chickens and {rabbits} rabbits')
            # break

# q100()

doctest.testmod()
