import numpy as np
#https://en.wikipedia.org/wiki/Particle_swarm_optimization
class Boid:
    def __init__(self, pos, vel) -> None:
        self.pos = np.array(pos)
        self.vel = np.array(vel)
        self.ind_best = self.pos

class Swarm:
    def __init__(self, f, num_particle, cog_weight, soc_weight, iner) -> None:
        self.glo_best = 0
        self.cog_weight = cog_weight
        self.soc_weight = soc_weight
        self.iner = iner
        self.num_particle = num_particle
        self.population = []
        self.function = f
    
    def init_population(self):
        low,high = 0.0,10.0
        for i in range(self.num_particle):
            pos0 = np.random.uniform(low=low,high=high,size=(1,2,1))

            if self.function(pos0) < self.function(self.glo_best):
                self.glo_best = self.function(pos0)

            vel0 = np.random.uniform(-abs(high-low),abs(high-low),size=(1,2,1))
            self.population.append((Boid(pos0,vel0)))
   
    def calc_pos(self, ind):
        self.population[i].pos += self.population[i].vel
            
    def calc_vel(self, ind, rp, rg):
        return self.iner*self.population[i].vel+self.cog_weight*rp*(self.population[i].ind_best-self.population[i].pos)+self.soc_weight*rg*(self.glo_best-self.population[i].pos)
        
    def run_aco(self):
        num_iters = 0
        dim = 2
        while num_iters<1000:
            for i in range(len(self.population)):
                for j in range(dim):
                    rp, rg = np.random.uniform(), np.random.uniform()
                    self.population[i].vel = calc_vel(i, rp, rg)
                    calc_pos(i)
                    if self.function(self.population[i].pos) < self.function(self.population[i].ind_best):
                        self.population[i].ind_best = self.population[i].pos
                        if self.function(self.population[i].ind_best) < self.function(self.glo_best):
                            self.glo_best = self.population[i].ind_best
            num_iters+=1

            
def func(inp):
    return inp[0]**2 + inp[1]**2

s = Swarm(func, 100, 2, 1.5, 0.4)
s.run_aco()
print(s.glo_best)
