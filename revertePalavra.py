input = "Leonardo"

# começa no ultimo caractere e vai decrecendo -1, e terminando no -1, onde não havera letra 
stringReversed= ""
for i in range(len(input) - 1, -1, -1):
    stringReversed += input[i]

print("A string invertida ficou assim:", stringReversed)
