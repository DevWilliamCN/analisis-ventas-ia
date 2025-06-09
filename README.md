# 📊 Análisis de Ventas con Inteligencia Artificial

Este proyecto es una aplicación interactiva desarrollada con [Streamlit](https://streamlit.io/) que permite cargar archivos CSV o PDF con información de ventas, procesarlos, generar visualizaciones dinámicas y realizar predicciones de ingresos utilizando un modelo de Inteligencia Artificial.

---

## 🚀 Funcionalidades

- 📁 **Carga de archivos**: Soporte para archivos `.csv` y `.pdf`
- 📊 **Visualización de datos**: Estadísticas descriptivas, ingresos por categoría y fecha
- 🎛️ **Filtros interactivos**: Por producto, categoría y rango de fechas
- 🤖 **Modelo IA**: Predicción de ingresos futuros usando regresión lineal
- 🧾 **Interfaz protegida**: Inicio de sesión con diferentes roles (Admin, Cliente Invitado, etc.)
- 💻 **Diseño personalizado**: Interfaz oscura, moderna y responsive

---

## 🛠️ Tecnologías utilizadas

- **Python 3.12**
- **Streamlit** (interfaz gráfica web)
- **Pandas** (procesamiento de datos)
- **NumPy** (cálculos numéricos)
- **Matplotlib** (gráficos y visualización)
- **scikit-learn** (modelo de regresión lineal)
- **PyMuPDF (fitz)** (extracción de texto y tablas desde PDF)
- **bcrypt** (hashing seguro de contraseñas)

---

## 🔐 Seguridad implementada

- 🔐 **Autenticación de usuarios con roles** mediante `streamlit-authenticator`
- 🧂 **Contraseñas encriptadas** con algoritmo **bcrypt**
- 🔒 **Sesiones protegidas con cookies** (`streamlit_authenticator`)
- 🔍 **Validación y limpieza de archivos cargados** para evitar errores o datos corruptos

---

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

---

## 🔐 Usuarios de prueba

| Usuario   | Contraseña       | Rol             |
|-----------|------------------|------------------|
| cliente   | `cliente123`     | Cliente Invitado |

> Todas las contraseñas están encriptadas con bcrypt.

---

## 🌐 Despliegue

Puedes desplegar este proyecto fácilmente en [Streamlit Cloud](https://streamlit.io/cloud) para hacerlo accesible públicamente desde un navegador web. Solo necesitas una cuenta de GitHub y conectar el repositorio.

---

## 👨‍💻 Autor

**William Cubero Navarro**  
🔗 [LinkedIn](https://www.linkedin.com/in/william-cubero-navarro-75880727a/)  
🐱 [GitHub](https://github.com/DevWilliamCN)

---

> Si te gustó este proyecto, no dudes en darle ⭐ en GitHub y compartirlo con tus colegas.
