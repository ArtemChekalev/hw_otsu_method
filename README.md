# hw_otsu_method

Основной файл проекта — main. Там лежит алгоритм Оцу вместе со всеми необходимыми функциями.

Описание алгоритма:
1. Изображение переводится из rgb в grayscale при помощи image_to_gray_scale()
2. Рассчитывается гистограмма изображения при помощи count_histogram()
3. Находится оптимальный порог при помощи otsu_threshold(): перебираются все пороги от 1 до 256 и находится тот, при котором межклассовая дисперсия максимальна
4. С найденным порогом выполняется бинаризация изображения функцией binarize_image()

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
