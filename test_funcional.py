import tempfile
import unittest
from pathlib import Path
import yaml
from Funcional import RETOS_FUNCIONALES, cargar_preguntas, combinar_preguntas


class PruebasFuncionales(unittest.TestCase):
    def test_diez_retos_con_campos_validos(self):
        self.assertEqual(len(RETOS_FUNCIONALES), 10)
        self.assertEqual(len({p['title'] for p in RETOS_FUNCIONALES}), 10)
        for p in RETOS_FUNCIONALES:
            self.assertTrue(all(p.get(k) for k in ('title', 'prompt', 'hints', 'tags')))

    def test_sin_mutar_entrada(self):
        originales = [{'title': 'Inicial'}]
        resultado = combinar_preguntas(originales, RETOS_FUNCIONALES)
        self.assertEqual(len(originales), 1)
        self.assertEqual(len(resultado), 11)

    def test_creacion_idempotente_y_preservacion(self):
        with tempfile.TemporaryDirectory() as tmp:
            ruta = Path(tmp) / 'problems.yaml'
            ruta.write_text('- title: Inicial\n  prompt: Ya existe\n  hints: [a]\n  tags: [b]\n', encoding='utf-8')
            self.assertEqual(cargar_preguntas(ruta), 10)
            self.assertEqual(cargar_preguntas(ruta), 0)
            datos = yaml.safe_load(ruta.read_text(encoding='utf-8'))
            self.assertEqual(len(datos), 11)
            self.assertEqual(datos[0]['title'], 'Inicial')


if __name__ == '__main__':
    unittest.main()
