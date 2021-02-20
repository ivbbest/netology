c = [[1, 2], [3, 4], [5, 6]]
# Давайте преобразуем эту матрицу в одномерный список
import itertools as it
newlist = list(it.chain.from_iterable(c))
print(newlist)
