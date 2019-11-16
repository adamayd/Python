# __eq__ : Equal
# __ne__ : Not Equal
# __lt__ : Less Than
# __gt__ : Greater Than
# __le__ : Less Than or Equal
# __ge__ : Greater Than or Equal
# __add__ : Addition
# __sub__ : Subtraction
# __mul__ : Multiplication
# __div__ : Division
# __mod__ : Modulus

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return "{}:{:02d}:{:02d}".format(self.hour, self.minute, self.second)

    def __add__(self, other_time):
        new_time = Time()

        # Add the seconds and correct if > 60
        if (self.second + other_time.second) >= 60:
            self.minute += 1
            new_time.second = (self.second + other_time.second) - 60
        else:
            new_time.second = self.second + other_time.second

        # Add the minutes and correct if > 60
        if (self.minute + other_time.minute) >= 60:
            self.hour += 1
            new_time.minute = (self.minute + other_time.minute) - 60
        else:
            new_time.mintue = self.minute + other_time.minute

        # Add the hours and correct if > 24
        if (self.hour + other_time.hour) >= 24:
            new_time.hour = self.hour + other_time.hour - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time

    def __sub__(self, other_time):
        new_time = Time()

        # Subtract the seconds and correct if < 0
        if (self.second - other_time.second) < 0:
            self.minute -= 1
            new_time.second = (self.second - other_time.second) + 60
        else:
            new_time.second = self.second - other_time.second

        # Subtract the minutes and correct if < 0
        if (self.minute - other_time.minute) < 0:
            self.hour -= 1
            new_time.minute = (self.minute - other_time.minute) + 60
        else:
            new_time.minute = self.minute - other_time.minute

        # Subtract the hours and correct if < 0
        if (self.hour - other_time.hour) < 0:
            new_time.hour = 0
            new_time.minute = 0
            new_time.second = 0
            print("You cannot have negative time. ")
        else:
            new_time.hour = self.hour - other_time.hour

        return new_time

    def __mul__(self, multNum):
        new_time = Time()
        addMinute = 0
        addHour = 0

        if (self.second * multNum) >= 60:
            addMinute = (self.second * multNum // 60)
            new_time.second = ((self.second * multNum) % 60)
        else:
            new_time.second = self.second * multNum

        if (self.minute * multNum) >= 60:
            addHour = (self.second * multNum // 60)
            new_time.minute = (((self.minute * multNum) + addMinute) % 60)
        else:
            new_time.minute = self.minute * multNum + addMinute

        new_time.hour = self.hour * multNum + addHour

        return new_time

    def __truediv__(self, divNum):
        new_time = Time()

        if (self.second // divNum) == 0 and \
                        (self.minute // divNum) == 0 and \
                        (self.hour // divNum) == 0:
            new_time.second = 0
            new_time.minute = 0
            new_time.hour = 0
            print("Divided too small")
        else:
            new_time.second = self.second // divNum
            new_time.minute = self.minute // divNum
            new_time.hour = self.hour // divNum

        return new_time


def main():
    time1 = Time(1, 20, 31)

    # print(time1)

    time2 = Time(24, 41, 30)

    time3 = Time(12, 32, 23)

    print("Time 1 = ", time1)
    print("Time 2 = ", time2)
    print("Time 3 = ", time3)

    print("Time 1 + Time 2 = ", time1 + time2)

    # print("19 divided by 4 = ", 19/4)

    # print("19 floored by 4 = ", 19//4)

    print("Time 3 * 7 =", time3 * 7)

    print("Time2 - Time3 = ", time2 - time3)

    print("Time3 - Time2 = ", time3 - time2)

    print("Time2 / 4 = ", time2 / 4)


main()
