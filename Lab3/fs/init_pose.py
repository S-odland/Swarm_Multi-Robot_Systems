''' Function to initialize agent's poses. 
Input:
    swarmsize --  swarmsize.
    x -- An array to store  agents' x positions, the length of this array is the same as swarmsize
    y -- An array to store agents' y positions, the length of this array is the same as swarmsize
    theta -- An array to store agents' orientations, the length of this is the same as swarmsize

Usage:
    Usr can configure an agent's initial x, y, theta by modifying the value of the corresponding element in array x, y, and theta. 
    For example, initialize agent 0's pose to x = 0, y = 1, theta = 2:
    x[0] = 0
    y[0] = 1
    theta[0] = 2

Constraints to be considered:
    x -- the value should range between -2.5 to 2.5.
    y -- the value should range between -1.5 to 1.5.
    theta -- the value should range between -pi to pi.
    
    The minimal pairwise inter-agent distance should be greater than 0.12

def init(swarmsize, x, y, theta, a_ids):
    import math
    import random
    for i in range(swarmsize):
        x[i] = (i % 16 ) * 0.11-1
        y[i] = (i / 16 ) * 0.11-1
        a_ids[i] = 0
        theta[i] = 0
        if i==0:
            a_ids[i]=1
        elif i==15:
            a_ids[i]=2
    pass
'''
def init(swarmsize, x, y, theta, a_ids):
    import math
    import random
    for i in range(swarmsize):
        y[i] = (i % 10 ) * 0.3-1
        x[i] = (i / 10 ) * 0.3-1
        a_ids[i] = 0
        theta[i] = 0
        j = i % 3
        if j == 0:
            a_ids[i]=0
        elif j == 1:
            a_ids[i]=1
        else:
            a_ids[i] = 2
    pass




# if pos[0] < 0 and pos[1] > 0:
# 	phi_t = -phi_t
# elif pos[0] > 0 and pos[1] < 0:
# 	phi_t = -phi_t + math.pi
# elif pos[0] > 0 and pos[1] > 0:
# 	phi_t = phi_t - math.pi
# elif pos[0] < 0 and pos[1] == 0:
# 	phi_r = 0
# elif pos[0] > 0 and pos[1] == 0:
# 	phi_r = -math.pi
# elif pos[0] == 0 and pos[1] < 0:
# 	phi_r = math.pi/2
# elif pos[0] == 0 and pos[1] > 0:
# 	phi_r = -math.pi/2

##phi_r = math.asin(abs((pos[1]-y)/rAct)) 
# if pos[0] < x and pos[1] == y:
# 	phi_r = math.pi
# elif pos[0] > x and pos[1] == y:
# 	phi_r = 0
# elif pos[0] == x and pos[1] < y:
# 	phi_r = -math.pi/2
# elif pos[0] == x and pos[1] > y:
# 	phi_r = math.pi/2					
# elif pos[0] < x and pos[1] > y:
# 	phi_r = -phi_r + math.pi
# elif pos[0] > x and pos[1] < y:
# 	phi_r = -phi_r
# elif pos[0] < x and pos[1] < y:
# 	phi_r = phi_r - math.pi