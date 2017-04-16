# Real para inteiro
print("int(3.14) =", int(3.14))

# Inteiro para real
print("float(5) = ", float(5))

# Cálculo entre inteiro e real resulta em real
print("5.0 / 2 + 3 = ", 5.0 / 2 + 3)

# Inteiros em outra base
print("int('20', 8) =", int('20', 8))  # base 8
print("int('20', 16) =", int('20', 16))  # base 16

# Operações com números complexos
c = 3 + 4j
print("Parte real: ", c.real)
print("Parte imaginária: ", c.imag)
print("Conjugado", c.conjugate())
