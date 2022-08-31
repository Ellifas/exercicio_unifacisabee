x = int(input())
a = x//365
resto = x%365
m = resto//30
d = resto%30
print("%i ano(s)"%a)
print("%i mes(es)"%m)
print("%i dia(s)"%d)