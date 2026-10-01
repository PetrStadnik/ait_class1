import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

def vizualize(a, b, c, alfa):
    A = [0,0]
    B = [c,0]
    C = [np.cos(np.radians(alfa))*b, np.sin(np.radians(alfa))*b]
    p = Polygon([A, B, C], facecolor="orange", edgecolor="purple")
    fig, ax = plt.subplots()

    ax.add_patch(p)
    plt.show()

def sss(a,b,c):
    print("Počítám SSS")
    alfa = np.degrees(np.arccos((b**2 + c**2 - a**2)/(2*b*c)))
    beta = np.degrees(np.arccos((a**2 + c**2 - b**2)/(2*a*c)))
    gama = 180 - alfa - beta
    return alfa, beta, gama

if __name__ == "__main__":
    a, b, c = None, None, None
    alfa, beta, gama = None, None, None

    a = int(input("a: "))
    b = int(input("b: "))
    c = int(input("c: "))
    alfa = int(input("alfa: "))
    beta = int(input("beta: "))
    gama = int(input("gama: "))

    strany = np.array([a,b,c])
    uhly = np.array([alfa,beta,gama])

    print(np.where(strany == 0)[0].shape[0])

    if np.where(strany == 0)[0].shape[0] == 3:
        print("neplatny vstup")
        exit(1)
    if np.where(strany == 0)[0].shape[0] == 2 and np.where(uhly == 0)[0].shape[0] > 1:
        print("neplatny vstup")
        exit(1)
    if np.where(strany == 0)[0].shape[0] == 1 and np.where(uhly == 0)[0].shape[0] > 2:
        print("neplatny vstup")
        exit(1)

    if np.where(strany != 0)[0].shape[0] == 3:
        alfa, beta, gama = sss(a,b,c)

    vizualize(a,b,c, alfa)
    print(a,b,c, alfa, beta, gama)
