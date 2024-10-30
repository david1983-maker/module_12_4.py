import unittest
from module_12_3 import *
import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            a1 = Runner('max', -10)
            for i in range(10):
                a1.walk()

            self.assertEqual(a1.distance, 50)
            logging.info('test_walk  выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner')

    def test_run(self):
        try:
            a1 = Runner(10)
            for i in range(10):
                a1.run()

            self.assertEqual(a1.distance, 100)
            logging.info('test_run выполнен успешно')
        except:
            logging.warning('Неверный тип данных для обьекта')

    def test_chalLenge(self):
        a1 = Runner('david')
        a2 = Runner('max')
        for i in range(10):
            a1.run()

        for i in range(10):
            a2.walk()
        self.assertNotEqual(a1.distance, a2.distance)


if __name__ == '__main__':
    unittest.main()
    
