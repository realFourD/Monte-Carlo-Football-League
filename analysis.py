import numpy as np
import sys
import matplotlib.pyplot as plt
from StrengthCalc import pos, team_pos


# get interations from cmd
if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
    k = int(sys.argv[1])
else:
    k = 1
print(k)
# setup output matrix
output = np.memmap("output_{}.npy".format(k),
                   dtype='int', mode='r', shape=(k, 20, 6))
'''# order table via points
# set matrix of ordered table
output_sorted = np.memmap("output_S_{}.npy".format(k),
                          dtype='int', mode='w+', shape=(k, 20, 6))
# order each table via points
for j in range(k):
    ordering = output[j, :, 5].argsort()
    ordering = np.flip(ordering, axis=0)
    output_sorted[j, :, :] = output[j, ordering, :]

    if j % 500 == 0:
            print("Completed:",j)

# flush and reopen as read only
del output_sorted'''

# table for positions
output_sorted = np.memmap("output_S_{}.npy".format(k),
                          dtype='int', mode='r', shape=(k, 20, 6))

# average of teams
table = np.average(output, axis=0)
# average of positions
table_sort = np.average(output_sorted, axis=0)

'''
# display average of teams
fig1, ax1 = plt.subplots(4, 5, sharey='row')
fig1.subplots_adjust(hspace=0.4)
for y in range(0, 4):
    for x in range(0, 5):
        team = x+y*5
        axe = ax1[y, x]

        axe.set_xlim([0, 120])
        # axe.set_ylim([0, 0.09])
        axe.set_xticks(range(0, 121, 30))
        axe.set_title(str(team_pos[team]), fontsize=8)
        axe.set_xlabel('Points', fontsize=6)
        axe.set_ylabel('Probability', fontsize=6)
        axe.tick_params(axis='both', labelsize=8)

        axe.hist(output[:, team, 5], density=True, bins=25)
        axe.axvline(x=table[team, 5], color="r", lw="1")
        axe.axvline(x=np.amin(output[:, team, 5]), color="y", lw="1")
        axe.axvline(x=np.amax(output[:, team, 5]), color="g", lw="1")
fig1.savefig("1.png", bbox_inches='tight', dpi=1000)
'''
'''
# average of positions
table_sort = np.average(output_sorted, axis=0)
# display average of positions
fig2, ax2 = plt.subplots(4, 5, sharey='row')
fig2.subplots_adjust(hspace=0.4)
for y in range(0, 4):
    for x in range(0, 5):
        team = x+y*5
        axe = ax2[y, x]

        axe.set_xlim([0, 120])
        # axe.set_ylim([0, 0.25])
        axe.set_xticks(range(0, 121, 30))
        axe.set_title("Pos: {}".format(str(team+1)), fontsize=8)
        axe.set_xlabel('Points', fontsize=6)
        axe.set_ylabel('Probability', fontsize=6)
        axe.tick_params(axis='both', labelsize=8)

        axe.hist(output_sorted[:, team, 5], density=True, bins=20)
        axe.axvline(x=table_sort[team, 5], color="r", lw="1")
        axe.axvline(x=np.amin(output_sorted[:, team, 5]), color="y", lw="1")
        axe.axvline(x=np.amax(output_sorted[:, team, 5]), color="g", lw="1")
fig2.savefig("2.png", bbox_inches='tight', dpi=1000)
'''
'''
fig1, ax1 = plt.subplots(1, 2, sharex=True)
team = 20 - 1
minx = 0
maxx = 50
# cum pos [team]


def setup_axe(axe, xmin, xmax, ymin, ymax, step):
    axe.set_xlim([xmin, xmax])
    axe.set_ylim([ymin, ymax])
    axe.set_xticks(range(xmin, xmax+1, 5))
    axe.set_yticks(
        list(map(lambda x: x/100, range(ymin*100, int(ymax*100+1), step))))
    axe.tick_params(axis='both', labelsize=8)
    axe.set_xlabel('Points', fontsize=10)
    axe.set_xlabel('Points', fontsize=10)
    axe.set_ylabel('Probability', fontsize=10)


axe = ax1[0]
setup_axe(axe, minx, maxx, 0, 1, 5)

axe.set_title("Cumulative Distribution of 20th", fontsize=12)
axe.hist(output_sorted[:, team, 5], density=True,
         bins=range(0, 121), cumulative=True)

a = np.percentile(output_sorted[:, team, 5], 50, interpolation='lower')
b = np.percentile(output_sorted[:, team, 5], 75, interpolation='lower')
c = np.percentile(output_sorted[:, team, 5], 95, interpolation='lower')
axe.axvline(a, color="r", lw="1", label="50% = {}".format(a))
axe.axvline(b, color="black", lw="1", label="75% = {}".format(b))
axe.axvline(c, color="purple", lw="1", label="95% = {}".format(c))
axe.legend()


# dist pos [team]
axe = ax1[1]
setup_axe(axe, minx, maxx, 0, 0.2, 1)

axe.set_title("Probability Distribution of 20th", fontsize=12)
axe.hist(output_sorted[:, team, 5], density=True, bins=range(0, 121))

me = table_sort[team, 5]
mi = np.amin(output_sorted[:, team, 5])
ma = np.amax(output_sorted[:, team, 5])
axe.axvline(me, color="r", lw="1", label="mean = {:.2f}".format(me))
axe.axvline(mi, color="y", lw="1", label="min = {}".format(mi))
axe.axvline(ma, color="g", lw="1", label="max = {}".format(ma))
axe.legend()
'''

