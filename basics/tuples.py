# Tuples (IMMUTABLE!!!)
# tuplea = (4, 5)
# i, j = tuplea
# tuple_list = [tuplea, (6,9), (4, 20)]
appointmentBook = {
    "09/09/2020": [(800, 900), (900, 1000), (1500, 1600)],
}

print(appointmentBook)
print(appointmentBook["09/09/2020"])

day = appointmentBook["09/09/2020"]
day.append((1100, 1200))
appointmentBook["09/09/2020"].append((1100, 1200))

print(appointmentBook)
print(appointmentBook["09/09/2020"])
# print(tuplea)
# print(tuple_list)
# print(i)
# print(j)
# print(tuple[0])
# print(tuple[1])
# for tuple in tuple_list:
#     print((x,y))