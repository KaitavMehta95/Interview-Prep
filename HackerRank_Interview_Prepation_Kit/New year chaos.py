# Complete the minimumBribes function below.
def minimumBribes(q):
    bribed = 0
    chaotic = False
    for i in range(len(q)-1,-1,-1):
        if(q[i] != i+1):
            #bribed
            if (q[i-1] == i+1):
                q[i-1],q[i] = q[i],q[i-1]
                bribed +=1
                
            elif(q[i-2] == i+1):
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = i+1
                bribed +=2
            else:
                print('Too chaotic')
                chaotic = True
                break
    if(chaotic == False):
        print(bribed)