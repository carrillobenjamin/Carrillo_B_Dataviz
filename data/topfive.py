import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Canada', 'USA', 'Russia', 'Germany', 'Norway')
y_pos = np.arange(len(objects))
performance = [605, 652, 761, 619, 457]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Total Medals')
plt.title('Top 5 Winning Countires')

plt.show()