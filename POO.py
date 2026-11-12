from pathlib import Path
from typing import List, Dict, Any

try:
    import yaml
except ImportError:
    yaml = None

PROBLEMS_PATH = Path(__file__).parent / "problems.yaml"


class Question:
    """Clase que representa un reto o pregunta de programación (POO)."""
    
    def __init__(self, title: str, prompt: str, hints: List[str], tags: List[str]):
        self.title = title
        self.prompt = prompt
        self.hints = hints
        self.tags = tags

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "prompt": self.prompt,
            "hints": self.hints,
            "tags": self.tags
        }


class QuestionManager:
    """Clase gestora para administrar, validar y fusionar el banco de preguntas."""
    
    def __init__(self, filepath: Path = PROBLEMS_PATH):
        self.filepath = filepath

    def sincronizar_preguntas(self, nuevas_preguntas: List[Dict[str, Any]]) -> None:
        """
        Carga las preguntas existentes y agrega de forma incremental solo las que falten 
        (evitando duplicados), aplicando Programación Funcional (`filter`, `map`).
        """
        if yaml is None:
            raise RuntimeError("PyYAML no está instalado. Instálalo con 'pip install PyYAML'.")
        
        # 1. Cargar preguntas existentes si el archivo existe
        existentes = []
        if self.filepath.exists():
            with self.filepath.open("r", encoding="utf-8") as f:
                existentes = yaml.safe_load(f) or []

        # Obtener los títulos actuales usando programación funcional
        titulos_existentes = set(map(lambda q: q.get("title"), existentes))

        # 2. Filtrar únicamente las preguntas que todavía no estén en el YAML
        preguntas_a_agregar = list(
            filter(lambda q: q.get("title") not in titulos_existentes, nuevas_preguntas)
        )

        if preguntas_a_agregar:
            existentes.extend(preguntas_a_agregar)
            with self.filepath.open("w", encoding="utf-8") as f:
                yaml.dump(existentes, f, allow_unicode=True, sort_keys=False)
            print(f"¡Éxito! Se agregaron {len(preguntas_a_agregar)} preguntas nuevas a {self.filepath.name}.")
        else:
            print("El archivo YAML ya contiene todas las preguntas.")


def cargar_preguntas() -> None:
    """
    Función requerida para registrar las preguntas en problems.yaml 
    utilizando POO y Programación Funcional.
    """
    # Banco completo (1 original + 10 nuevas)
    datos_banco = [
        {
            "title": "Suma dos números",
            "prompt": "Escribe `suma(a, b)` que devuelva a + b.",
            "hints": ["Usa operadores aritméticos", "Devuelve el resultado"],
            "tags": ["funciones", "aritmética"]
        },
        {
            "title": "Filtrar elementos mayores a un umbral",
            "prompt": "Escribe una función `filtrar_mayores(datos, umbral)` que reciba una lista de números y un umbral, y devuelva una nueva lista solo con los elementos mayores al umbral usando programación funcional.",
            "hints": ["Puedes usar la función `filter` con una función lambda", "También se puede resolver con comprensión de listas"],
            "tags": ["funciones", "programación-funcional", "filtrado"]
        },
        {
            "title": "Normalizar lista de valores",
            "prompt": "Escribe una función `normalizar(valores)` que reciba una lista de números y devuelva una nueva lista con los valores normalizados restando el valor mínimo y dividiendo por el rango (max - min).",
            "hints": ["Usa `min()` y `max()` para encontrar los límites", "Maneja el caso donde el rango sea cero para evitar errores de división"],
            "tags": ["matemáticas", "preprocesamiento", "listas"]
        },
        {
            "title": "Promedio móvil simple",
            "prompt": "Escribe una función `promedio_movil(datos, k)` que calcule el promedio móvil de una lista `datos` con una ventana de tamaño `k`.",
            "hints": ["El resultado tendrá una longitud de `len(datos) - k + 1`", "Suma los elementos de cada sub-ventana y divídelos por `k`"],
            "tags": ["series-temporales", "algoritmos", "estadística"]
        },
        {
            "title": "Agrupar por categoría",
            "prompt": "Escribe una función `agrupar_por(registros, clave)` donde `registros` es una lista de diccionarios. La función debe agrupar los diccionarios según el valor de esa clave, devolviendo un diccionario con las agrupaciones.",
            "hints": ["Puedes usar `collections.defaultdict(list)`", "O iterar construyendo las listas asociadas a cada llave"],
            "tags": ["diccionarios", "agrupación", "estructuras-de-datos"]
        },
        {
            "title": "Imputar valores faltantes",
            "prompt": "Escribe una función `imputar_media(datos)` que reciba una lista numérica con posibles valores `None` y devuelva una nueva lista reemplazando los nulos por la media de los valores válidos.",
            "hints": ["Filtra los valores que no sean `None` para calcular la media", "Reemplaza los `None` manteniendo la misma estructura de la lista"],
            "tags": ["limpieza-de-datos", "estadística", "listas"]
        },
        {
            "title": "Generador de lotes (Batches)",
            "prompt": "Escribe un generador en Python llamado `crear_lotes(iterable, tamano)` que divida un iterable en lotes (chunks) de tamaño fijo `tamano`.",
            "hints": ["Usa la palabra clave `yield`", "Puedes recorrer el iterable por pasos o cortando rebanadas (slices)"],
            "tags": ["generadores", "eficiencia", "iteradores"]
        },
        {
            "title": "Aplanar estructura anidada",
            "prompt": "Escribe una función `aplanar(lista_anidada)` que reciba una lista de listas de números y devuelva una única lista con todos los elementos aplanados.",
            "hints": ["Puedes usar una comprensión de listas anidada", "O utilizar herramientas del módulo `itertools`"],
            "tags": ["listas", "recursión", "transformación"]
        },
        {
            "title": "Distancia Euclidiana entre vectores",
            "prompt": "Escribe una función `distancia_euclidiana(v1, v2)` que calcule la distancia euclidiana entre dos tuplas o listas numéricas de la misma longitud.",
            "hints": ["La fórmula es la raíz cuadrada de la suma de las diferencias al cuadrado", "Puedes usar `zip` para emparejar los elementos de ambos vectores"],
            "tags": ["álgebra-lineal", "métricas", "matemáticas"]
        },
        {
            "title": "Procesamiento condicional con funciones de orden superior",
            "prompt": "Escribe una función `procesar_elementos(datos)` que reciba una lista de números, multiplique por 2 los números impares y elimine los menores o iguales a 4, usando `map` y `filter`.",
            "hints": ["Combina `filter` para la condición y `map` para la transformación", "Recuerda convertir el resultado final a lista antes de retornarlo"],
            "tags": ["programación-funcional", "map", "filter"]
        },
        {
            "title": "Detección de valores atípicos (Outliers)",
            "prompt": "Escribe una función `detectar_outliers(datos)` que reciba una lista numérica y devuelva aquellos elementos que se alejen más de 2 desviaciones estándar de la media.",
            "hints": ["Calcula la media y la desviación estándar de la lista", "Filtra los valores cuyo valor absoluto de la diferencia con la media sea mayor a `2 * std`"],
            "tags": ["estadística", "análisis-de-datos", "limpieza"]
        }
    ]

    manager = QuestionManager()
    manager.sincronizar_preguntas(datos_banco)


if __name__ == "__main__":
    cargar_preguntas()