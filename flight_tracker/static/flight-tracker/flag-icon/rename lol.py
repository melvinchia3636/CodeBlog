import os
[os.rename(i, i.lower()) for i in os.listdir('.')]