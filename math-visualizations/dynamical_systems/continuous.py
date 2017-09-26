from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D





# Models continuous systems of DE's with Euler's method
def model_3d(function, parameters, x_initial, y_initial, z_initial, num_steps, delta_t):
    x = [0] * (num_steps + 1) # add one for initial value
    y = [0] * (num_steps + 1) # add one for initial value
    z = [0] * (num_steps + 1) # add one for initial value

    x[0] = x_initial
    y[0] = y_initial
    z[0] = z_initial

    for i in range(num_steps):
        x_prime, y_prime, z_prime = function(x[i], y[i], z[i], parameters)
        x[i+1] = x[i] + x_prime * delta_t
        y[i+1] = y[i] + y_prime * delta_t
        z[i+1] = z[i] + z_prime * delta_t

    return x, y, z

# Models continuous systems of DE's with Euler's method
def model_2d(function, parameters, x_initial, y_initial, num_steps, delta_t):
    x, y, z = model_3d(function, parameters, x_initial, y_initial, 0, num_steps,delta_t)
    # throw away z
    return x, y

def plot_3d(x, y, z, plot_name, x_axis_label="X axis", y_axis_label="Y axis", z_axis_label="Z axis"):
    fig = plt.figure()
    axes = fig.gca(projection='3d')

    axes.plot(x, y, z, lw=0.5)
    axes.set_xlabel(x_axis_label)
    axes.set_ylabel(y_axis_label)
    axes.set_zlabel(z_axis_label)
    axes.set_title(plot_name)
    plt.show()

def plot_2d(x, y, plot_name, x_axis_label="X axis", y_axis_label="Y axis"):
    fig = plt.figure()
    axes = fig.gca()

    axes.plot(x, y, z, lw=0.5)
    axes.set_xlabel(x_axis_label)
    axes.set_ylabel(y_axis_label)
    axes.set_title(plot_name)
    plt.show()


def lorenz(x,y,z, parameters = {'sigma': 10, 'rho': 2, 'beta': 8/3}):
    sigma = parameters['sigma']
    rho = parameters['rho']
    beta = parameters['beta']
    x_prime = sigma * (y-x)
    y_prime = x * (rho-z) -y
    z_prime = x*y - beta*z

    return x_prime, y_prime, z_prime



def luChen(x, y, z, parameters = {'a': 40, 'b': 3, 'c': 28}):
    a = parameters['a']
    b = parameters['b']
    c = parameters['c']
    x_prime = a * (y-x)
    y_prime = (c-a) * x - x*z + c*y
    z_prime = x*y - b*z

    return x_prime, y_prime, z_prime


def plot_lorenz(sigma, rho, beta, delta_t, num_steps, x_initial, y_initial, z_initial):
    parameters = {
                    'sigma': sigma,
                    'rho': rho,
                    'beta': beta
                }

    x, y, z = model_3d(lorenz, parameters, x_initial, y_initial, z_initial, num_steps, delta_t)
    plot_3d(x, y, z, "Lorenz Attractor")

def plot_lorenz_2d(sigma, rho, beta, delta_t, num_steps, x_initial, y_initial, z_initial):
    parameters = {
                    'sigma': sigma,
                    'rho': rho,
                    'beta': beta
                }

    x, y, z = model_3d(lorenz, parameters, x_initial, y_initial, z_initial, num_steps, delta_t)
    plot_2d(x, y, "Lorenz Attractor")

def plot_luChen(a, b, c, delta_t, num_steps, x_initial, y_initial, z_initial):
    parameters = {'a': a, 'b': b, 'c': c}
    x, y, z = model_3d(luChen, parameters, x_initial, y_initial, z_initial, num_steps, delta_t)
    plot_3d(x, y, z, "Lu Chen Attractor")

def plot_henon(a, b, num_steps, x_initial, y_initial):
    parameters = {
                    'a': a,
                    'b': b
                }

    x, y = henon(x, y, parameters)

def main():
    # parameters Lorenz used
    sigma = 10
    rho = 28
    beta = 8/3

    delta_t = 0.01
    num_steps = 10000

    x_initial = 1
    y_initial = 1
    z_initial = 14
    a = 40
    b = 3
    c = 28
    plot_luChen(a, b, c, delta_t, num_steps, x_initial, y_initial, z_initial)


if __name__ == "__main__":
    main()