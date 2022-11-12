'''Вариант 1'''

from collections import defaultdict

n, m = map(int,input().split())
A = defaultdict(list)
B = defaultdict(list)


for _ in range(n):
    A[1].append(input()) # создаем словарь {произвольный индекс:список веденных значений}
    
for _ in range(m):
    B[1].append(input()) # создаем словарь {произвольный индекс:список веденных значений}
    

for i in B[1]:
    answer = [] # контейнер для вывода ответа согласно условию задачи
    if i not in A[1]: # выполняем условие задачи "If the word, does not appear in group A"
        print(-1)
    else:
        for j in range(len(A[1])):
            if i == A[1][j]:
                answer.append(j+1) # смена выводимого индекса согласно условию задачи
        print(*answer)

''' Вариант 2: с другим способом формирования словаря и отказом от искусственной инкрементации выводимых индексов'''

from collections import defaultdict

n, m = map(int,input().split())
A = defaultdict(str)
B = defaultdict(str)


for i in range(1, n+1): # создаем словарь {порядковый номер:введенная строка}
    A[i] = input()

for i in range(1, m+1):
    B[i] = input()

for i in B:
    if B[i] not in A.values(): # выполняем условие задачи "If the word, does not appear in group A"
        print(-1)
    else:
        for j in A:
            if B[i] == A[j]:
                print(j, end=' ')
        print()
                
