# -*- coding: utf-8 -*-
"""
@author: recon
"""
import csv
from math import sqrt
#We are going to give X inputs for each of the 64 teams
#Mean PPG, Standard Deviation PPG, Mean OPPG, Standard Deviation OPPG, Games Won, Games Lost
def get_training_data():
    input_data = []
    years = ["2019","2021","2022"]
    regions = ["South","East","Midwest","West"]
    
    #Loop through the years
    for y in range(len(years)):
        #Loop through the regions
        sample_data = []
        for r in range(4):
            #Loop through the seeds in the region
            for s in range(16):
                #Get the data from the appropriate CSV
                file = open("C:/Users/recon/Documents/Spyder/March Madness/Past Data/"+years[y]+"/"+regions[r]+"/"+str(s+1)+".csv", "r")
                data = list(csv.reader(file, delimiter=","))
                file.close()
                pf = []
                pa = []
                wins = 0
                losses = 0
                #Loop through the rows of data and collect the necessary data
                for d in range(len(data)):
                    if data[d][8] == 'W': wins += 1
                    if data[d][8] == 'L': losses += 1
                    if str(data[d][9]).isnumeric() == True:
                        pf.append(int(data[d][9]))
                        pa.append(int(data[d][10]))
                #Now Calculate the two means and standard deviations
                pfm = float(sum(pf)) / float(len(pf))
                pam = float(sum(pa)) / float(len(pa))
                s1 = 0
                s2 = 0
                for v in range(len(pf)):
                    s1 += (pf[v] - pfm)**2
                    s2 += (pa[v] - pam)**2
                s1 = sqrt(s1 / len(pf))
                s2 = sqrt(s2 / len(pa))
                sample_data.append(pfm)
                sample_data.append(pam)
                sample_data.append(s1)
                sample_data.append(s2)
                sample_data.append(wins)
                sample_data.append(losses)
        input_data.append([sample_data])
    return input_data