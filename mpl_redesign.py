import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv("data.csv")
raw = df
raw = raw.sort_values('dollars', ascending=False)
y_range = [row[0] for row in raw.values]
print(y_range)
width = [row[1] for row in raw.values]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), tight_layout=True)
rect1 = ax1.barh(y_range, width)
ax1.set_xlim(0, 165000)
ax1.set_ylim(-0.6, 19.6)


def autolabel(rects, ax):
    (x_bottom, x_top) = ax.get_xlim()
    x_height = x_top - x_bottom

    for rect in rects:
        print(rect.get_width())
        width = rect.get_width()

        p_width = (width / x_height)

        if p_width > 0.95:
            print("greater")
            label_position = width - (x_height * 0.15)
        else:
            label_position = width + (x_height * 0.01)

        ax.text(label_position, rect.get_y() + rect.get_height()/2.,
                '$%.f' % width,
                ha='left', va='center')


autolabel(rect1, ax1)

ax2.barh(y_range, width)
ax2.set_xlim(0, 100)
ax2.set_ylim(-0.6, 19.6)

plt.show()
