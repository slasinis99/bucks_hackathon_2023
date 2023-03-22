"""
@author: Stephen Lasinis
"""

import csv
from math import sqrt
from random import randint
import numpy as np
from training_data import get_training_data
from network import Network
from fc_layer import FCLayer
from activation_layer import ActivationLayer
from activation_functions import tanh, tanh_prime
from error_functions import mse, mse_prime

def getData():
    file = open("INSERT FILEPATH TO CSV DATA", "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()
    
    #First we need to create our usable list of data
    new_data = []
    for r in range(1,len(data)):
        new_data.append([data[r][2] , data[r][3] , data[r][4] , data[r][5] , data[r][6] , data[r][7] , data[r][8] , data[r][9] , data[r][10] , data[r][11] , data[r][12] , data[r][13] , data[r][14]])
    
    #Convert all the totalTickets, totalAttendance, and revenue to integers
    for r in range(len(new_data)):
        newStr = ""
        for c in new_data[r][10]:
            if c.isdigit(): newStr += c
        new_data[r][10] = int(newStr)
        
        newStr = ""
        for c in new_data[r][11]:
            if c.isdigit(): newStr += c
        new_data[r][11] = int(newStr)
        
        newStr = ""
        for c in new_data[r][12]:
            if c.isdigit(): newStr += c
        new_data[r][12] = int(newStr)
    
    #First sort our new_data by revenue
    sorted_data = []
    while len(new_data) > 0:
        #Find the row with the greatest revenue
        gR = 0
        gI = -1
        for r in range(len(new_data)):
            rev = new_data[r][12]
            if rev > gR:
                gR = rev
                gI = r
        sorted_data.append(new_data[gI])
        new_data.pop(gI)
    return sorted_data

def normalizeData(d):
    #Start with the game time, loop through the list recording the keys with the sums the indexes of occurances and number of occurances
    conversions = []
    gt = {}
    for r in range(len(d)):
        if d[r][0] in gt:
            gt[d[r][0]][0] += r+1
            gt[d[r][0]][1] += 1
        else:
            gt[d[r][0]] = [r+1,1]
    #Get a list of the keys, and convert the dictionary
    l = list(gt.keys())
    for i in range(len(l)):
        gt[l[i]] = (gt[l[i]][0] / gt[l[i]][1]) / 267
    #Loop through all rows and replace game time with dictionary value
    for r in range(len(d)):
        d[r][0] = gt[d[r][0]]
    #Loop through the rows and find the smallest and largest value for normalization
    small = 1
    big = 0
    for r in range(len(d)):
        if d[r][0] < small: small = d[r][0]
        if d[r][0] > big: big = d[r][0]
    for r in range(len(d)):
        d[r][0] = (d[r][0] - small) / (big - small)
    print(gt)
    
    #Create the conversion list for this gt
    conv = []
    k = list(gt.keys())
    for i in range(len(k)):
        conv.append([gt[k[i]],k[i]])
    conversions.append(conv)
    
    #Repeat for month
    gt = {}
    for r in range(len(d)):
        if d[r][1] in gt:
            gt[d[r][1]][0] += r+1
            gt[d[r][1]][1] += 1
        else:
            gt[d[r][1]] = [r+1,1]
    #Get a list of the keys, and convert the dictionary
    l = list(gt.keys())
    for i in range(len(l)):
        gt[l[i]] = (gt[l[i]][0] / gt[l[i]][1]) / 267
    #Loop through all rows and replace game time with dictionary value
    for r in range(len(d)):
        d[r][1] = gt[d[r][1]]
    #Loop through the rows and find the smallest and largest value for normalization
    small = 1
    big = 0
    for r in range(len(d)):
        if d[r][1] < small: small = d[r][0]
        if d[r][1] > big: big = d[r][0]
    for r in range(len(d)):
        d[r][1] = (d[r][1] - small) / (big - small)
    print(gt)
    
    #Create the conversion list for this gt
    conv = []
    k = list(gt.keys())
    for i in range(len(k)):
        conv.append([gt[k[i]],k[i]])
    conversions.append(conv)
    
    #Repeat for Day of Week
    gt = {}
    for r in range(len(d)):
        if d[r][2] in gt:
            gt[d[r][2]][0] += r+1
            gt[d[r][2]][1] += 1
        else:
            gt[d[r][2]] = [r+1,1]
    #Get a list of the keys, and convert the dictionary
    l = list(gt.keys())
    for i in range(len(l)):
        gt[l[i]] = (gt[l[i]][0] / gt[l[i]][1]) / 267
    #Loop through all rows and replace game time with dictionary value
    for r in range(len(d)):
        d[r][2] = gt[d[r][2]]
    #Loop through the rows and find the smallest and largest value for normalization
    small = 1
    big = 0
    for r in range(len(d)):
        if d[r][2] < small: small = d[r][0]
        if d[r][2] > big: big = d[r][0]
    for r in range(len(d)):
        d[r][2] = (d[r][2] - small) / (big - small)
    print(gt)
    
    #Create the conversion list for this gt
    conv = []
    k = list(gt.keys())
    for i in range(len(k)):
        conv.append([gt[k[i]],k[i]])
    conversions.append(conv)
    
    #Repeat for days since last home game
    gt = {}
    for r in range(len(d)):
        if d[r][3] in gt:
            gt[d[r][3]][0] += r+1
            gt[d[r][3]][1] += 1
        else:
            gt[d[r][3]] = [r+1,1]
    #Get a list of the keys, and convert the dictionary
    l = list(gt.keys())
    for i in range(len(l)):
        gt[l[i]] = (gt[l[i]][0] / gt[l[i]][1]) / 267
    #Loop through all rows and replace game time with dictionary value
    for r in range(len(d)):
        d[r][3] = gt[d[r][3]]
    #Loop through the rows and find the smallest and largest value for normalization
    small = 1
    big = 0
    for r in range(len(d)):
        if d[r][3] < small: small = d[r][0]
        if d[r][3] > big: big = d[r][0]
    for r in range(len(d)):
        d[r][3] = (d[r][3] - small) / (big - small)
    print(gt)
    
    #Create the conversion list for this gt
    conv = []
    k = list(gt.keys())
    for i in range(len(k)):
        conv.append([gt[k[i]],k[i]])
    conversions.append(conv)
    
    #Repeat for opponents
    gt = {}
    for r in range(len(d)):
        if d[r][4] in gt:
            gt[d[r][4]][0] += r+1
            gt[d[r][4]][1] += 1
        else:
            gt[d[r][4]] = [r+1,1]
    #Get a list of the keys, and convert the dictionary
    l = list(gt.keys())
    for i in range(len(l)):
        gt[l[i]] = (gt[l[i]][0] / gt[l[i]][1]) / 267
    #Loop through all rows and replace game time with dictionary value
    for r in range(len(d)):
        d[r][4] = gt[d[r][4]]
    #Loop through the rows and find the smallest and largest value for normalization
    small = 1
    big = 0
    for r in range(len(d)):
        if d[r][4] < small: small = d[r][0]
        if d[r][4] > big: big = d[r][0]
    for r in range(len(d)):
        d[r][4] = (d[r][4] - small) / (big - small)
    print(gt)
    
    #Create the conversion list for this gt
    conv = []
    k = list(gt.keys())
    for i in range(len(k)):
        conv.append([gt[k[i]],k[i]])
    conversions.append(conv)
    
    #Repeat for Giveaway
    gt = {}
    for r in range(len(d)):
        if d[r][9] in gt:
            gt[d[r][9]][0] += r+1
            gt[d[r][9]][1] += 1
        else:
            gt[d[r][9]] = [r+1,1]
    #Get a list of the keys, and convert the dictionary
    l = list(gt.keys())
    for i in range(len(l)):
        gt[l[i]] = (gt[l[i]][0] / gt[l[i]][1]) / 267
    #Loop through all rows and replace game time with dictionary value
    for r in range(len(d)):
        d[r][9] = gt[d[r][9]]
    #Loop through the rows and find the smallest and largest value for normalization
    small = 1
    big = 0
    for r in range(len(d)):
        if d[r][9] < small: small = d[r][0]
        if d[r][9] > big: big = d[r][0]
    for r in range(len(d)):
        d[r][9] = (d[r][9] - small) / (big - small)
    
    print(gt)
    
    #Create the conversion list for this gt
    conv = []
    k = list(gt.keys())
    for i in range(len(k)):
        conv.append([gt[k[i]],k[i]])
    conversions.append(conv)
    
    #Normalize Temperature, Total Tickets, Total Attendance, and Total Revenue
    for r in range(len(d)):
        d[r][5] = (int(d[r][5]) - (-2)) / (70 - (-2))
        d[r][6] = int(d[r][6])
        d[r][7] = int(d[r][7])
        d[r][8] = int(d[r][8])
        d[r][10] = (d[r][10] - 11800) / (21400 - 11800)
        d[r][11] = (d[r][11] - 8450) / (19650 - 8450)
        d[r][12] = (d[r][12] - 780000) / (2670000 - 780000)
    return d, conversions

def calculateWeights(d,pct):
    #Loop through the first pct rows and find the biggest value and smallest value for each attribute
    weights = []
    smalls = [1,1,1,1,1,1,1,1,1,1,1,1,1]
    bigs = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for r in range(int(len(d)*pct)):
        #Loop through the columns
        for c in range(len(smalls)):
            if d[r][c] < smalls[c]: smalls[c] = d[r][c]
            if d[r][c] > bigs[c]: bigs[c] = d[r][c]
    for i in range(len(smalls)):
        weights.append(1-(bigs[i] - smalls[i]))
    s = sum(weights)
    for i in range(len(weights)):
        weights[i] = weights[i] / s
    return weights

def dis(w,g1, g2):
    s = 0
    for i in range(len(w)):
        s += w[i] * (g2[i]-g1[i])**2
    return sqrt(s)

def compareClusters(c1,c2):
    #Loop through the key list of c2 and check if the values match in c1 and c2
    equal = True
    l = list(c2.keys())
    for i in range(len(l)):
        if c1[l[i]] != c2[l[i]]: equal = False
    return equal

def cluster(clusters,d,w):
    #Perform the initial clustering
    prevCluster = {}
    for r in range(len(d)):
        #For this row check to make sure it is not one of the cluster medoids
        isMedoid = False
        for g in range(len(clusters)):
            if r == clusters[g][0]: isMedoid = True
        
        #If not medoid, then place in appropriate cluster
        if isMedoid == False:
            cI = -1
            cDis = 1
            for g in range(len(clusters)):
                tDis = dis(w, d[r], d[clusters[g][0]])
                if tDis < cDis: 
                    cDis = tDis
                    cI = g
            prevCluster[str(r)] = cI
            clusters[cI].append(r)
    #Add the current medoids to the prevCluster dictionary
    for g in range(len(clusters)):
        prevCluster[str(clusters[g][0])] = clusters[g][0]
    #print(clusters)
    #Find the new medoid for each cluster
    for c in range(len(clusters)):
        #Loop through the games in this cluster and find the one with the smallest avg distance to all the others
        minI = -1
        minAvg = 1
        for g in range(len(clusters[c])):
            s = 0
            for o in range(len(clusters[c])):
                s += dis(w, d[clusters[c][g]], d[clusters[c][o]])
            s = s / len(clusters[c])
            if s < minAvg:
                minI = g
                minAvg = s
        clusters[c] = [clusters[c][minI]]
    return prevCluster, clusters

def clusterFull(k):
    d, c = normalizeData(getData())
    w = calculateWeights(d, 0.2)
    #Select k rows in d, first one is random, the other must be as far away as possible from the others
    clusters = []
    clusters.append([randint(0, len(d)-1)])
    while len(clusters) < k:
        #Find the game that is farthest away from 
        bestRow = -1
        bestAvg = 0
        for r in range(len(d)):
            #Make sure this r is a medoid already
            inCluster = False
            for i in range(len(clusters)):
                if r == clusters[i][0]: inCluster = True
            if inCluster == False:
                s = 0
                for i in range(len(clusters)):
                    s += dis(w, d[clusters[i][0]], d[r])
                s = s / len(clusters)
                if s > bestAvg: 
                    bestAvg = s
                    bestRow = r
        clusters.append([bestRow])
    print(clusters)
    
    #Perform the initial clustering
    prevCluster, clusters = cluster(clusters, d, w)
    print(clusters)
    newCluster, clusters = cluster(clusters, d, w)
    print(clusters)
    
    #Loop until the next clustering and previous clustering are equivalent
    while compareClusters(prevCluster, newCluster) == False:
        prevCluster = newCluster
        newCluster, clusters = cluster(clusters, d, w)
        print(clusters)
    return clusters

def avgDist():
    avgs = []
    for k in range(1,21):
        c = clusterFull(k)
        d, conv = normalizeData(getData())
        w = calculateWeights(d, 0.2)
        s = 0
        for r in range(len(d)):
            minDis = 1
            for cl in range(len(c)):
                cDis = dis(w, d[r], d[c[cl][0]])
                if cDis < minDis: minDis = cDis
            s += minDis
        avgs.append(s / len(d))
    return avgs

def createTrainingData(d,c,w):
    x_input = []
    y_output = []
    #Loop through all games and find the medoid it is closest to 
    for r in range(len(d)):
        closMedoid = -1
        #Loop through the clusters and find the one we are closest to
        minDis = 1
        for cl in range(len(c)):
            tDis = dis(w, d[r], d[c[cl][0]])
            if tDis < minDis: 
                minDis = tDis
                closMedoid = c[cl][0]
        x_input.append([d[r][0:10]])
        y_output.append([closMedoid/267])
    return np.array(x_input), np.array(y_output)
clus = clusterFull(6)
d, c = normalizeData(getData())
w = calculateWeights(d, 0.2)
# #avgs = avgDist()
# weights = []
# for pct in range(1,101):
#     weights.append(calculateWeights(d, pct / 100))
modelGames = []
og_data = getData()
for i in range(len(clus)):
    modelGames.append([clus[i][0],og_data[clus[i][0]]])

x_in, y_out = createTrainingData(d, clus, w)
net = Network()
net.add(FCLayer(10, 96))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(96, 64))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(64, 48))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(48, 32))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(32, 16))
net.add(ActivationLayer(tanh, tanh_prime))
net.add(FCLayer(16, 1))
net.add(ActivationLayer(tanh, tanh_prime))

#Train
net.use(mse, mse_prime)
net.fit(x_in,y_out,epochs=4000,learning_rate=0.1)

#Predict a Game
out = net.predict([d[0][0:10]])
print(int(out[0][0]*267))