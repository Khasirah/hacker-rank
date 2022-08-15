def dayOfProgrammer(year):
    isLeap = False

    if year <= 1917 and (year % 4 == 0):
        isLeap = True

    if year > 1918:
        if year % 400 == 0:
            isLeap = True
        elif year % 100 == 0:
            isLeap = False
        elif year % 4 == 0:
            isLeap = True
        else:
            isLeap = False
    
    if year == 1918:
        return f"26.09.{year}"
    
    if isLeap:
        return f"12.09.{year}"

    if not isLeap:
        return f"13.09.{year}"

if __name__ == "__main__":
    year = int(input().strip())
    result = dayOfProgrammer(year)
    print(result)
