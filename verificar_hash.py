from streamlit_authenticator.hasher import Hasher

# Las contraseñas que querés validar
claves_claras = ["1234", "adminpass", "invitado2025"]

# Hashes actuales en tu login.py
hashes_guardados = [
    "$2b$12$Xhi0JjS/JKpMYFwGdkRXhuL1pCUrO2s6yYbPswSnW7Tsk8Yv8RNYe",
    "$2b$12$nypOG4ZCtsPPRFDbAh8LP.yr35hILY01dQx.t2I8uI.0LxFeAHx/S",
    "$2b$12$Vi5OgwQEmnB8QkAfkYtR0ewPDn3TcDe71cS65jHkUlIfmcuy0/vkW"
]

# Validar si coinciden
for clave, hash in zip(claves_claras, hashes_guardados):
    print(f"{clave}: {'✅ Válido' if Hasher([clave]).verify(clave, hash) else '❌ Incorrecto'}")
