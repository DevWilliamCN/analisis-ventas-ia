import pdfplumber
import pandas as pd

def extraer_tabla_pdf(file) -> pd.DataFrame:
    """
    Extrae la primera tabla válida de un archivo PDF y la convierte en un DataFrame estructurado.
    Intenta convertir columnas numéricas y de fecha automáticamente.

    :param file: archivo PDF cargado desde Streamlit o ruta local
    :return: DataFrame con la tabla estructurada o vacío si no se encuentra
    """
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                tablas = page.extract_tables()
                if tablas:
                    tabla = tablas[0]
                    if len(tabla) > 1:
                        headers = [col.strip() if col else f"Col_{i}" for i, col in enumerate(tabla[0])]
                        filas = tabla[1:]

                        df = pd.DataFrame(filas, columns=headers)

                        # Limpiar espacios en los nombres de columnas
                        df.columns = df.columns.str.strip()

                        # Convertir columnas específicas si existen
                        for col in df.columns:
                            if col.lower() in ["cantidad", "precio unitario"]:
                                df[col] = pd.to_numeric(df[col].str.replace(",", "").str.strip(), errors="coerce")
                            elif col.lower() == "fecha":
                                df[col] = pd.to_datetime(df[col].str.strip(), errors="coerce")

                        df = df.dropna(how="all")  # Eliminar filas vacías
                        return df

        return pd.DataFrame()
    except Exception as e:
        raise RuntimeError(f"Error al procesar el PDF: {e}")
