pc1, qtd1, vlpc1 = map(float, input().split())
pc2, qtd2, vlpc2 = map(float, input().split())
vlf = qtd1*vlpc1+qtd2*vlpc2
print("VALOR A PAGAR: R$ %.2f"%vlf)
