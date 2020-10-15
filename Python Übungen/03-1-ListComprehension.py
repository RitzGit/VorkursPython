# Aufgabe:   Folgende Liste durch list comprehension generieren.
# [
# [0 , 0 , 1 , 0 , 0] ,
# [0 , 0 , 1 , 0 , 0] ,
# [1 , 1 , 1 , 1 , 1] ,
# [0 , 0 , 1 , 0 , 0] ,
# [0 , 0 , 1 , 0 , 0]
# ]

# 1: 1 falls r == 2 ist für die range [0, 1, 2, 3, 4]. Sonst 0. Dies generiert [0, 0, 1, 0, 0]
# 2: 1 für alle Werte von range 5, also [1, 1, 1, 1, 1]
# 3: Füge array1 ein falls n == 2 für die range [0, 1, 2, 3, 4], sonst füge array2 ein.
#                       1                              3                 22
array = [ [1 if r == 2 else 0 for r in range(5)] if n != 2 else [1 for _ in range(5)] for n in range(5)]

for e in array:
    print(e)