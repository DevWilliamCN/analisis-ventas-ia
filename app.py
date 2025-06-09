import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import os
from lector_pdf import extraer_tabla_pdf
from login import cargar_autenticacion

# ✅ Configuración de página
st.set_page_config(
    page_title="Análisis de Ventas con IA",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 🔐 Login
usuario = cargar_autenticacion()

# 🌐 Solo el footer (el header fue eliminado)
st.markdown("""
    <style>
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

        .stApp {
            padding-bottom: 60px;
        }
    </style>

    <div class="custom-footer">
        © 2025 William Cubero | Todos los derechos reservados
    </div>
""", unsafe_allow_html=True)

# 🧠 Título
st.title("📊 Análisis de Ventas con Inteligencia Artificial")

# 📘 Instrucciones
with st.expander("📘 Ver instrucciones"):
    st.markdown("""
    Esta app analiza un archivo `.csv` o `.pdf` con datos de ventas y aplica un modelo de IA para predecir ingresos futuros.

    **Requisitos del archivo:**
    - `Cantidad` y `Precio Unitario` (obligatorios)
    - `Fecha` (opcional pero recomendada)
    - `Producto`, `Categoria` (opcionales para filtros)
    """)

# 📥 Archivos de ejemplo
with st.sidebar:
    st.markdown("📥 ¿No tenés archivo?")
    if os.path.exists("ventas.csv"):
        with open("ventas.csv", "rb") as f_csv:
            st.download_button("📄 CSV", f_csv, "ejemplo_ventas.csv", "text/csv")
    if os.path.exists("ventas.pdf"):
        with open("ventas.pdf", "rb") as f_pdf:
            st.download_button("📄 PDF", f_pdf, "ejemplo_ventas.pdf", "application/pdf")

# 📁 Subida de archivo
archivo = st.file_uploader("📁 Subí tu archivo CSV o PDF", type=["csv", "pdf"])

if archivo is not None:
    try:
        if archivo.name.lower().endswith(".csv"):
            df = pd.read_csv(archivo)
        elif archivo.name.lower().endswith(".pdf"):
            with open("temp.pdf", "wb") as f:
                f.write(archivo.read())
            df = extraer_tabla_pdf("temp.pdf")
        else:
            st.error("❌ Tipo de archivo no soportado.")
            st.stop()

        if df.empty:
            st.warning("⚠️ No se encontraron datos válidos.")
            st.stop()

        # 🧹 Limpieza
        if "Fecha" in df.columns:
            df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
            df = df[df["Fecha"].notna()]

        for col in ["Cantidad", "Precio Unitario"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        df = df.dropna(subset=["Cantidad", "Precio Unitario"])

        # 👁 Vista previa
        st.markdown("### 🗂️ Vista previa del archivo")
        st.dataframe(df.head())
        st.markdown(f"**Columnas detectadas:** {df.columns.tolist()}")

        # 🎛 Filtros
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown("## 🎛️ Filtros")
            if "Producto" in df.columns:
                productos = df["Producto"].dropna().unique()
                seleccionados = st.multiselect("Filtrar por producto", productos, default=list(productos))
                df = df[df["Producto"].isin(seleccionados)]

            if "Categoria" in df.columns:
                categorias = df["Categoria"].dropna().unique()
                seleccionadas = st.multiselect("Filtrar por categoría", categorias, default=list(categorias))
                df = df[df["Categoria"].isin(seleccionadas)]

            if "Fecha" in df.columns and not df["Fecha"].empty:
                fmin = df["Fecha"].min().date()
                fmax = df["Fecha"].max().date()
                fechas = st.date_input("Filtrar por rango de fechas", [fmin, fmax])
                if len(fechas) == 2:
                    f1 = pd.to_datetime(fechas[0])
                    f2 = pd.to_datetime(fechas[1])
                    df = df[(df["Fecha"] >= f1) & (df["Fecha"] <= f2)]

        # 📈 Análisis
        with col2:
            if "Cantidad" in df.columns and "Precio Unitario" in df.columns:
                df["Ingreso Total"] = df["Cantidad"] * df["Precio Unitario"]

                st.markdown("## 📊 Estadísticas Generales")
                st.dataframe(df.describe())

                if "Categoria" in df.columns:
                    st.markdown("### 💼 Ingresos por Categoría")
                    resumen = df.groupby("Categoria")["Ingreso Total"].sum()
                    fig1, ax1 = plt.subplots()
                    resumen.plot(kind="bar", ax=ax1)
                    ax1.set_ylabel("Colones")
                    st.pyplot(fig1)

                if "Fecha" in df.columns:
                    st.markdown("### 📅 Ingresos por Fecha")
                    ingresos_fecha = df.groupby("Fecha")["Ingreso Total"].sum()
                    fig2, ax2 = plt.subplots(figsize=(10, 4))
                    ingresos_fecha.plot(ax=ax2)
                    ax2.set_ylabel("Colones")
                    st.pyplot(fig2)

                # 🔮 Predicción
                st.markdown("## 🔮 Predicción de Ingresos (IA)")
                df_pred = df[["Fecha", "Ingreso Total"]].dropna()
                df_pred = df_pred.groupby("Fecha").sum().reset_index()

                if not df_pred.empty and df_pred["Fecha"].notna().all():
                    df_pred["Fecha_Ordinal"] = df_pred["Fecha"].map(datetime.toordinal)
                    X = df_pred[["Fecha_Ordinal"]]
                    y = df_pred["Ingreso Total"]
                    modelo = LinearRegression().fit(X, y)

                    ultima_fecha = df_pred["Fecha"].max()
                    fechas_futuras = [ultima_fecha + timedelta(days=i) for i in range(1, 31)]
                    fechas_ordinal = np.array([f.toordinal() for f in fechas_futuras]).reshape(-1, 1)
                    ingresos_pred = modelo.predict(fechas_ordinal)

                    df_forecast = pd.DataFrame({
                        "Fecha": fechas_futuras,
                        "Ingreso_Pronosticado": ingresos_pred.round(2)
                    })

                    st.dataframe(df_forecast)

                    st.markdown("### 📉 Gráfico de Predicción (30 días)")
                    fig3, ax3 = plt.subplots()
                    ax3.plot(df_forecast["Fecha"], df_forecast["Ingreso_Pronosticado"], color="green", marker="o")
                    ax3.set_ylabel("Colones")
                    ax3.set_xlabel("Fecha")
                    ax3.set_title("Ingresos Pronosticados")
                    plt.xticks(rotation=45)
                    st.pyplot(fig3)
                else:
                    st.warning("⚠️ No hay suficientes datos válidos para entrenar el modelo de predicción.")
            else:
                st.warning("⚠️ El archivo necesita columnas 'Cantidad' y 'Precio Unitario'.")
    except Exception as e:
        st.error(f"❌ Error al procesar archivo: {e}")
else:
    st.info("👈 Subí tu archivo CSV o PDF para comenzar.")
