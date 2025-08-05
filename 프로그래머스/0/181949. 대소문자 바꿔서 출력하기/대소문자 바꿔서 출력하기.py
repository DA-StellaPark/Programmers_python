str = input()

a = ''

for i in str:
    if (i.islower()) :
        a = a + i.upper()
    else :
        a = a + i.lower()
        
print(a)