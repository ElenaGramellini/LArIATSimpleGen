import ROOT
from ROOT import *
import sys,os
import math
import argparse


def pdg2Mass(pdg) :
    mass = 0;
    pdg = math.fabs(float(pdg))
    if (pdg == 11):
        mass = 0.511
    if (pdg == 13):
        mass = 105.658374
    if (pdg == 211):
        mass = 139.570
    if (pdg == 321):
        mass = 493.667
    if (pdg == 2212):
        mass = 938.28

    if (mass):
        return mass
    sys.exit("no valid pdg") 

def EnergyCalc(mass, momentum):
    E = math.sqrt(momentum*momentum + mass*mass);
    return  E  






# This code takes as an argument the file 
# we need to generate metadata for
parser = argparse.ArgumentParser()
parser.add_argument("pdg", help="insert pdg")
args = parser.parse_args()
pdg = args.pdg


fname = "referenceTree.root"
f = ROOT.TFile(fname)
t = f.Get("momentum") 


filename = "LArIATHepEvt_pdg_"+ str(pdg)  +".txt"
print "Opening the file..."
target = open(filename, 'w')

for event in t:
    Px      = event.momentumX
    Py      = event.momentumY
    Pz      = event.momentumZ
    Mass    = pdg2Mass(pdg)
    Energy  = EnergyCalc(Mass,event.momentumTot )
    X       = event.WC4X
    Y       = event.WC4Y

    line1 = "0 1"
    target.write(line1)
    target.write("\n")
    line2 = "1 " + str(pdg) + " 0 0 0 0 "+ str(Px) + " "+ str(Py) + " "+ str(Pz) + " "+ str(Energy) + " "+ str(Mass) + " "+ str(X) + " "+ str(Y) + " -100.0 0.0"
    target.write(line2)
    target.write("\n")



    
