from tinycadlib import releative
from math import degrees
from time import time
a1 = 60

a2 = 40
a3 = 60
a4 = 50


if __name__=='__main__':
    t0 = time()
    l = [f"{t}\t{degrees(releative(t,a1,a2,a3,a4))%360}" for t in range(0, 360)]
    print("\n".join(l))
    print(time()-t0)
