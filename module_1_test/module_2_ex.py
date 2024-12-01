
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# is_prime = False
#
# for i in numbers[1:]:
#     #if i / 2 >= 1:
#         #print(i)
#         for j in range(2, i+1):  #i+1
#             #print(i, '   ', j)
#             if i % j == 0 and i / j > 1:
#                 #print('   ', j)
#                 is_prime = False
#                 break
#             else:
#                 is_prime = True
#
#         if is_prime:
#             primes.append(i)
#         else:
#             not_primes.append(i)
#
# print('Primes: ', primes)
# print('Not Primes: ', not_primes)

# for i in numbers:
#     if i / 2 >= 1:
#         for j in range(2, i):
#             if i % j == 0:
#                 is_prime = True
#                 #break
#             else:
#                 is_prime = False
#
#         if is_prime:
#             primes.append(i)
#         else:
#             not_primes.append(i)
#
# print('Primes: ', primes)
# print('Not Primes: ', not_primes)

# for i in numbers:
#     if i / 2 >= 1:
#         #print(i)
#         #while is_prime:
#         for j in range(2, i+1):
#         #print(i, '   ', j)
#             while i % j == 0: #and i / j > 1:
#                 #print('   ', j)
#                 is_prime = False
#                 #break
#             else:
#                 is_prime = True
#
#         if is_prime:
#             primes.append(i)
#         else:
#             not_primes.append(i)
#
# print('Primes: ', primes)
# print('Not Primes: ', not_primes)

#for i in range(1,11):
#    for g in range(2,11):
#        print(i, g)

# import random
# def lottery ():
#     tickets = [1,2,3,4,5,6]
#     win = random.choice(tickets)
#     print(win)
#     return win
#
#
# great = 54 + lottery()
# print(great)

' модуль 2 повышенная сложность'
# for n in range (3, 21):
#     list_ = ''
#     for i in range(1, n):
#         for j in range(i+1, n):
#             if n % (i + j) == 0:
#                 list_ += (f'{i}{j}') #list_.append(int(''.join(map(str, (sorted([i, j]))))))
#         if i >= (n // 2):
#             break
#
#
#     print()
#     print(list_)

list_0 = [7, 3, 3, 5, 8]
list_ = ''
for i in range(len(list_0)):

    #print(list_0[i])
    print()
    for j in range(len(list_0)):
        #print(list_0[j])
        #if n % (i + j) == 0:
        list_ += (f'{list_0[i]}+{list_0[j]} u ')
    # if i >= (n // 2):
    #     break

print('Пароль: ', list_)

# list_ = ''
# if n % 2 == 0:
#     for i in range(1, n // 2):
#         for j in range(1, n):
#             if n % (i + j) == 0 and i != j:
#                 list_ += (f'{i} + {j} ') #list_.append(int(''.join(map(str, (sorted([i, j]))))))
#
# else:
#     for i in range(1, n // 2 + 1):
#         for j in range(1, n):
#             if n % (i + j) == 0 and i != j:
#                 list_ += (f'{i} + {j} ')
#
# print(list_)




# set_ = sorted({i for i in list_})
#
#
# print(set_)


# list_ = []
# for i in range(1, n ):
#     for j in range(1, 20):
#         if n % (i + j) == 0 and i != j:
#             list_.append(sorted(list({i, j})))
#
# print(*list_)



# set_sort = set()
# for i in list_:
#     print(str(sorted(list(i))))
#     set_sort.add(int(''.join(map(str, (sorted(list(i))))))) #str(sorted(list(i))))
#
# print(set_sort)


# set = set()
# set.add({2, 3})