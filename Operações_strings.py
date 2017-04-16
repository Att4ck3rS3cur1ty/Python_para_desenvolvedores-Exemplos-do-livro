s = "Camel"

# Concatenação
print("The " + s + " run away!")

# Interpolação
print("tamanho de %s => %d" % (s, len(s)))

# String tratada como sequência
for ch in s: print(ch)

# Strings são objetos
if s.startswith("C"): print(s.upper())

# Imprime o valor da variável s 3 vezes
print(3 * s)
# Que resulta na mesma coisa da expressão:
print(s + s + s)