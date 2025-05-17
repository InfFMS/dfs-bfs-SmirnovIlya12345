# Дан взвешенный граф.
# Необходимо ответить на следующие вопросы:
# 
# 1. Найти длину всех наикротчайших маршрутов из 'Home' в любую точку на графе? (Просто применить алгоритм Дейкстры)
# 2. Найту как выглядит самый кротчайший маршрут из 'Home' в 'Theater' (вывести последовательность прохождения вершин)?
# Подсказка:
# Удобно хранить значения о пройденном маршруте в виде словаря, где ключ - это текущая вершина, а значение - вершина, из которой мы попали в текущую
# Потом в конце нужно будет просто пройтись по такому словарю от финиша к старту и развернуть его.
#
# Входные данные:

city_map = {
    'Home': {'Park': 2, 'School': 5, 'Mail': 10},
    'Park': {'Home': 2, 'Museum': 4, 'Cafe': 3},
    'School': {'Home': 5, 'Library': 6, 'Mail': 2},
    'Mail': {'Home': 10, 'School': 2, 'Hospital': 3},
    'Library': {'School': 6, 'Hospital': 1},
    'Hospital': {'Library': 1, 'Mail': 3, 'Office': 4},
    'Cafe': {'Park': 3, 'Theater': 8, 'Office': 7},
    'Museum': {'Park': 4, 'Shop': 5},
    'Shop': {'Museum': 5, 'Theater': 1},
    'Theater': {'Shop': 1, 'Cafe': 8},
    'Office': {'Cafe': 7, 'Hospital': 4}
}
finish='Theater'
optimum={}
for i in range(len(city_map)):
    optimum[list(city_map)[i]]=1000000+i
optimum[list(city_map)[0]]=0
last={}
for i in range(len(list(optimum))):
    last[list(optimum)[i]]=0
for I in range(len(optimum)):
    for j in range(len(optimum)):
        for k in range(len(city_map[list(city_map)[j]])):
            if optimum[list(city_map)[j]]>optimum[list(city_map[list(city_map)[j]])[k]]+list(city_map[list(city_map)[j]].values())[k]:
                optimum[list(city_map)[j]]=optimum[list(city_map[list(city_map)[j]])[k]]+list(city_map[list(city_map)[j]].values())[k]
                last[list(optimum)[j]]=list(city_map[list(optimum)[j]])[k]
print(optimum)
print(last)
way=[]
f=finish
while f!=0:
    way.append(f)
    f=last[f]
print(way)
