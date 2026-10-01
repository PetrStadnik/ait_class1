import matplotlib.pyplot as plt
import numpy as np

def znamenko(x):
    return np.sign(np.cos(x)-x)

if __name__ == "__main__":


    x = np.linspace(-1, 4, 110)
    #print(x)

    a = 0
    b = 1
    size = 1
    while size >= 0.01:
        plt.plot(x, np.cos(x)-x, "-")
        plt.plot(x, x*0, "-")
        #plt.plot([2], "o")
        plt.grid(True)
        plt.axvspan(a,b, color="red", alpha=0.2)
        plt.show()

        c = (b-a)/2 + a
        if znamenko(c) == znamenko(a):
            a=c
        else:
            b=c
        size = (b-a)/2



    plt.plot(x, np.cos(x)-x, "-")
    plt.plot(x, 0*x+0, "-")
    plt.grid(True)
    plt.show()

    plt.plot(x, x, "-")
    plt.plot(x, 0*x -1, "-")
    plt.show()

    """
    3x - 2 = 5x
    
   3x - 2 - 5x = 0
    """

    reseni = np.roots([-2,-2])
    print(reseni)

