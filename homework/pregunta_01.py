"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

import pandas as pd
import os

INPUT_PATH = "files/input/"
OUTPUT_PATH = "files/output/"


def clean_string(s: str):
    tmp = s.upper()
    ans = tmp.replace("_", " ").replace(".", " ").replace("-", " ")
    return " ".join(ans.split()).strip()


def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    df_credit_req = pd.read_csv(
        os.path.join(INPUT_PATH, "solicitudes_de_credito.csv"), sep=";", index_col=0
    )

    df_clean = df_credit_req.copy().dropna()

    string_cols = [
        "sexo",
        "tipo_de_emprendimiento",
        "idea_negocio",
        "línea_credito",
    ]

    for col in string_cols:
        df_clean[col] = df_clean[col].apply(clean_string).astype("category")

    df_clean["monto_del_credito"] = (
        df_clean["monto_del_credito"]
        .str.replace("$ ", "")
        .str.replace(",", "")
        .astype(float)
    )

    df_clean["estrato"] = df_clean["estrato"].astype("category")

    df_clean["barrio"] = (
        df_clean["barrio"]
        .str.upper()
        .str.replace("_", " ")
        .str.replace("-", " ")
        .astype("category")
    )

    df_clean["fecha_de_beneficio"] = pd.to_datetime(
        df_clean["fecha_de_beneficio"], dayfirst=True, format="mixed"
    )

    df_clean.drop_duplicates(inplace=True)

    # Cargar resultados
    df_clean.to_csv(
        os.path.join(OUTPUT_PATH, "solicitudes_de_credito.csv"), sep=";", index=False
    )
    return df_clean
