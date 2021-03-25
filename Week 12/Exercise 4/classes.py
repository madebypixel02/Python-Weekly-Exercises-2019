class Time_interval:
    def __init__(self, hour1, minute1, hour2, minute2):
        self.__hour1 = hour1
        self.__minute1 = minute1
        self.__hour2 = hour2
        self.__minute2 = minute2
        self.__morning = list(range(6, 12))
        self.__afternoon = list(range(12, 18))
        self.__evening = [18, 19, 20, 21, 22, 23]
        self.__night = list(range(0, 6))
        self.__times = []
        self.__hourSwap = None
        self.__minuteSwap = None

        if self.__hour1 not in range(0,24) and self.__hour2 not in range(0,24):
            self.__hour1 = 0
            self.__hour2 = 0
        elif self.__hour1 not in range(0,24):
            self.__hour1 = self.__hour2
        elif self.__hour2 not in range(0,24):
            self.__hour2 = self.__hour1
        if self.__minute1 not in range(0,60):
            self.__minute1 = 0
        if self.__minute2 not in range(0,60):
            self.__minute2 = 0
       
        if self.__hour1 > self.__hour2 or (self.__hour1 == self.__hour2 and self.__minute1 > self.__minute2):
            self.swap()
 
        for i in range(self.__hour1, self.__hour2 + 1):
            if i in self.__morning:
                if "morning" not in self.__times:
                    self.__times.append("morning")
            elif i in self.__afternoon:
                if "afternoon" not in self.__times:
                    self.__times.append("afternoon")
            elif i in self.__evening:
                if "evening" not in self.__times:
                    self.__times.append("evening")
            elif i in self.__night:
                if "night" not in self.__times:
                    self.__times.append("night")


    def swap(self):
        self.__hourSwap = self.__hour1
        self.__minuteSwap = self.__minute1
        self.__hour1 = self.__hour2
        self.__minute1 = self.__minute2
        self.__hour2 = self.__hourSwap
        self.__minute2 = self.__minuteSwap

    def printInfo(self):
        if len(str(self.__hour1)) == 1:
            self.__hour1 = "0" + str(self.__hour1)
        if len(str(self.__hour2)) == 1:
            self.__hour2 = "0" + str(self.__hour2)
        if len(str(self.__minute1)) == 1:
            self.__minute1 = "0" + str(self.__minute1)
        if len(str(self.__minute2)) == 1:
            self.__minute2 = "0" + str(self.__minute2)

        print("[" + str(self.__hour1) + ":" + str(self.__minute1) + "-" + str(self.__hour2) + ":" + str(self.__minute2) + "]")
        print("Interval runs through:", end = " ")
        for i in self.__times:
            print(i, end = " ")
