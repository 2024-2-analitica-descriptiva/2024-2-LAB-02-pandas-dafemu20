"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd  # type: ignore

def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna `c1` del
    archivo `tbl0.tsv`?

    Rta/
    c1
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: count, dtype: int64

    """
    data = pd.read_csv("files/input/tbl0.tsv", sep='\t')

    # Contar la cantidad de registros por cada letra en la columna 'c1'
    conteo_c1 = data['c1'].value_counts().sort_index()

    print(conteo_c1)

    return conteo_c1

pregunta_03()