"""
Símbolos usados na interpolação:

%s: string 
%d: inteiro
%o: octal
%x: hexadecimal
%f: real
%e: real exponencial
%%: sinal de porcentagem
"""
# Zeros à esquerda
print("Agora são %02d:%02d." % (16, 30))

# Real (número após o ponto controla as casas decimais)
print("Porcentagem: %.1f%%, Exponencial: %.2e" % (5.333, 0.00314))

# Octal e hexadecimal
print("Decimal: %d, Octal: %o, Hexadecimal: %x" % (10, 10, 10))


