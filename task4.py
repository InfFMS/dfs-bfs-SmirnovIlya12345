# Дан список курсов университета и их пререквизитов. Нужно определить,
# можно ли окончить все курсы, и если да, то вывести один из возможных порядков их изучения.
#
# Формат ввода:
# Первая строка: n (число курсов), m (число зависимостей).
# Следующие m строк: a b (курс b требует прохождения курса a).
#
# Формат вывода:
# Если циклов нет, вывести любой допустимый порядок курсов.
# Если есть цикл, вывести -1.

# Пример 1 (нет циклов)
# Ввод:
# 4 3
# 1 2
# 2 3
# 1 4
# Граф:
# 1 → 2 → 3
# 1 → 4
# Вывод:
# 1 2 4 3  # Или 1 4 2 3

# Пример 2 (есть цикл)
# Ввод:
# 3 3
# 1 2
# 2 3
# 3 1
# Граф:
# 1 → 2 → 3 → 1 (цикл!)
# Вывод:
# -1
print('Enter the number of courses and dependences')
pre=input()
numcor=int(pre.split()[0])
numdep=int(pre.split()[1])
print('Enter dependences')
deps=[]
for i in range(numdep):
    preroads=input()
    deps.append([int(preroads.split()[0]),int(preroads.split()[1])])
print(numcor,numdep,deps)
free=[]
order=[]
c=0
while len(order)<numcor:
    for i in range(1,numcor+1):
        if i not in order:
            c=0
            for j in range(len(deps)):
                if deps[j][1]==i and deps[j][0] not in order:
                    c=1
                    break
            if c==0:
                free.append(i)
    if free==[]:
        print(-1)
        break
    else:
        print(free,order)
        order.append(free[0])
        free.remove(free[0])
if len(order)==numcor:
    print(order)
