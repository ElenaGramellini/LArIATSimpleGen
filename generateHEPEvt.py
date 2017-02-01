import ROOT
from ROOT import *
import sys,os



fname = "blahblah.root"
f = ROOT.TFile(fname)
t = f.Get("momentumTree")

for event in t :
    momentum  = event.P
    Px  = event.Px
    Py  = event.Py
    Pz  = event.Pz


raw_input()


    
