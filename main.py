#quiz game
Name = input('Enter your name: ')
age = int(input('Enter your age: '))
if  age<18:
    print('You cannot play game!')
else:
    print('You can play!')
    print('Hello,welcome to my quiz game!')

    ans = input('Are you ready to play? (yes/no):')
    if ans.lower() == "yes" :
        print("Welcome sir!")
    else:
        print("no")

    score = 0
    Total_q = 3

    ans = input('1.What is your favourite language?\n(a[python]/b[ruby])\n')
    if ans.lower() == "a" :
        score += 1
        print("correct")
    else:
        print("incorrect")

    ans = input('2.What is pep?\n(a[Python Enhancement Proposal],b[Personalised Employment Pass])\n')
    if ans.lower() == "a" :
        score += 1
        print("correct")
    else:
        print("incorrect")

    ans = input('3.what is Summer Favorite Food??\n(a[apple]/b[mango])\n')
    if ans.lower() == "b" :
        score += 1
        print("correct")
    else:
        print("incorrect")

    print('Thank you for playing,you got', score, "question correct")
    Marks = (score/Total_q)*100

    print("Marks: ", Marks)
    print("Good Bye")
