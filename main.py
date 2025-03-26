def is_kaprekar(n):
    square = n * n
    square_str = str(square)
    
    # Caso especial para números com quadrado de um único dígito
    if len(square_str) == 1:
        return square == n
    
    # Verifica todas as divisões possíveis do quadrado
    for i in range(1, len(square_str)):
        left_str = square_str[:i]
        right_str = square_str[i:]
        
        # Ignora divisões com partes vazias
        if not left_str or not right_str:
            continue
        
        # A parte esquerda não pode ser zero
        if left_str == '0':
            continue
        
        # A parte direita não pode ser toda zeros
        if all(c == '0' for c in right_str):
            continue
        
        # Converte para inteiros e verifica a soma
        left = int(left_str)
        right = int(right_str)
        
        if left + right == n:
            return True
    
    return False

# Encontrar todos os números de Kaprekar abaixo de 1.000.000
kaprekar_numbers = []
for num in range(1, 10000000):
    if is_kaprekar(num):
        kaprekar_numbers.append(num)
        print(f"Número de Kaprekar encontrado: {num}")

print("Números de Kaprekar menores que 10.000.000:")
print(kaprekar_numbers)
