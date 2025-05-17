# Реализовать алгоритм Кана для топологической сортировки
# Пример с пошаговой работой алгоритма
# Граф: A → B → C
#       A → D
from time import sleep

graf = {1 : [2, 3],
        2 : [3],
        3 : [],
        4 : []}

# Шаги:
# 1. Начальные вершины без входящих рёбер: [A]
# 2. Обрабатываем A → результат [A], обновляем степени B(1→0), D(1→0)
# 3. Вершины для обработки: [B, D]
# 4. Обрабатываем B → результат [A,B], обновляем степень C(1→0)
# 5. Обрабатываем D → результат [A,B,D]
# 6. Обрабатываем C → результат [A,B,D,C]
# 7. Все вершины обработаны → сортировка завершена
may_there_be=[]
len0=len(graf)
for h in range(1, len(graf)+1):
    c=0
    for i in range(1, len(graf)+1):
        if graf[i]!=[]:
            for j in range(len(graf[i])):
                if graf[i][j]==h:
                    c=1
                    break
    if c==0:
        may_there_be.append(h)
journey=[]
while may_there_be!=[]:
    journey.append(may_there_be[0])
    print(journey, may_there_be, 'a')
    print(graf, 'b')
    sleep(0.1)
    del graf[may_there_be[0]]
    may_there_be.remove(may_there_be[0])
    print(i in graf, 'c')
    for h in range(1, len0):
        if h in graf:
            c = 0
            for i in range(1, len(graf) + 1):
                if i in graf:
                    if graf[i] != []:
                        for j in range(len(graf[i])):
                            if graf[i][j] == h:
                                c = 1
                                break
            if c==0:
                may_there_be.insert(0,h)
        else:
            pass