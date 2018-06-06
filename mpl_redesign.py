import matplotlib.pyplot as plt
import pandas


# ----
# Data
# ----


df = pandas.read_csv("data.csv")

# Raw Plot
raw = df
raw = raw.sort_values('dollars', ascending=False)
raw_y = [row[0] for row in raw.values]
raw_width = [row[1] for row in raw.values]

# Percentage Plot
perc = df
perc = perc.sort_values('dollars', ascending=False)
perc['dollars'] = perc['dollars']/perc['dollars'].sum()
perc['remainder'] = 1 - perc['dollars']
perc_y = [row[0] for row in perc.values]
perc_width = [row[1] for row in perc.values]
perc_remainder = [row[2] for row in perc.values]


# --------
# Plotting
# --------


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle("Tier One Organization Budget Breakdown", size=16)

# Plot raw numbers
rect1 = ax1.barh(raw_y, raw_width)
ax1.set_title("Raw Numbers")
ax1.set_xlim(0, 165000)
ax1.set_ylim(-0.6, 19.6)
# TODO axis labels

#Plot percentages
rect2 = ax2.barh(perc_y, perc_width)
ax2.set_title("% of Whole Budget")
ax2.barh(perc_y, perc_remainder, left=perc_width)
ax2.set_xlim(0, 1)
ax2.set_ylim(-0.6, 19.6)
# TODO axis labels

# -----------
# Data Labels
# -----------


def autolabel(rects, ax):
    (x_bottom, x_top) = ax.get_xlim()
    x_height = x_top - x_bottom

    for rect in rects:
        print(rect.get_width())
        width = rect.get_width()

        p_width = (width / x_height)

        if p_width > 0.95:
            print("greater")
            label_position = width - (x_height * 0.17)
            # TODO change color to white
        else:
            label_position = width + (x_height * 0.01)

        ax.text(label_position, rect.get_y() + rect.get_height()/2.,
                '$%.f' % width,
                ha='left', va='center')


autolabel(rect1, ax1)
autolabel(rect2, ax2)  # TODO make it plot percentage instead of $

fig.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()
