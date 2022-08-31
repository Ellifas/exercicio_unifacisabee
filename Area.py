A, B, C = map(float,input().split())
tri = (A * C)/2
circ = 3.14159 * C**2
trape = (A + B) *C /2
quad = B**2
ret = A * B
print("TRIANGULO: %.3f" %tri)
print("CIRCULO: %.3f" %circ)
print("TRAPEZIO: %.3f" %trape)
print("QUADRADO: %.3f" %quad)
print("RETANGULO: %.3f" %ret)