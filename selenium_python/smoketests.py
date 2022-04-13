from unittest import TestLoader, TestSuite, runner
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests import SearchTests

# cargando los casos de pruebas para ejecutarlos al mismo
# tiempo
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

# lista de las variables donde cargamos las pruebas
smoke_test = TestSuite([assertions_test, search_test])

# paramatros para generar nuestro reporte
kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)