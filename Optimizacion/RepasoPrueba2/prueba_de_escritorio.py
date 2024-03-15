number = 0
ep = 1

while (1 + ep) > 1.01:
    ep = ep / 2
    number += 1
    
    print(f'Number: {number} - Ep: {ep} - suma: {1 + ep}')
    
    
