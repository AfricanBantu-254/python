#chekc isf a users age is approrpiat to buy tckets to a concert

def concert_program(age):
    if age < 18:
        print("No entry")
    elif 18 <= age <= 25:
        print("Free drink")
    else:
        print("Extra ticket")

#to get funvction to work you must  trigger
age=int(input ("enter your age:"))
    #make call to a funciton
concert_program(age)

