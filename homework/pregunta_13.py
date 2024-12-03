"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""
import pandas as pd

def pregunta_13():
    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """

    data = pd.read_csv("files/input/tbl0.tsv", sep="\t")

    data_tbl2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")

    # Hacer merge entre tbl0 y tbl2 usando 'c0' como clave
    merged_data = data.merge(data_tbl2, on='c0')

    # Calcular la suma de 'c5b' por cada valor en 'c1'
    suma_c5b_por_c1 = merged_data.groupby('c1')['c5b'].sum()

    print(suma_c5b_por_c1)


    return suma_c5b_por_c1

pregunta_13()
