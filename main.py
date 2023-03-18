abc = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def number(n):
    firstpart = 0
    for i in range(len(n)-1):
        firstpart += 26**(i+1)
    secondpart = 0
    j = 0
    for i in n:
        j += 1
        secondpart += (i-1)*(26**(len(n)-j))
    print(firstpart + secondpart + 1, end="")

def letters(n):
    answer = []
    power = 0
    while n > (26**power):
        power += 1
    power = power - 1
    
    for i in range(power + 1):
        answer.append(int(n/(26**power)))
        n = n%(26**power)
        power = power - 1
    return answer

option = input()
n = input()
length = len(n)
position = []

if option  == "L":
    for i in n:
        position.append(abc.index(i)+1)
    number(position)
elif option == "N":
    answer = letters(int(n))
    string = ""
    for i in range(len(answer)):
        string += abc[answer[i]-1]
    print(string, end="")
