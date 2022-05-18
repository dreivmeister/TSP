import numpy as np

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
    
    def run_aco(self):
        num_iters = 0
        dim = 2
        while num_iters<1000:
            for i in range(len(self.population)):
                for j in range(dim):
                    rp, rg = np.random.uniform(), np.random.uniform()
                    self.population[i].vel = calc_vel(rp, rg)
                    #usw https://en.wikipedia.org/wiki/Particle_swarm_optimization



