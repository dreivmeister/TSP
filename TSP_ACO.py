import numpy as np
#https://en.wikipedia.org/wiki/Particle_swarm_optimization
class Boid:
    def __init__(self, pos, vel) -> None:
        #initialize Boid with position, velocity vector and individual best pos (min value of function)
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.ind_best = self.pos

class Swarm:
    def __init__(self, f, num_particle, max_iters, low, high, cog_weight, soc_weight, iner) -> None:
        self.glo_best = np.random.uniform(high=high, size=(2,))
        print(self.glo_best)
        self.cog_weight = cog_weight
        self.soc_weight = soc_weight
        self.iner = iner
        self.num_particle = num_particle
        self.max_iters = max_iters
        self.low = low
        self.high = high
        self.population = []
        self.function = f

        self.init_population()

    def init_population(self):
        for i in range(self.num_particle):
            pos0 = np.random.uniform(low=self.low,high=self.high, size=(2,))
            # print(pos0)
            # print(self.glo_best)
            if self.function(pos0) < self.function(self.glo_best):
                self.glo_best = pos0

            vel0 = np.random.uniform(-abs(self.high-self.low),abs(self.high-self.low), size=(2,))
            self.population.append((Boid(pos0,vel0)))

    def calc_pos(self, ind):
        # print(self.population[ind].pos)
        # print(self.population[ind].vel)
        self.population[ind].pos += self.population[ind].vel

    def calc_vel(self, ind, rp, rg):
        return self.iner*self.population[ind].vel+self.cog_weight*rp*(self.population[ind].ind_best-self.population[ind].pos)+self.soc_weight*rg*(self.glo_best-self.population[ind].pos)

    def run_aco(self):
        num_iters = 0
        dim = len(self.population[0].pos)
        while num_iters<self.max_iters:
            for i in range(len(self.population)):
                for j in range(dim):
                    rp, rg = np.random.uniform(), np.random.uniform()
                    self.population[i].vel = self.calc_vel(i, rp, rg)
                    #print(self.population[i].vel)
                    self.calc_pos(i)
                    if self.function(self.population[i].pos) < self.function(self.population[i].ind_best):
                        self.population[i].ind_best = self.population[i].pos
                        if self.function(self.population[i].ind_best) < self.function(self.glo_best):
                            self.glo_best = self.population[i].ind_best

            num_iters+=1


def func(inp):
    x1 = inp[0]
    x2 = inp[1]
    return -np.cos(x2)+np.cos(x2)*np.exp(-(x1-np.pi)**2-(x2-np.pi)**2)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot(function, mode='3D', range=[-20,20]):

    b = np.arange(range[0], range[1], 0.2)
    d = np.arange(range[0], range[1], 0.2)
    B, D = np.meshgrid(b, d)
    nu = function([B,D])

    # x = np.random.uniform(low=-10,high=10,size=(5,))
    # y = np.random.uniform(low=-10,high=10,size=(5,))

    if mode == '3D':
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot_surface(B, D, nu)
        #ax.scatter(x, y, function(x,y)+3, c='red')
    elif mode == '2D':
        plt.contourf(B, D, nu)
        plt.colorbar()
        #plt.scatter(x,y, c='red')


    plt.xlabel('b')
    plt.ylabel('d')
    plt.show()



#s = Swarm(func, num_particle=1000, max_iters=1000, low=0, high=10, cog_weight=2, soc_weight=1.5, iner=0.4)
#s.run_aco()
# print(s.glo_best)
# print(function(s.glo_best))



plot(func)
