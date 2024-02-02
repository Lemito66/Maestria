n_simulations= 10
population_sim=[]
for n in range(n_simulations):
    n_times=1000
    population_count=[population_init]
    population= population_init
    for t in range(n_times-1):
        if limit_min < population < limit_max:
            birth= 1 if np.random.rand() <= b_rate * population else 0
            death= 1 if np.random.rand() <= d_rate * population else 0
            population = population + birth - death
        else:
            population = population
        population_count.append(population)
        
    population_sim.append(population_count)