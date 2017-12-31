'''
Multiply elements in p by pHit if the corresponding 
element in world equals Z. Renormalize the distribution
so the sum of the elements equals 1.
'''

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss)) # multiply by pHit if hit true, else multiply by pMiss
    sumQ = sum(q)
    for i in range(len(q)):
        q[i] /= sumQ
    return q
print sense(p,Z)