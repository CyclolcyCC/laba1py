import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy import fft
from scipy import linalg
import cmocean
import warnings

warnings.filterwarnings('ignore')
# iter = 3 5 10 20
x_0 = 1.35 #27175
x_f = 0.9
step = 0.002

deg = np.pi / 180

def original(arg):
    return arg * np.cos(arg * 4) - 0.5

def derivative(arg):
    return arg * np.cos(arg * 4) - arg * 4 * np.sin(arg * 4)

def double_derivative(arg):
    return -8 * np.sin(4 * arg) - 16 * arg * np.cos(4 * arg)

def standard(x_k_1):
    return x_k_1 - (original(x_k_1)/derivative(x_k_1))

def simplified(x_k_1):
    return x_k_1 - (original(x_k_1)/derivative(x_0))

def draw_func():
    plt.figure(figsize=(15, 5))

    x, of, df, ddf = [], [], [], []

    for i in np.arange(x_f, x_0, step):
        x.append(i)
        of.append(original(i))
        df.append(derivative(i))
        ddf.append(double_derivative(i))

    plt.subplot(1, 1, 1)
    plt.plot(x, of, 'b-', label='original', alpha=0.7)
    plt.plot(x, df, 'g-', label='derivative', alpha=0.7)
    plt.plot(x, ddf, 'r-', label='double derivative', alpha=0.7)

    plt.xlabel('x')
    plt.ylabel('f')
    plt.title('original, derivative and double derivative')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    print('Enter number of iterations:')
    iterations = int(input())

    stand, simple = [x_0], [x_0]
    for i in range(iterations):
        stand.append(standard(stand[i]))
        simple.append(simplified(simple[i]))

    print('Results:\nstandard:')
    print(stand)
    if (np.abs(original(stand[iterations])) <= 1e-12):
        print('Fine')
    else:
        print('Not fine')
    print('simple:')
    print(simple)
    if (np.abs(original(simple[iterations])) <= 1e-12):
        print('Fine')
    else:
        print('Not fine')

    draw_func()