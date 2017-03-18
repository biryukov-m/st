import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, x):
        super(LoggableList, self).append(x)
        self.log(x)

l = LoggableList()
l.append(112341234)