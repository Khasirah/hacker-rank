def timeConversion(stringTime):
    jam = int(stringTime[0:2])
    menit = ""
    detik = ""
    jenisTime = stringTime[8:]

    if len(stringTime[6:8]) == 1:
        detik = f"0{stringTime[6:8]}"
    else:
        detik = stringTime[6:8]

    if len(stringTime[3:5]) == 1:
        menit = f"0{stringTime[3:5]}"
    else:
        menit = stringTime[3:5]

    if jenisTime == "AM" and jam == 12:
        return f"00:{menit}:{detik}"

    if jenisTime == "AM" and jam != 12:
        return f"0{jam}:{menit}:{detik}"

    if jenisTime == "PM" and jam == 12:
        return f"{jam}:{menit}:{detik}"

    if jenisTime == "PM" and jam != 12:
        return f"{12+jam}:{menit}:{detik}"


if __name__ == '__main__':

    stringTime = input()

    print(timeConversion(stringTime))
