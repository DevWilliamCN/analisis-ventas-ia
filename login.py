import streamlit as st
import streamlit_authenticator as stauth

def cargar_autenticacion():
    users = {
        "usernames": {
            "william": {
                "name": "William Cubero",
                "password": "$2b$12$4o.wKt7nF0DkYcEiRVAe1edT07YW/BT.R.Cma1Z5QWm/sNUU/m6rS"
            },
            "admin": {
                "name": "Administrador",
                "password": "$2b$12$LLUCgssukE61XnTShWB1X.yrU1/r8CZAOB6tm/bnqD3j65WpQhBtm"
            },
            "cliente": {
                "name": "Cliente Invitado",
                "password": "$2b$12$Q23K6.73ZVxRqFFWVKcUgujfRz2Rh06yi.nQp33Ov43n3SjWGXMwO"
            }
        }
    }

    authenticator = stauth.Authenticate(
        users,
        "analisis_ventas_cookie",
        "clave_super_secreta_segura",
        cookie_expiry_days=1
    )

    # 🎨 ESTILOS SOLO FOOTER
    st.markdown("""
        <style>
            html, body, .main {
                background-color: #000 !important;
                color: white !important;
                font-family: 'Segoe UI', sans-serif;
            }

            .stApp {
                padding-bottom: 60px;
            }

            .custom-footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #111;
                color: #999;
                text-align: center;
                padding: 0.7rem;
                font-size: 0.85rem;
                border-top: 1px solid #222;
            }

            input {
                background-color: #1f1f1f !important;
                color: white !important;
                border: 1px solid #444 !important;
                border-radius: 8px !important;
            }

            button[kind="primary"] {
                background-color: #00bfff !important;
                color: white !important;
                border-radius: 8px !important;
                font-size: 1rem;
                margin-top: 1rem;
            }

            .stAlert {
                background-color: #222 !important;
                color: white !important;
                font-size: 0.9rem !important;
                border-radius: 10px !important;
            }

            .right-text {
                padding-top: 2vh;
            }
        </style>

        <div class="custom-footer">
            © 2025 William Cubero | Todos los derechos reservados
        </div>
    """, unsafe_allow_html=True)

    # 🔐 LOGIN VISUAL
    if not st.session_state.get("authentication_status"):
        col1, col2 = st.columns([1.2, 1])

        with col1:
            st.markdown("## 🔐 Iniciá sesión")
            authenticator.login(location="main")

        with col2:
            st.markdown("<div class='right-text'>", unsafe_allow_html=True)
            st.markdown("""
            ### Bienvenido a tu Dashboard

            Este sistema analiza tus archivos de ventas (.csv o .pdf), calcula estadísticas claves y utiliza un modelo de Inteligencia Artificial para predecir ingresos futuros.

            - 📊 Gráficos automáticos  
            - 📁 Soporte para CSV y PDF  
            - 🤖 IA para pronósticos  

            **Iniciá sesión para comenzar 🚀**

            👨‍💻 **Desarrollador: William Cubero Navarro – Ingeniero en Tecnologías de la Información**

            <div style="margin-top: 1.5rem; display: flex; gap: 1.2rem;">
                <a href="https://www.linkedin.com/in/william-cubero-navarro-75880727a/" target="_blank">
                    <img src="https://skillicons.dev/icons?i=linkedin" width="42" height="42"/>
                </a>
                <a href="https://github.com/DevWilliamCN" target="_blank">
                    <img src="https://skillicons.dev/icons?i=github" width="42" height="42"/>
                </a>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        if st.session_state.get("authentication_status") is False:
            st.error("❌ Usuario o contraseña incorrectos.")
        elif st.session_state.get("authentication_status") is None:
            st.warning("⚠️ Iniciá sesión para continuar.")
        st.stop()

    # ✅ Autenticado
    authenticator.logout("Cerrar sesión", "sidebar")
    st.sidebar.success(f"👋 Bienvenido, {st.session_state['name']}")
    return st.session_state['name']

# Ejecutar si login.py es el principal
if __name__ == "__main__":
    cargar_autenticacion()
