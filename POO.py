import os
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
        """Convierte la instancia en un diccionario apto para YAML."""
        return {
            "title": self.title,
            "prompt": self.prompt,
            "hints": self.hints,
            "tags": self.tags
        }

    def __repr__(self) -> str:
        return f"Question(title='{self.title}', tags={self.tags})"


class QuestionManager:
    """Clase gestora para administrar, transformar y guardar el banco de preguntas."""
    
    def __init__(self, filepath: Path = PROBLEMS_PATH):
        self.filepath = filepath
        self.questions: List[Question] = []

    def load_raw_questions(self, raw_data: List[Dict[str, Any]]) -> None:
        """
        Carga datos crudos aplicando Programación Funcional 
        mediante `map` y expresiones `lambda`.
        """
        self.questions = list(
            map(
                lambda d: Question(
                    title=d.get("title", ""),
                    prompt=d.get("prompt", ""),
                    hints=d.get("hints", []),
                    tags=d.get("tags", [])
                ),
                raw_data
            )
        )

    def get_serialized_questions(self) -> List[Dict[str, Any]]:
        """
        Serializa la lista de objetos Question a diccionarios 
        usando Programación Funcional (`map`).
        """
        return list(map(lambda q: q.to_dict(), self.questions))

    def guardar_en_yaml(self) -> None:
        """Guarda el banco completo de preguntas en el archivo YAML."""
        if yaml is None:
            raise RuntimeError("PyYAML no está instalado. Instálalo con 'pip install PyYAML'.")
        
        data = self.get_serialized_questions()
        with self.filepath.open("w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)
        print(f"¡Éxito! Se han guardado {len(data)} preguntas en {self.filepath.name}")


def cargar_preguntas() -> None:
    """
    Función requerida para inicializar y registrar las 10 preguntas 
    en problems.yaml utilizando POO y Programación Funcional.
    """
    # Banco con las 10 preguntas enriquecidas para Ciencia de Datos / Python Avanzado
    datos_iniciales = [
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
            "hints": ["Combina `filter` para la condición y `map` para la transformación", "Recuerda convertir el resultado final a una lista antes de retornarlo"],
            "tags": ["programación-funcional", "map", "filter"]
        }
    ]

    # Instanciación y ejecución del flujo orientado a objetos y funcional
    manager = QuestionManager()
    manager.load_raw_questions(datos_iniciales)
    manager.guardar_en_yaml()


if __name__ == "__main__":
    cargar_preguntas()