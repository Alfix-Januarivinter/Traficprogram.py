#version 0.1.2 (debug release) https://github.com/Alfix-Januarivinter/Traficprogram.py
import random
#imports random software package for generate random numbers
while True:
    a = random.randint(1,5)
    b = random.randint(1,3)
    d1 = random.randint(1,3)
    d2 = random.randint(1,3)
    d3 = random.randint(1,3)
    d4 = random.randint(1,3)
    print(d1, d2, d3, d4)
    #generates a random number and stores it in different places

    n1= 1
    n2= 2
    n3= 3
    n4= 4
    c= 0
    #sets a value on the different variables

    c = a * b
    n1 = n1 * c
    n2 = n2 * c
    n3 = n3 * a
    n4 = n4 * b
    #performs the operations and assigns the result to the respective variables

    if d1 == 1:
        print("d1 = 1")
        while n1 > 0:
            if d2 == 1:
                if n2 > 0:
                    print("d2 = 1")
                while n2 > 0:
                    n2 = n2 - 1
            if d3 == 1:
                if n3 > 0:
                    print("d3 = 1")
                while n3 > 0:
                    n3 = n3 - 1
            if d4 == 1:
                if n4 > 0:
                    print("d4 = 1")
                while n4 > 0:
                    n4 = n4 - 1
            n1 = n1 - 1

    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        print("Congratulations, its done!")
        input()
        break
    
    #prints the result based on the operations performed and the conditions is right

    elif d2 == 1:
        if n2 > 0:
            print("d2 = 1")
        while n2 > 0:
            if d1 == 1:
                if n1 > 0:
                    print("d1 = 1")
                while n1 > 0:
                    n1 = n1 - 1
            if d3 == 1:
                if n3 > 0:
                    print("d3 = 1")
                while n3 > 0:
                    n3 = n3 - 1
            if d4 == 1:
                if n4 > 0:
                    print("d4 = 1")
                while n4 > 0:
                    n4 = n4 - 1
            n2 = n2 - 1
    
    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        print("Congratulations, its done!")
        input()
        break
    
    #prints the result based on the operations performed and the conditions is right
    elif d3 == 1:
        if n3 > 0:
            print("d3 = 1")
        while n3 > 0:
            if d1 == 1:
                if n1 > 0:
                    print("d1 = 1")
                while n1 > 0:
                    n1 = n1 - 1
            if d2 == 1:
                if n2 > 0:
                    print("d2 = 1")
                while n2 > 0:
                    n2 = n2 - 1
            if d4 == 1:
                if n4 > 0:
                    print("d4 = 1")
                while n4 > 0:
                    n4 = n4 - 1
            n3 = n3 - 1
    
    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        print("Congratulations, its done!")
        input()
        break
    
    #prints the result based on the operations performed and the conditions is right
    
    elif d4 == 1:
        if n4 > 0:
            print("d4 = 1")
        while n4 > 0:
            if d1 == 1:
                if n1 > 0:
                    print("d1 = 1")
                while n1 > 0:   
                    n1 = n1 - 1
            if d2 == 1:
                if n2 > 0:
                    print("d2 = 1")
                while n2 > 0:
                    n2 = n2 - 1
            if d3 == 1:
                if n3 > 0:
                    print("d3 = 1")
                while n3 > 0:
                    n3 = n3 - 1
            n4 = n4 - 1
    
    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        print("Congratulations, its done!")
        input()
        break
    
    #prints the result based on the operations performed and the conditions is right
    
    elif d1 > 1:
        if d1 == 2:
            print("d1 = 2")
        if d1 == 3:
            print("d1 = 3")
        while n1 > 0:
            if d2 > 1:
                if n2 > 0:
                    if d2 == 2:
                        print("d2 = 2")
                    if d2 == 3:
                        print("d2 = 3")
                while n2 > 0:
                    n2 = n2 - 1
            if d3 > 1:
                if n3 > 0:
                    if d3 == 2:
                        print("d3 = 2")
                    if d3 == 3:
                        print("d3 = 3")
                while n3 > 0:
                    n3 = n3 - 1
            if d4 > 1:
                if n4 > 0:
                    if d4 == 2:
                        print("d4 = 2")
                    elif d4 == 3:
                        print("d4 = 3")
                while n4 > 0:
                    n4 = n4 - 1
            n1 = n1 - 1
    
    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        print("Congratulations, its done!")
        input()
        break
    
    #prints the result based on the operations performed and the conditions is right
    
    elif d2 > 1:
        if n2 > 0:
            if d2 == 2:
                print("d2 = 2")
            if d2 == 3:
                print("d2 = 3")
        while n2 > 0:
            if d1 > 1:
                if d1 == 3:
                    if n1 > 0:
                        if d1 == 2:
                            print("d1 = 2")
                        if d1 == 3:
                            print("d1 = 3")
                while n1 > 0:
                    n1 = n1 - 1
            if d3 > 1:
                if n3 > 0:
                    if d3 == 2:
                        print("d3 = 2")
                    if d3 == 3:
                        print("d3 = 3")
                while n3 > 0:
                    n3 = n3 - 1
            if d4 > 1:
                if n4 > 0:
                    if d4 == 2:
                        print("d4 = 2")
                    elif d4 == 3:
                        print("d4 = 3")
                while n4 > 0:
                    n4 = n4 - 1
            n2 = n2 - 1
    
    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        print("Congratulations, its done!")
        input()
        break
    
    #prints the result based on the operations performed and the conditions is right
    
    elif d3 > 1:
        if n3 > 0:
            if d3 == 1:
                print("d3 = 2")
            if d3 == 3:
                print("d3 = 3")
        while n3 > 0:
            if d1 > 1:
                if n1 > 0:     
                    if d1 == 2:
                        print("d1 = 2")
                    if d1 == 3:
                        print("d1 = 3")
                while n1 > 0:
                    n1 = n1 - 1
            if d2 > 1:
                if n2 > 0:
                    if d2 == 2:
                        print("d2 = 2")
                    if d2 == 3:
                        print("d2 = 3")
                while n2 > 0:
                    n2 = n2 - 1
            if d4 > 1:
                if n4 > 0:
                    if d4 == 2:
                        print("d4 = 2")
                    elif d4 == 3:
                        print("d4 = 3")
                while n4 > 0:
                    n4 = n4 - 1
            n3 = n3 - 1
    
    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        print("Congratulations, its done!")
        input()
        break
    
    #prints the result based on the operations performed and the conditions is right
    
    elif d4 > 1:
        if n4 > 0:
            if d4 == 1:
                print("d4 = 2")
            elif d4 == 3:
                print("d4 = 3")
        while n4 > 0:
            if d1 > 1:
                if n1 > 0:
                    if d1 == 2:
                        print("d1 = 2")
                    if d1 == 3:
                        print("d1 = 3")
                while n1 > 0:
                    n1 = n1 - 1
            if d2 > 1:
                if n2 > 0:
                    if d2 == 2:
                        print("d2 = 2")
                    if d2 == 3:
                        print("d2 = 3")
                while n2 > 0:
                    n2 = n2 - 1
            if d3 > 1:
                if n3 > 0:
                    if d3 == 2:
                        print("d3 = 2")
                    if d3 == 3:
                        print("d3 = 3")
                while n3 > 0:
                    n3 = n3 - 1
            n4 = n4 - 1
    
    if n1 == 0 and n2 == 0 and n3 == 0 and n4 == 0:
        print("Congratulations, its done!")
        input()
        break
    
    #prints the result based on the operations performed and the conditions is right
    
    else:
        print("What this is an error in the system. The operation was not performed. Contact the creator/developer of the program! https://github.com/Alfix-Januarivinter/Traficprogram.py Error code: exit")
        input()
        break
    #if the conditions are not met, the program will print an error message and ask contact the bug to a developer https://github.com/Alfix-Januarivinter/Traficprogram.py