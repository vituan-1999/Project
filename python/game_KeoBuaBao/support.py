def message(Computer, User):
    print("\tBạn chọn: " + User)
    print("\tMáy chọn: " + Computer)


def calculate(Computer, User):
    tie = "Chúng ta hòa rồi :)"
    win = "Bạn thắng rồi! Chúc mừng nha :)"
    lose = "Bạn thua rồi! he he ^^"
    if User == Computer:
        return tie
    elif User == "Kéo":
        if Computer == "Búa":
            return lose
        elif Computer == "Bao":
            return win
    elif User == "Bao":
        if Computer == "Kéo":
            return lose
        elif Computer == "Búa":
            return win
    elif User == "Búa":
        if Computer == "Bao":
            return lose
        elif Computer == "Kéo":
            return win
