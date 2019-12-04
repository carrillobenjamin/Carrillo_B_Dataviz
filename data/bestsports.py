import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('10000m', '1000m', '1500m', '15km', '3000m', '5000m', '500m', 
'5km', '7.5km', 'Aerials','Curling', 'Downhill', 'Four-Man', 'Slalom',
'Ice Dancing', 'Hockey', 'Individual', 'Moguls', 'Pairs', 'Skiing',
'Snowboard', '1.5km', 'Super-G', 'Team', 'Two-Man')
y_pos = np.arange(len(objects))
performance = [1, 11, 9, 2, 34, 29, 9,
1, 1, 4, 50, 5, 8, 6,
6, 323, 18, 8, 14, 6,
5, 1, 2, 24, 10]

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Medal Count')
plt.title('Medals Won From Each Sport For Canada')

plt.show()