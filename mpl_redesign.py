import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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
perc['dollars'] = (perc['dollars']/perc['dollars'].sum())*100
perc['remainder'] = 100 - perc['dollars']
perc_y = [row[0] for row in perc.values]
perc_width = [row[1] for row in perc.values]
perc_remainder = [row[2] for row in perc.values]


# --------
# Plotting
# --------


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle("Tier One Organization Budget Breakdown", size=16)

# Plot raw numbers
rect1 = ax1.barh(raw_y, raw_width, color="#2b8cbe")
ax1.xaxis.grid(color="#d9d9d9")
ax1.set_title("Raw Numbers")
ax1.set_xlim(0, 165000)
ax1.set_ylim(-0.6, 19.6)
ax1.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax1.xaxis.set_major_locator(ticker.MultipleLocator(50000))
ax1.xaxis.set_major_formatter(ticker.StrMethodFormatter('${x:,g}'))
ax1.tick_params(axis='both', labelsize=8)
ax1.set_xlabel("Funding (in dollars)", size=10)
ax1.set_ylabel("Organization", size=10)

# Plot percentages
rect2 = ax2.barh(perc_y, perc_width, color="#7ecd92")
ax2.xaxis.grid(color="#d9d9d9")
ax2.set_title("Percent of Whole Budget")
ax2.barh(perc_y, perc_remainder, left=perc_width, color="#bae4bc")
ax2.set_xlim(0, 100)
ax2.set_ylim(-0.6, 19.6)
ax2.xaxis.set_minor_locator(ticker.AutoMinorLocator())
ax2.xaxis.set_major_formatter(ticker.PercentFormatter())
ax2.tick_params(axis='both', labelsize=8)
ax2.set_xlabel("Percentage of Whole Tier One Budget", size=10)


# -----------
# Data Labels
# -----------


def autolabel(rects, ax, str_format):
    (x_left, x_right) = ax.get_xlim()
    x_lim = x_right - x_left

    for rect in rects:
        rect_width = rect.get_width()

        if (rect_width / x_lim) > 0.95:
            label_position = rect_width - (x_lim * 0.14)
        else:
            label_position = rect_width + (x_lim * 0.01)

        ax.text(label_position, rect.get_y() + rect.get_height()/2.,
                str_format.format(rect_width), ha='left', va='center', fontsize=8)


autolabel(rect1, ax1, '${:,.0f}')
autolabel(rect2, ax2, '{:.1f}%')


#rcParams['ytick.labelsize'] = 4
fig.tight_layout()
fig.subplots_adjust(top=0.88)
plt.show()
