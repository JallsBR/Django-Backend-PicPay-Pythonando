from django.core.exceptions import ValidationError

def validate_cpf(value):
        # Remover pontuação
        cpf = ''.join(char for char in value if char.isdigit())        
        # Validar tamanho
        if len(cpf) != 11:
            raise ValidationError("CPF deve conter 11 dígitos.")
        
        # Verificar se todos os dígitos são iguais
        if cpf == cpf[0] * 11:
            raise ValidationError("CPF inválido (todos dígitos iguais).")
        
        # Função para calcular dígitos verificadores
        def calculate_digit(cpf_slice, factor):
            total = 0
            for digit in cpf_slice:
                total += int(digit) * factor
                factor -= 1
            remainder = total % 11
            return '0' if remainder < 2 else str(11 - remainder)
        
        # Calcular os dois dígitos verificadores
        first_digit = calculate_digit(cpf[:9], 10)
        second_digit = calculate_digit(cpf[:9] + first_digit, 11)
        print(f"Dígitos calculados: {first_digit}{second_digit}")
        
        # Validar CPF final
        if cpf[-2:] != first_digit + second_digit:
            raise ValidationError("CPF inválido (dígitos verificadores incorretos).")

    
