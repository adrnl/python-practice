# There are one thousand lockers and one thousand students in a school.
# The principal asks the FIRST student to go to each locker and CLOSES it.
# Then he has the SECOND student go to every SECOND locker and OPENS it.
# The THIRD goes to every third locker and, if it is OPEN, he CLOSES it.
# How many lockers are left OPEN/CLOSED?

def counter(data, object):
    count = 0
    for ele in data:
        if (ele == object):
            count = count + 1
    return count

def studentsAndLockers(num):
    lockers = [1] * num

    for student in range(1, num+1):
        action = student % 2
        for i in range(num):
            if i % student == 0:
                lockers[i] = action

        # print(lockers)
    print('{} lockers are OPEN'.format(counter(lockers, 0)))

print("n = 1")
studentsAndLockers(1)
print("n = 2")
studentsAndLockers(2)
print("n = 3")
studentsAndLockers(3)
print("n = 5")
studentsAndLockers(5)
print("n = 10")
studentsAndLockers(10)
print("n = 25")
studentsAndLockers(25)
print("n = 100")
studentsAndLockers(100)
print("n = 1000")
studentsAndLockers(1000)
