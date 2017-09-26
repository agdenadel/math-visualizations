from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def model_2d(function, parameters, num_steps, x_initial, y_initial):
    x = [0] * (num_steps + 1) # add one for initial state
    y = [0] * (num_steps + 1) # add one for initial state

    for i in range(num_steps):
        x[i+1], y[i+1] = function(x[i], y[i], parameters)

    return x, y

def henon(x, y, parameters = {'a': 1.4, 'b': 0.3}):
    a = parameters['a']
    b = parameters['b']

    x_next = 1 - a * x **2 + y
    y_next = b * x
    return x_next, y_next

def plot_2d(x, y, plot_name, x_axis_label="X axis", y_axis_label="Y axis"):
    fig = plt.figure()
    axes = fig.gca()

    axes.scatter(x, y, lw=0.5)
    axes.set_xlabel(x_axis_label)
    axes.set_ylabel(y_axis_label)
    axes.set_title(plot_name)
    plt.show()

def main():
    parameters = {
                    'a': 1.4,
                    'b': 0.3
                }
    num_steps = 1000
    x_initial = 0
    y_initial = 0

    x, y = model_2d(henon, parameters, num_steps, x_initial, y_initial)
    plot_2d(x, y, "Henon")

if __name__ == "__main__":
    main()  