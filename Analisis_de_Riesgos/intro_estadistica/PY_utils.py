import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def plot_multiple_hist(dataframe, var_list, n_rows, n_cols, fig_size=(9, 10), discrete=False, stat='probability'):
  fig, ax = plt.subplots(n_rows, n_cols, figsize=fig_size)
  ax = np.ravel(ax)
  for i in range(len(var_list)):
    sns.histplot(x=dataframe[var_list[i]], discrete=discrete, stat=stat, ax=ax[i])
    if discrete:
      ax[i].set_xticks(dataframe[var_list[i]].unique())
    ax[i].set_title(var_list[i])
    ax[i].grid()
  ax = np.reshape(ax, (n_rows, n_cols))
  fig.subplots_adjust(hspace=0.6)
  plt.grid(None)
  plt.show()