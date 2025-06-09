import bcrypt

def generar_hash(contraseñas):
    return [bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode() for p in contraseñas]

# Ejemplo
passwords = ["1234", "adminpass", "invitado2025"]
hashes = generar_hash(passwords)

for h in hashes:
    print(h)
