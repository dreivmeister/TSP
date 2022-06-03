import numpy as np
import random

class Boid:
    def __init__(self, pos, vel, ind_best) -> None:
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.ind_best = ind_best
        self.ind_best_pos = self.pos

class Swarm:
    def __init__(self, f, num_particle, cog_weight, soc_weight) -> None:
        self.glo_best = None
        self.glo_best_pos = None

        self.cog_weight = cog_weight
        self.soc_weight = soc_weight
        self.r1 = random.uniform(0,1)
        self.r2 = random.uniform(0,1)
        self.inermax = 1.0
        self.inermin = 0.1
        self.iner = self.inermax

        self.num_particle = num_particle
        self.population = []
        self.function = f
        self.init_population()
    
    def init_population(self):
        low,high = 0.0,10.0
        glpos = np.random.uniform(low=low,high=high,size=(2,))
        self.glo_best_pos = glpos
        self.glo_best = self.function(self.glo_best_pos)
        for i in range(self.num_particle):
            pos0 = np.random.uniform(low=low,high=high,size=(2,))

            if self.function(pos0) < self.glo_best:
                self.glo_best = self.function(pos0)
                self.glo_best_pos = pos0

            vel0 = np.random.uniform(-abs(high-low),abs(high-low),size=(2,))
            self.population.append(Boid(pos0,vel0, self.function(pos0)))
    
    def update_velocity(self, curr_vel, ind_best_pos, curr_pos):
        return self.iner*curr_vel + self.cog_weight*self.r1*(ind_best_pos-curr_pos) + self.soc_weight*self.r2*(self.glo_best_pos-curr_pos)
    
    def update_position(self, curr_pos, curr_vel):
        return curr_pos + curr_vel
    
    def update_iner(self, t, T):
        return self.inermax - (self.inermax - self.inermin)*(t/T)
    
    def run_aco(self):
        num_iters = 0
        max_iters = 1000
        while num_iters < max_iters:
            for particle in self.population:
                #calc fitness
                p_fitness = self.function(particle.pos)

                #update ind_best
                if p_fitness < particle.ind_best:
                    particle.ind_best = p_fitness
                    particle.ind_best_pos = particle.pos

                    #update glo_best
                    if particle.ind_best < self.glo_best:
                        self.glo_best = particle.ind_best
                        self.glo_best_pos = particle.pos
            
            #update velocity
            #update location
            for particle in self.population:
                particle.vel = self.update_velocity(particle.vel, particle.ind_best_pos, particle.pos)
                particle.pos = self.update_position(particle.pos, particle.vel)
            self.iner = self.update_iner(num_iters, max_iters)
            num_iters += 1


def function(x,y):
    return x**2 + y**2

# S = Swarm(function, 100, 2.0, 2.0)
# S.run_aco()
# print(S.glo_best, S.glo_best_pos)


#https://stackoverflow.com/questions/51765184/how-to-3d-plot-function-of-2-variables-in-python
#https://moonbooks.org/Articles/How-to-evaluate-and-plot-a-2D-function-in-python-/


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot(function, mode='3D'):

    b = np.arange(-10, 10, 0.2)
    d = np.arange(-10, 10, 0.2)
    B, D = np.meshgrid(b, d)
    nu = function(B,D)
    x = np.random.uniform(low=-10,high=10,size=(5,))
    y = np.random.uniform(low=-10,high=10,size=(5,))

    if mode == '3D':
        fig = plt.figure()
        ax = Axes3D(fig)
        ax.plot_surface(B, D, nu)
        ax.scatter(x, y, function(x,y)+3, c='red')
    elif mode == '2D':
        plt.contourf(B, D, nu)
        plt.colorbar()
        plt.scatter(x,y, c='red')

    
    plt.xlabel('b')
    plt.ylabel('d')
    plt.show()


plot(function, '3D')
