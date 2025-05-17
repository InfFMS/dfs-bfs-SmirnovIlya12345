# Напишите алгоритм поиска в ширину (BFS)
#
# Формат входных данных:
# Граф задаётся в виде словаря, где ключи — вершины, а значения — списки смежных вершин.
#
# Обход начинается с заданной стартовой вершины.
# Требуется:
# 1.Реализовать BFS — обход графа в ширину.
# 2.Вернуть самый коротки маршрут от точки старта до точки назначения.

# Пример входных данных
city_map = {
    'Home': ['Park', 'School', 'Mail'],
    'Park': ['Home', 'Museum', 'Cafe'],
    'School': ['Home', 'Library', 'Mail'],
    'Mail': ['Home', 'School', 'Hospital'],
    'Library': ['School', 'Hospital'],
    'Hospital': ['Library', 'Mail', 'Office'],
    'Cafe': ['Park', 'Theater', 'Office'],
    'Museum': ['Park', 'Shop'],
    'Shop': ['Museum', 'Theater'],
    'Theater': ['Shop', 'Cafe'],
    'Office': ['Cafe', 'Hospital']
}
start = "Home"
finish = "Theater"
#
# Пример выходных данных
# ['Home', 'Park', 'Cafe', 'Theater']
optimum={}
print(city_map[list(city_map)[0]][0])
print(list(city_map))
for i in range(len(city_map)):
    optimum[list(city_map)[i]]=1000000+i
print(optimum[city_map[list(city_map)[0]][0]])
optimum[list(city_map)[0]]=0
print(optimum[list(city_map)[5]])
last={}
for i in range(len(list(optimum))):
    last[list(optimum)[i]]=0
print(last)
for I in range(len(optimum)):
    for j in range(len(optimum)):
        for k in range(len(city_map[list(city_map)[j]])):
            print(list(city_map)[j])
            if optimum[list(city_map)[j]]>optimum[city_map[list(city_map)[j]][k]]+1:
                optimum[list(city_map)[j]]=optimum[city_map[list(city_map)[j]][k]]+1
                last[list(optimum)[j]]=city_map[list(optimum)[j]][k]
print(optimum)
print(last)
way=[]
f=finish
for i in range(optimum[finish]+1):
    way.append(f)
    f=last[f]
print(way)