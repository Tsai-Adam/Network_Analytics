# import library
from collections import Counter
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# read data
teams = pd.read_csv("/Users/adam/Desktop/Bayes/Class/Network_Analytics/SMM638/MTP/team_employee_affiliations.csv")
teams.head()
teams.tail()

outcome = pd.read_csv("/Users/adam/Desktop/Bayes/Class/Network_Analytics/SMM638/MTP/project_outcomes.csv")
outcome.head()
outcome.tail()
outcome.describe().T

ke = pd.read_csv("/Users/adam/Desktop/Bayes/Class/Network_Analytics/SMM638/MTP/knowledge_exchange_network.csv",
sep=",", header=None, names=["u", "v"])
ke.head(15)
ke.tail()

# plot
## ke
g = nx.from_pandas_edgelist(ke, source="u", target="v")
nx.is_directed(g)
nx.is_weighted(g)
nx.draw_kamada_kawai(g, node_size=10, node_color="lime", alpha=0.5)
plt.show()

## 
g_node_degree = nx.degree(g)
# get average degree
g_k = np.mean([d for n, d in g_node_degree])
g_k

# visualize average degree
fig = plt.figure(figsize=(3, 9))
ax0 = fig.add_subplot(311)
ax1 = fig.add_subplot(312)
# bar chart
ax0.bar(0, g_k, color='lime', width=0.5)
#ax0.bar(1, g1_k, color='magenta', width=.5)
ax0.set_xticks([0, 1])
ax0.set_xticklabels(['Star network', 'Denser network'])
ax0.set_ylabel('Average degree ― $<k>$')
# star network
nx.draw(g, with_labels=True, node_size=500, node_color='lime', ax=ax1)
ax1.text(1.25, -1, 'A', fontdict={'fontsize': 16, 'fontweight': 'bold'})
('A. Star network')
# show plot
plt.show()


