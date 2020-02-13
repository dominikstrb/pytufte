import matplotlib as mpl

mpl.rcParams["axes.spines.top"] = False
mpl.rcParams["axes.spines.right"] = False
mpl.rcParams["legend.frameon"] = False

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    x = np.linspace(0, 2 * np.pi)
    y = np.sin(x)

    plt.plot(x, y, label="sin")
    plt.legend()
    plt.show()