# table for positions
'''rankings = np.memmap("rankings_{}.npy".format(k),
                     dtype='int', mode='w+', shape=(20, 20))
rankings[:, :] = np.zeros((20, 20), dtype=int)
for j in range(k):
    ordering = output[j, :, 5].argsort()
    ordering = np.flip(ordering, axis=0)
    rankings[ordering, range(20)] += 1
    if j % 10**4 == 0:
        print(j)
del rankings
'''

rankings = np.memmap("rankings_{}.npy".format(k),
                     dtype='int', mode='r', shape=(20, 20))


fig3, ax3 = plt.subplots(1, 1, figsize=(12, 12))
data = []
labs = []
for y in range(20):
    x = rankings[y, 0]
    if x != 0:
        data.append(int(x))
        labs.append(team_pos[y])


order = [0, 3, 1, 5, 2, 4, 6]
colors = ["#ff585c", "#dd0000", "#034694",
          "#ffe500", "#6c8193", "#97c1e7",  "#cccccc"]
data = [data[i] for i in order]
labs = [labs[i] for i in order]

ax3.set_title("Number of 1st place finishes", fontsize=12)
ax3.pie(data, labels=labs, autopct='%1.4f%%', colors=colors,
        explode=(0.2, 0.2, 0.2, 0.2, 0.2, 0, 0.2), labeldistance=0.8)


fig4, ax4 = plt.subplots(1, 1, figsize=(12, 12))
data = []
labs = []
for y in range(20):
    x1 = rankings[y, 17]
    x2 = rankings[y, 18]
    x3 = rankings[y, 19]
    tot = x1+x2+x3
    if tot != 0:
        data.append(int(tot))
        labs.append(team_pos[y])

order = [0, 1, 2, 5, 6, 7, 9, 10, 8, 11, 4, 12, 13, 14, 3, 15]
colors = ["#ff585c", "#ed1c24", "#005daa", "#27409b", "#cccccc",
          "#ccff33", "#99ccff", "#ed1a3b", "#6c8193", "#761ec8",
          "#034694", "#a3a3a3", "#fbee23", "#007020", "#fde6b3", "#7c2c3b"]
data = [data[i] for i in order]
labs = [labs[i] for i in order]

ax4.set_title("Number of times relegated", fontsize=12)
ax4.pie(data, labels=labs,  colors=colors, autopct='%1.4f%%')

'''
fig0, ax0 = plt.subplots(1, 1)
rowlabel = team_pos
collabel = list(map(str, range(1, 21)))
ax0.set_title("Total finishes for each team per position", fontsize=12)
ax0.axis('tight')
ax0.axis('off')
# normal = plt.Normalize(0, np.max(rankings))
# cellColours = plt.cm.plasma(normal(rankings))
table1 = ax0.table(cellText=rankings, colLabels=collabel,
                   rowLabels=rowlabel, loc='center', fontsize=12)
table1.auto_set_font_size(False)
table1.set_fontsize(10)


# table for scores
points = np.zeros((20, 3))
points[:, 2] = table_sort[:, 5]
points[:, 0] = np.min(output_sorted[:, :, 5], axis=0)
points[:, 1] = np.max(output_sorted[:, :, 5], axis=0)
fig5, ax5 = plt.subplots(1, 1)
rowlabel1 = list(map(str, range(1, 21)))
collabel1 = ("Minimum Points", "Maximum Points", "Average")
ax5.set_title("Points per position", fontsize=12)
ax5.axis('tight')
ax5.axis('off')
table2 = ax5.table(cellText=points, colLabels=collabel1,
                   rowLabels=rowlabel1, loc='center')
table2.auto_set_font_size(False)
table2.set_fontsize(10)
'''

plt.show()
