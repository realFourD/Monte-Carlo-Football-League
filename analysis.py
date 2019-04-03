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
output_sorted = np.memmap("output_S_{}.npy".format(k),
                          dtype='int', mode='r', shape=(k, 20, 6))


# average of teams
table = np.average(output, axis=0)
# display average of teams
fig1, ax1 = plt.subplots(4, 5, sharey='row')
fig1.subplots_adjust(hspace=0.4)
for y in range(0, 4):
    for x in range(0, 5):
        team = x+y*5
        axe = ax1[y, x]
        
        axe.set_xlim([0, 120])
        axe.set_ylim([0, 0.09])
        axe.set_xticks(range(0, 121, 30))
        axe.set_title(str(team_pos[team]), fontsize=8)
        axe.set_xlabel('Points', fontsize=6)
        axe.set_ylabel('Probability', fontsize=6)
        axe.tick_params(axis='both', labelsize=8)
        
        axe.hist(output[:, team, 5], density=True, bins=15)
        axe.axvline(x=table[team, 5], color="r", lw="1")
        axe.axvline(x=np.amin(output[:,team,5]), color="y", lw="1")
        axe.axvline(x=np.amax(output[:,team,5]), color="g", lw="1")


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
        axe.set_ylim([0, 0.25])
        axe.set_xticks(range(0, 121, 30))
        axe.set_title("Pos: {}".format(str(team+1)), fontsize=8)
        axe.set_xlabel('Points', fontsize=6)
        axe.set_ylabel('Probability', fontsize=6)
        axe.tick_params(axis='both', labelsize=8)
        
        axe.hist(output_sorted[:, team, 5], density=True, bins=15)
        axe.axvline(x=table_sort[team, 5], color="r", lw="1")
        axe.axvline(x=np.amin(output_sorted[:,team,5]), color="y", lw="1")
        axe.axvline(x=np.amax(output_sorted[:,team,5]), color="g", lw="1")

fig1.savefig("1.png", bbox_inches='tight', dpi=1000)
fig2.savefig("2.png", bbox_inches='tight', dpi=1000)
plt.show()


