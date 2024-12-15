import matplotlib.pyplot as plt

def plot_data(title,x,y,degree=0):
    plt.title(title)
    plt.xlabel(x)
    plt.ylabel(y)
    plt.xticks(rotation=degree)
    plt.show()