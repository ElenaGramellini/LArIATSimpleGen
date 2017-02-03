# Copyright (C) 2017-2017 Elena Gramellini <elena.gramellini@yale.edu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You can read copy of the GNU General Public License here:
# <http://www.gnu.org/licenses/>.

"""@package docstring
Scope of this python script: convert ROOT TTree to HEPEvt format for LArIAT MC
Author: Elena Gramellini
Creation Date: 2016-12-03 
Version 0 
-----------------------------------------------------------------------
Input: name of the root file, name of the ttree, pdg code for particle to generate
Output: a text file with tabulated HEPEvt
"""   


import ROOT
from ROOT import *
import sys,os
import math
import argparse

# This function assigns the mass given the pdg code
def pdg2Mass(pdg) :
    mass = 0;
    pdg = math.fabs(float(pdg))
    if (pdg == 11):
        mass = 0.000511
    if (pdg == 13):
        mass = 0.105658374
    if (pdg == 211):
        mass = 0.139570
    if (pdg == 321):
        mass = 0.493667
    if (pdg == 2212):
        mass = 0.93828

    if (mass):
        return mass
    sys.exit("no valid pdg") 

# This function assigns the energy given the mass and momentum
# Relativistic formula is used 
def EnergyCalc(mass, momentum):
    E = math.sqrt(momentum*momentum + mass*mass);
    return  E  






# This code takes as an argument the file 
# we need to generate metadata for
parser = argparse.ArgumentParser()
parser.add_argument("pdg", help="insert pdg")
parser.add_argument("fname"   , nargs='?', default = 'referenceTree.root', type = str, help="insert fileName")
parser.add_argument("treeName", nargs='?', default = 'momentum'          , type = str, help="insert treeName")

#fname    = "referenceTree.root"
#treeName = "momentum"

args = parser.parse_args()
pdg       = args.pdg
fname     = args.fname   
treeName  = args.treeName

print fname, treeName

f = ROOT.TFile(fname)
t = f.Get(treeName)


filename = "LArIATHepEvt_pdg_"+ str(pdg)  +".txt"
print "Opening the file..."
target = open(filename, 'w')

i = 0
for event in t:
    Px      = float(event.momentumX)/1000.
    Py      = float(event.momentumY)/1000.
    Pz      = float(event.momentumZ)/1000.
    Mass    = pdg2Mass(pdg)
    Energy  = EnergyCalc(Mass,float(event.momentumTot)/1000. )
    X       = event.WC4X
    Y       = event.WC4Y

    line1 = str(i) + " 1"
    target.write(line1)
    target.write("\n")
    line2 = "1 " + str(pdg) + " 0 0 0 0 "+ str(Px) + " "+ str(Py) + " "+ str(Pz) + " "+ str(Energy) + " "+ str(Mass) + " "+ str(X) + " "+ str(Y) + " -100.0 0.0"
    target.write(line2)
    target.write("\n")
    i += 1


    
