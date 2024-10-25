# hw_otsu_method

Основной файл проекта — main. Там лежит алгоритм Оцу вместе со всеми необходимыми функциями.

Следующая команда запустит скрипт:
```bash
python main.py
```
Он выведет результат работы на одной из картинок в консоль.

Команды для запуска тестов. 

Чтобы тесты работали, нужно поменять путь до папки с картинками в файле **config.py**
```bash
python -m unittest tests/contrast_test.py
```
```bash
python -m unittest tests/empty_test.py
```
```bash
python -m unittest tests/silhouette_test.py
```
```bash
python -m unittest tests/noise_test.py
```
```bash
python -m unittest tests/vladimir_vladimirovich_test.py
```
```bash
python -m unittest tests/xray_test.py
```
```bash
python -m unittest tests/stars_test.py
```
Тесты представляют из себя вывод картинок (оригинальной, обработанной написанным методом и библиотечным методом Оцу)
При закрытии картинки будет сам тест: попиксельное сравнение библиотечного решения и разработанного. Взял погрешность 
(количество несовпадающих пикселей) в 1%

****
