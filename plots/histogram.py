import matplotlib.pyplot as plt

freq = {
    "traffic light": 2.69e+04,
    "traffic sign": 3.49e+04,
    "car": 1.03e+05,
    "person": 1.33e+04,
    "bus": 1.6e+03,
    "truck": 4.24e+03,
    "rider": 649,
    "bike": 1.01e+03,
    "motor": 452,
    "train": 15
}

vs = freq.values()
s = sum(vs)

plt.xticks(rotation='vertical')
plt.ylabel("Frequencies of targets")
for i, v in enumerate(vs):
    plt.text(i, v + 1600, str(int(v)), ha='center')
plt.ticklabel_format(style='sci', axis='y', scilimits=(4,4))
plt.bar(freq.keys(), vs)
plt.tight_layout()
# plt.show()
plt.savefig("plots/frequencies.jpg")
