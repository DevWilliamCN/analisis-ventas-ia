
# 📊 Análisis de Ventas con Inteligencia Artificial

Este proyecto es una aplicación interactiva desarrollada con [Streamlit](https://streamlit.io/) que permite cargar archivos CSV o PDF con información de ventas, procesarlos, generar visualizaciones dinámicas y realizar predicciones de ingresos utilizando un modelo de Inteligencia Artificial.

## 🚀 Funcionalidades

- 📁 **Carga de archivos**: Soporte para archivos `.csv` y `.pdf`
- 📊 **Visualización de datos**: Estadísticas descriptivas, ingresos por categoría y fecha
- 🎛️ **Filtros interactivos**: Por producto, categoría y rango de fechas
- 🤖 **Modelo IA**: Predicción de ingresos futuros usando regresión lineal
- 🧾 **Interfaz protegida**: Inicio de sesión con diferentes roles (Admin, Cliente Invitado, etc.)
- 💻 **Diseño personalizado**: Interfaz oscura, moderna y responsive

## 📂 Estructura de archivos

```bash
.
├── app.py                 # Archivo principal de la app Streamlit
├── login.py              # Lógica de autenticación de usuarios
├── lector_pdf.py         # Extracción de tablas desde PDFs
├── generar_hash.py       # Herramienta para crear contraseñas encriptadas
├── verificar_hash.py     # Herramienta para validar contraseñas
├── ventas.csv / .pdf     # Archivos de ejemplo
├── requirements.txt      # Dependencias necesarias
```

## 🔐 Usuarios de prueba

| Usuario   | Contraseña       | Rol             |
|-----------|------------------|------------------|
| william   | `william123`     | William Cubero   |
| admin     | `admin123`       | Administrador    |
| cliente   | `cliente123`     | Cliente Invitado |

> Todas las contraseñas están encriptadas con bcrypt.

## 🌐 Despliegue (opcional)

Puedes desplegar este proyecto en [Streamlit Cloud](https://streamlit.io/cloud) para que funcione en la web de forma gratuita.

## 👨‍💻 Autor

**William Cubero Navarro**  
🔗 [LinkedIn](https://www.linkedin.com/in/william-cubero-navarro-75880727a/)  
🐱 [GitHub](https://github.com/DevWilliamCN)

---

> Si te gustó este proyecto, no dudes en darle ⭐ en GitHub.
