# Dictionaries

monthAbbrs = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

appointmentBook = {
    "09/17/2020": {
        "docA": [(2100, 2200), (1000, 1130), (900, 954)],
        "docB": [(900, 930), (1500, 1600), (1800, 1900)],
    },
    "09/18/2020": {
        "docA": [(2100, 2200), (1000, 1130), (900, 954)],
        "docB": [(900, 930), (1500, 1600), (1800, 1900)],
    }
}

monthNums = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

print(monthAbbrs["Nov"])
print(monthAbbrs.get("Aug"))
print(monthAbbrs.get("Luv", "Not a valid key"))
print(monthNums[12])
print(monthNums.get(69, "N/A"))