a, b, c = map(int, input().split())
MAIORAB = ((a+b+abs(a-b))/2)
MAIORC = (MAIORAB + c + abs(MAIORAB - c))/2

print("%d eh o maior"%MAIORC)