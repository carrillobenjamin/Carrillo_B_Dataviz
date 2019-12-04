import matplotlib.pyplot as plt

amount = [306, 198, 101]
medals = ['gold', 'silver', 'bronze']
colors = ['gold', 'silver', 'peru']

plt.pie(amount, labels=medals, colors=colors, startangle=90, autopct='%.1f%%')
plt.title("Canada's Medal Collection", pad=20)

plt.show()