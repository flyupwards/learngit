import time
import random

start=time.time()
sorted([random.random() for i in range(2000000)])
end=time.time()
print(str(end-start))
