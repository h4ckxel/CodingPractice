import random
import time
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_aort import insertion_sort as injerto
from shellShort import shellShort as Shelly

huarache = [random.randint(1, 1000) for _ in range(20000)]

# ordenamiento burbuja
inicio = time.time()
bubble_sort(huarache)
fin = time.time()
print(f"\nOrdenamiento por Burbuja. Tiempo: {fin - inicio: .10f} segundos")

# ordenamiento selection sort
inicio = time.time()
selection_sort(huarache)
fin = time.time()
print(f"\nOrdenamiento por Selection Sort. Tiempo: {fin - inicio: .10f} segundos")

# ordenamiento sorted python
inicio = time.time()
sorted(huarache)
fin = time.time()
print(f"\nOrdenamiento por Sorted(Python). Tiempo: {fin - inicio: .10f} segundos")

# ordenamiento injerto
inicio = time.time()
injerto(huarache)
fin = time.time()
print(f"\nOrdenamiento por Injerto. Tiempo: {fin - inicio: .10f} segundos\n")

# ordenamiento shell
inicio = time.time()
Shelly(huarache)
fin = time.time()
print(f"\nOrdenamiento por Shell Short. Tiempo: {fin - inicio: .10f} segundos\n")
