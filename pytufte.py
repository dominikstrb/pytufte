import matplotlib.pyplot as plt

plt.style.use("tufte.mplstyle")

GOLDEN_RATIO = 1.61803
DEFAULT_FIGSIZE = 4.7747

def get_figsize(width=1/2, ratio=GOLDEN_RATIO, base_figsize=DEFAULT_FIGSIZE):
    """ Get the figure size for a Latex document in inches
    Args:
        width (float): width in terms of textwidth in a Latex doc that the figure should occupy
        base_figsize (float): width of the page
        ratio (float): height = width / ratio
    Returns:
        (width, height) tuple of floats
    """
    return base_figsize * width, base_figsize * width / ratio

if __name__ == "__main__":
    import numpy as np

    x = np.linspace(0, 2 * np.pi)
    y = np.sin(x)

    plt.plot(x, y, label="sin")
    plt.legend()
    plt.show()
