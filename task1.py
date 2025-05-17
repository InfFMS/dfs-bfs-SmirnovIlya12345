# Напишите алгоритм поиска в глубину (DFS)
#
# Формат входных данных:
# Граф задаётся в виде словаря, где ключи — вершины, а значения — списки смежных вершин.
#
# Обход начинается с заданной стартовой вершины.
# Требуется:
# 1.Реализовать DFS (Depth-First Search) — обход графа в глубину.
# 2.Вернуть список вершин в порядке их посещения.
from os import remove

# Пример входных данных
graph = {
     1: [2, 3],
     2: [1, 4, 6],
     3: [1, 5],
     4: [2],
     5: [3],
     6: [7, 8, 9],
     7: [8],
     8: [1],
     9: [10],
     10: [6]
 }
start = 1
path=[]
path.append(start)
C=1
while True:
    c=1
    while c==1:
        c=0
        for i in range(len(graph[path[-C]])):
            if graph[path[-C]][i] not in path:
                path.append(graph[path[-C]][i])
                c=1
                C=1
                break
        if c==0:
            C+=1
        print(path, C)
    if len(path)<C:
        break
