from random import randint

points = 40
stats_list = ["strenght","agility","stamina","percepcion","inteligence","charizma","luck"]
stats = {
"strenght":0,
"agility":0,
"stamina":0,
"percepcion":0,
"inteligence":0,
"charizma":0,
"luck":0}
for i in range(points):
    while True:
        stat_index = randint(0,6) # choose index stat
        stat_to_raise = stats_list[stat_index]
        if stats[stat_to_raise]<10:
            stats[stat_to_raise]+=1
            break
    
        

print(stats)