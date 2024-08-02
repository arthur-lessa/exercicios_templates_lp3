from validate_docbr import CPF

cpf = CPF()

# Validar CPF  # True
print(cpf.generate(True))
print(cpf.generate(False))

print(cpf.validate("49947898865"))
print(cpf.validate("499.478.988-65"))