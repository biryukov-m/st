from datetime import datetime

now = datetime.now()

dt = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
print(type(dt))