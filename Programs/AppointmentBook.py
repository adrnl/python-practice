# PART 1
# Take in Date, Time, Duration
# return true and make appointment if available
# return false if not available
# Data Structure:
# appointmentBook = {key(date): value([(StartTime, endTime)])}
appointmentBook = {
    "09/17/2020": [(2100, 2200), (1000, 1130), (900, 954)],
    "09/18/2020": [(2100, 2200), (1000, 1130), (900, 954)],
}

def scheduleAppointment(date, startTime, duration):
    endTime = time + duration
    if not appointmentBook.has_key(date):
        appointmentBook[date] = [(startTime, endTime)]
        return True

    for appointment in appointmentBook[date]:
        # startTime within existing appointment
        if appointment[0] < startTime and startTime < appointment[1]:
            return False
        # endTime within existing appointment
        elif appointment[0] < endTime and endTime < appointment[1]:
            return False
        # existing appointmentStart within new appointment
        elif startTime < appointment[0] and appointment[0] < endTime:
            return False
        # existing appointmentEnd within new appointment
        elif startTime < appointment[1] and appointment[1] < endTime:
            return False

    appointmentBook[date].append((startTime, endTime))
    return True

# PART 2
# Take in Date, Time, Duration, DoctorID,
# return true and make appointment if available,
# otherwise check different doctors for availability and schedule with them,
# otherwise return false
# Data Structure:
# appointmentBook = {key(date): {key(id): value(appointments)}}
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

def checkAppointment(appointment, startTime, endTime):
    # startTime within existing appointment
    if appointment[0] < startTime and startTime < appointment[1]:
        return False
    # endTime within existing appointment
    elif appointment[0] < endTime and endTime < appointment[1]:
        return False
    # existing appointmentStart within new appointment
    elif startTime < appointment[0] and appointment[0] < endTime:
        return False
    # existing appointmentEnd within new appointment
    elif startTime < appointment[1] and appointment[1] < endTime:
        return False
    else:
        return True

def scheduleAppointmentAdvanced(date, startTime, duration, doctorID):
    endTime = startTime + duration
    if not appointmentBook.has_key(date):
        appointmentBook[date] = {doctorID: [(startTime, endTime)]}
        return True

    if not appointmentBook[date].has_key(doctorID):
        appointmentBook[date][doctorID] = [(startTime, endTime)]
        return True

    for appointment in appointmentBook[date][doctorID]:
        if checkAppointment(appointment, startTime, endTime):
            appointmentBook[date][doctorID].append((startTime, endTime))
            return True

    for doctor in appointmentBook[date]:
        if doctor != doctorID:
            for appointment in appointmentBook[date][doctor]:
                if checkAppointment(appointment, startTime, endTime):
                    appointmentBook[date][doctor].append((startTime, endTime))
                    return True

    return False
