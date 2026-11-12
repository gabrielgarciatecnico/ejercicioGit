"""Carga funcional e idempotente de retos de Python en problems.yaml."""
from pathlib import Path
from typing import Dict, List, Optional

import yaml


RETOS_FUNCIONALES: List[Dict] = [
    {"title": "Filtrar números pares", "prompt": "Implementa `pares(numeros)` que devuelva solo los elementos pares de una lista.", "hints": ["Usa filter o una comprensión", "Un número par cumple n % 2 == 0"], "tags": ["funciones", "listas", "filtros"]},
    {"title": "Elevar al cuadrado", "prompt": "Implementa `cuadrados(numeros)` que transforme cada número en su cuadrado.", "hints": ["Usa map o una comprensión", "No modifiques la lista original"], "tags": ["funciones", "map", "listas"]},
    {"title": "Sumar con reduce", "prompt": "Implementa `total(numeros)` usando `functools.reduce` para sumar los elementos.", "hints": ["Importa reduce desde functools", "Considera la lista vacía"], "tags": ["reduce", "funciones", "aritmética"]},
    {"title": "Contar palabras", "prompt": "Implementa `frecuencias(texto)` que devuelva un diccionario con la frecuencia de cada palabra.", "hints": ["Normaliza mayúsculas y minúsculas", "Separa el texto en palabras"], "tags": ["diccionarios", "strings", "funciones"]},
    {"title": "Eliminar duplicados conservando orden", "prompt": "Implementa `unicos(valores)` que elimine elementos repetidos sin cambiar el orden de aparición.", "hints": ["Puedes llevar un conjunto auxiliar", "Conserva la primera aparición"], "tags": ["listas", "conjuntos", "funciones"]},
    {"title": "Composición de funciones", "prompt": "Implementa `componer(f, g)` que devuelva una función que calcule f(g(x)).", "hints": ["Devuelve una función interna o lambda", "Primero ejecuta g"], "tags": ["funciones", "orden-superior", "composición"]},
    {"title": "Ordenar por segunda componente", "prompt": "Implementa `ordenar_pares(pares)` que ordene tuplas `(nombre, nota)` de menor a mayor nota.", "hints": ["Usa sorted", "Define key con una función lambda"], "tags": ["sorted", "lambda", "tuplas"]},
    {"title": "Agrupar por longitud", "prompt": "Implementa `agrupar_longitud(palabras)` que agrupe palabras por cantidad de caracteres.", "hints": ["Usa un diccionario", "La clave puede ser len(palabra)"], "tags": ["diccionarios", "strings", "funciones"]},
    {"title": "Generador de Fibonacci", "prompt": "Implementa `fibonacci(n)` como generador que produzca los primeros n números de Fibonacci.", "hints": ["Utiliza yield", "Actualiza los dos valores previos en cada iteración"], "tags": ["generadores", "yield", "secuencias"]},
    {"title": "Pipeline de transformación", "prompt": "Implementa una función que reciba números, conserve los positivos, los duplique y devuelva su suma.", "hints": ["Combina filter, map y sum", "Evita modificar los datos de entrada"], "tags": ["funciones", "pipeline", "map", "filter"]},
]


def combinar_preguntas(actuales: List[Dict], nuevas: List[Dict]) -> List[Dict]:
    """Devuelve una nueva lista sin títulos duplicados; no muta entradas."""
    if not isinstance(actuales, list):
        raise ValueError("problems.yaml debe contener una lista de preguntas")
    if not all(isinstance(item, dict) and isinstance(item.get("title"), str) for item in actuales):
        raise ValueError("Las preguntas existentes deben tener un campo title de texto")
    titulos = {item["title"].strip().casefold() for item in actuales}
    pendientes = [item for item in nuevas if item["title"].strip().casefold() not in titulos]
    return [*actuales, *pendientes]


def cargar_preguntas(ruta: Optional[Path] = None) -> int:
    """Agrega los diez retos si faltan. Retorna la cantidad agregada."""
    archivo = Path(ruta) if ruta is not None else Path(__file__).resolve().parent / "problems.yaml"
    actuales = yaml.safe_load(archivo.read_text(encoding="utf-8")) if archivo.exists() else []
    actuales = [] if actuales is None else actuales
    resultado = combinar_preguntas(actuales, RETOS_FUNCIONALES)
    agregadas = len(resultado) - len(actuales)
    if agregadas:
        archivo.write_text(yaml.safe_dump(resultado, allow_unicode=True, sort_keys=False, width=100), encoding="utf-8")
    return agregadas
