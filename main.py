# Q3
def players(dmovies):
    d = {}  # maps players to number of movies they played in
    for movie in dmovies:
        playerslist = dmovies[movie]
        for player in playerslist:
            if player in d:
                d[player] += 1
            else:
                d[player] = 1
    # print(d.items())
    sorted_dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    return sorted_dict


d = {"You have got mail": ["Meg Ryan", "Tom Hanks"],
     "The Post": ["Tom Hanks", "Meryl Streep", "Bob OdenKirk"],
     "Sleepless in Seattle": ["Meg Ryan", "Tom Hanks"]}

print(players(d))

# Q4 a
print([x for x in range(2, 20)
       if all(x % y != 0 for y in range(2, x))])


# def prime_numbers(n):
#     primes = []
#     for x in range(2, n):
#         lst=[]
#         for y in range(2, x):
#             if x % y != 0:
#                 lst.append(True)
#             else:
#                 lst.append(False)
#         if all(lst):
#             primes.append(x)
#     return primes

# print(prime_numbers(20))

# Q4 b
def pref(a_list):
    return [a_list[0:i] for i in range(len(a_list) + 1)]


lst = [1, 2, "hi", "bye"]
print(pref(lst))


# def pref (a_list):
#     return [[ a_list[j] for j in range(0,i)] for i in range(len(a_list) + 1)]
#
# lst=[1, 2, "hi", "bye"]
# print(pref(lst))


# def prefixes(a_list):
#     result = []
#     for i in range(len(a_list) + 1):
#         lst=[]
#         for j in range(0,i):
#             lst.append(a_list[j])
#         result.append(lst)
#     return result
#
# lst=[1, 2, "hi", "bye"]
# print(prefixes(lst))


# Q5
def select(iterable, bitmap):
    it = iter(bitmap)
    for i in iterable:
        b = next(it, 1)
        if b == 1:
            yield i


##(1,0,0,1,1,1)
for x in select(["Yes", "we", "can", "lock", "her", "up"], (1, 0, 0, 1)):
    print(x)
