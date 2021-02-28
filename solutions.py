"""
The list of exercises from: https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises%20for%20Python%203.md
"""
import doctest


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

q20(int(input("enter number [20]: ") or "20"))

doctest.testmod()
