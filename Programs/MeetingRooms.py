# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] find the minimum number of conference rooms required.
# Example Input: [[1,10],[3,4],[2,6],[4,5]]
# Output: 3

def mySolution(meetings):
    times = []
    for meeting in meetings:
        times.append((meeting[0], True))
        times.append((meeting[1], False))

    times.sort()
    currentRooms, maxRooms = 0, 0
    for time in times:
        if time[1] is True:
            currentRooms += 1
            if currentRooms > maxRooms:
                maxRooms = currentRooms
        elif time[1] is False:
            currentRooms -= 1

    return maxRooms


def optimal(meetings):
    schedule = {}
    for i in range(24):
        schedule[i] = 0

    maxRooms = 0
    for meeting in meetings:
        for i in range(meeting[0], meeting[1]):
            schedule[i] += 1
            if schedule[i] > maxRooms:
                maxRooms = schedule[i]

    return maxRooms

cases = [
    ([[1,10],[3,4],[2,6],[4,5]], 3),
    ([[1,10]], 1),
]

def test(cases):
    for case in cases:
        if mySolution(case[0]) != case[1]:
            print("TEST FAILED")

test(cases)