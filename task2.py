# Даны N городов и M дорог между ними. Дороги двусторонние (граф неориентированный). 
# Известно, что города разделены на группы (острова), 
# между которыми дорог нет. То есть граф состоит из нескольких компонент связности (островов). 
# Необходимо ответить на следующие вопросы:
# 
# 1. Есть ли путь между двумя заданными городами (вершинами)?
# 2. Сколько всего островов (компонент связности) в графе?
# 3.Перечислить, какие города принадлежат каждому острову.
# 
# Входные данные:
# Первая строка: N (количество городов) и M (количество дорог).
# Следующие M строк: пары чисел u и v, обозначающие дорогу между городами u и v.
# Затем вводится два числа: start и end — номера городов, между которыми нужно проверить наличие пути.
# 
# Выходные данные:
# Ответ на вопрос, есть ли путь между start и end ("YES" или "NO").
# Количество островов (компонент связности) в графе.
# Список городов для каждого острова (в порядке возрастания номеров островов).
from re import purge

from PIL.ImImagePlugin import split

# Пример 1:
# 5 3
# 1 2
# 2 3
# 4 5
# 1 4
# 
# Ожидаемый вывод:
# 
# NO
# 2
# 1: [1, 2, 3]
# 2: [4, 5]

# Пример 2:
# 6 4
# 1 2
# 3 4
# 5 6
# 2 3
# 3 5
# 
# Ожидаемый вывод:
# 
# YES
# 1
# 1: [1, 2, 3, 4, 5, 6]

# Пример 3:
# 7 0
# 1 2
# 
# Ожидаемый вывод:
# 
# NO
# 7
# 1: [1]
# 2: [2]
# 3: [3]
# 4: [4]
# 5: [5]
# 6: [6]
# 7: [7]
print('Enter the number of cities and roads')
pre=input()
numtowns=int(pre.split()[0])
numroads=int(pre.split()[1])
print('Enter roads')
roads=[]
for i in range(numroads):
    preroads=input()
    roads.append([int(preroads.split()[0]),int(preroads.split()[1])])
print('Enter specific cities')
pretowns=input()
towns=[int(pretowns.split()[0]),int(pretowns.split()[1])]
print(roads, towns)
my_dict={}
for i in range(numtowns):
    my_dict[int(i+1)]=[]
for i in range(numroads):
    my_dict[int(roads[i][0])].append(roads[i][1])
    my_dict[int(roads[i][1])].append(roads[i][0])
one_list_to_rule_them_all=[]
for h in range(1, numtowns+1):
    start = h
    path=[]
    path.append(start)
    C=1
    while True:
        c=1
        while c==1:
            c=0
            for i in range(len(my_dict[path[-C]])):
                if i<len(my_dict[path[-C]]):
                    if my_dict[path[-C]][i] not in path:
                        path.append(my_dict[path[-C]][i])
                        c=1
                        C=1
                        break
            if c==0:
                C+=1
            print(path, C)
        if len(path)>=numtowns:
            one_list_to_rule_them_all.append(sorted(path))
            break
print(one_list_to_rule_them_all)
purified_list=[]
for i in range(numtowns):
    if one_list_to_rule_them_all[i] not in purified_list:
        purified_list.append(one_list_to_rule_them_all[i])
print(purified_list)
a=0
b=0
for i in range(len(purified_list)):
    if towns[0] in purified_list[i]:
        a=i
    if towns[1] in purified_list[i]:
        b=i
if a==b:
    print('YES')
else:
    print('NO')
print(len(purified_list))
for i in range(len(purified_list)):
    print(i+1, purified_list[i])