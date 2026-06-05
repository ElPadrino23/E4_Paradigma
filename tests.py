import unittest

from funcional import (
    cargar_series,
    por_genero,
    por_calificacion,
    ordenar,
    formatear,
    recomendar
)

from orientada_objetos import Serie, Catalogo


class TestFuncional(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.series = cargar_series('series.csv')

    def test_01_cargar_datos(self):
        self.assertGreater(len(self.series), 0)

    def test_02_estructura_datos(self):

        serie = self.series[0]

        self.assertIn('nombre', serie)
        self.assertIn('genero', serie)
        self.assertIn('calificacion', serie)
        self.assertIn('ano', serie)

    def test_03_filtro_genero(self):

        resultado = por_genero(['drama'])(self.series)

        self.assertGreater(len(resultado), 0)

        for serie in resultado:
            self.assertEqual(serie['genero'], 'drama')

    def test_04_filtro_genero_multiple(self):

        resultado = por_genero(
            ['drama', 'sci-fi']
        )(self.series)

        for serie in resultado:
            self.assertIn(
                serie['genero'],
                ['drama', 'sci-fi']
            )

    def test_05_filtro_genero_vacio(self):

        resultado = por_genero(
            ['noexiste']
        )(self.series)

        self.assertEqual(len(resultado), 0)

    def test_06_filtro_calificacion(self):

        resultado = por_calificacion(
            9.0
        )(self.series)

        for serie in resultado:
            self.assertGreaterEqual(
                serie['calificacion'],
                9.0
            )

    def test_07_filtro_calificacion_vacio(self):

        resultado = por_calificacion(
            10.5
        )(self.series)

        self.assertEqual(len(resultado), 0)

    def test_08_ordenamiento(self):

        resultado = ordenar(self.series)

        for i in range(len(resultado) - 1):

            actual = resultado[i]
            siguiente = resultado[i + 1]

            self.assertGreaterEqual(
                actual['calificacion'],
                siguiente['calificacion']
            )

    def test_09_no_mutacion(self):

        copia_original = self.series.copy()

        ordenar(self.series)

        for i in range(len(copia_original)):
            self.assertEqual(
                copia_original[i]['nombre'],
                self.series[i]['nombre']
            )

    def test_10_formateo(self):

        primeras_series = self.series[:3]

        resultado = formatear(primeras_series)

        self.assertEqual(len(resultado), 3)

        for texto in resultado:
            self.assertIn('|', texto)
            self.assertIn('Calificacion:', texto)

    def test_11_pipeline_drama(self):

        resultado = recomendar(
            self.series,
            ['drama'],
            8.5
        )

        self.assertGreater(len(resultado), 0)

    def test_12_pipeline_vacio(self):

        resultado = recomendar(
            self.series,
            ['noexiste'],
            8.0
        )

        self.assertEqual(len(resultado), 0)

    def test_13_currying(self):

        filtro_drama = por_genero(['drama'])
        filtro_scifi = por_genero(['sci-fi'])

        resultado_drama = filtro_drama(self.series)
        resultado_scifi = filtro_scifi(self.series)

        self.assertNotEqual(
            len(resultado_drama),
            len(resultado_scifi)
        )

    def test_14_composicion(self):

        filtradas = por_genero(
            ['drama']
        )(self.series)

        resultado = por_calificacion(
            8.5
        )(filtradas)

        self.assertGreater(len(resultado), 0)

    def test_15_orden_final(self):

        resultado = recomendar(
            self.series,
            ['drama', 'sci-fi'],
            8.0
        )

        if len(resultado) > 1:

            calificaciones = [
                float(
                    texto.split(
                        "Calificacion: "
                    )[1]
                )
                for texto in resultado
            ]

            for i in range(len(calificaciones) - 1):
                self.assertGreaterEqual(
                    calificaciones[i],
                    calificaciones[i + 1]
                )


class TestOOP(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.catalogo = Catalogo('series.csv')

    def test_serie(self):

        serie = Serie(
            'Test',
            'drama',
            9.0,
            2020
        )

        self.assertEqual(
            serie.nombre,
            'Test'
        )

    def test_catalogo_carga(self):

        self.assertGreater(
            len(self.catalogo.series),
            0
        )

    def test_filtro_oop(self):

        resultado = self.catalogo.filtrar_genero(
            ['drama']
        )

        self.assertGreater(
            len(resultado.series),
            0
        )

    def test_chaining(self):

        resultado = (
            self.catalogo
            .filtrar_genero(['drama'])
            .filtrar_calificacion(8.5)
            .ordenar()
        )

        self.assertGreater(
            len(resultado.series),
            0
        )

    def test_equivalencia(self):

        series = cargar_series('series.csv')

        resultado_funcional = recomendar(
            series,
            ['drama'],
            8.5
        )

        resultado_oop = self.catalogo.recomendar(
            ['drama'],
            8.5
        )

        self.assertEqual(
            len(resultado_funcional),
            len(resultado_oop)
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
