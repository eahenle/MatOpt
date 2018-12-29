from decimal import Decimal

import time

#declare nanocyrstal matrix  ZrO2, ZnO, TiO2/ZrO2, SiHN, MgO, ZnS, SiO2, Hf02, NanoDiamond, TiO2 SOPRA 1, YV04, TiO2 Alternate, BGO, TiO2/SiO2

#open tables file to be readable and editable
table = open("material table.txt", "r")
#display tables for users
tableCon = table.read()
print(tableCon)

table.close()
# extract info from file of this table to be used throughout program
nanoM = []
table = open("material table.txt", "r")
for tabLine in table.readlines():
    # add a new sublist
    nanoM.append([])
    # loop over the elemets, split by comma
    for i in tabLine.split(','):
        # append to the last
        # element of the list
        nanoM[-1].append(i)    


T = time.time()

doc = open("results.txt", "a+", buffering=1, newline="\n")

Pdf_hi = 0
Pdf_lo = 0
Vgrin = 500
Dnavg = 0
#ask for user input
print("Greetings User!")

print("Enter the max difference between")
maxDiffPdfs = float(input("Pd,f_hi and Pd,f_lo:"))
maxPDf = float(input("Enter the max P(delta)d,f:"))
minVgrin = float(input("Enter the minimum Vgrin:"))
minDnAvg = float(input("Enter the minimum avg of (delta)n:"))

print("For the polymer rows, enter values of 1 to 3.")
iMin = int(input("Enter the first row for the np2 data:"))
iMax = int(input("Enter the last row for the np2 data:"))

jMin = int(input("Enter the first row for the np1 data:"))
jMax = int(input("Enter the last row for the np1 data:"))

print("For the nanocrystal rows, enter values of from 3 and 16.")

kMin = int(input("Enter the first row for the n4 data:"))
kMax = int(input("Enter the last row for the n4 data:"))

lMin = int(input("Enter the first row for the n3 data:"))
lMax = int(input("Enter the last row for the n3 data:"))

mMin = int(input("Enter the first row for the n2 data:"))
mMax = int(input("Enter the last row for the n2 data:"))

nMin = int(input("Enter the first row for the n1 data:"))
nMax = int(input("Enter the last row for the n1 data:"))

oMin = int(input("Enter the minimum value of percent 4:"))
oMax = int(input("Enter the maximum value of percent 4:"))

pMin = int(input("Enter the minimum value of percent 3:"))
pMax = int(input("Enter the maximum value of percent 3:"))

qMin = int(input("Enter the minimum value of percent 2:"))
qMax = int(input("Enter the maximum value of percent 2:"))

rMin = int(input("Enter the minimum value of percent 1:"))
rMax = int(input("Enter the maximum value of percent 1:"))
#loop
# for i = iMin to iMax
for i in range(iMin,iMax):
   # Get np2 data
    np2_486 = float(nanoM [i][1])
    np2_587 = float(nanoM [i][2])
    np2_656 = float(nanoM [i][3])
    # for j = jMin to jMax
    for j in range(jMin,jMax):
        # Get np1 data
        np1_486 = float(nanoM [j][1])
        np1_587 = float(nanoM [j][2])
        np1_656 = float(nanoM [j][3])
        # for k = kMin to kMax
        for k in range(kMin,kMax):
            # get n4 data (N4_486, N4_587, N4_656)
            n4_486 = float(nanoM [k][1])
            n4_587 = float(nanoM [k][2])
            n4_656 = float(nanoM [k][3])
            # for l = lMin to lMax
            for l in range(lMin,lMax):
                # get n3 data
                n3_486 = float(nanoM [l][1])
                n3_587 = float(nanoM [l][2])
                n3_656 = float(nanoM [l][3])            
                # for m = mMin to mMax
                for m in range(mMin,mMax):
                    # get n2 data
                    n2_486 = float(nanoM [m][1])
                    n2_587 = float(nanoM [m][2])
                    n2_656 = float(nanoM [m][3])               
                    # for n = nMin to nMax
                    for n in range(nMin,nMax):
                        # get n1 data
                        n1_486 = float(nanoM [n][1])
                        n1_587 = float(nanoM [n][2])
                        n1_656 = float(nanoM [n][3])                  
                        # for o = oMin to oMax
                        for o in range(oMin,oMax):
                            # PCT4 = o*0.003
                            Pct4 = o*0.003
                            dT = time.time() - T
                            T = time.time()
                            print(i,j,k,l,m,n,o,(Pdf_hi - Pdf_lo),Vgrin,Dnavg,dT)
                            # for p = pMin to pMax
                            for p in range(pMin,pMax):
                                # PCT3 = p*0.003
                                Pct3 = p*0.003
                                # for q = qMin to qMax
                                for q in range(qMin,qMax):
                                    # PCT2 = q*0.003
                                    Pct2 = q*0.003
                                    # for r = rMin to rMax
                                    for r in range(rMin,rMax):
                                        # PCT1 = r*003
                                        Pct1 = r*0.003
                                        # if (o + p <= 50 and q + r <= 50):
                                        #declare equations
                                        # DN_486 = xxxx
                                        Dn486 = (n1_486*Pct1+n2_486*Pct2+np1_486*(1-Pct1-Pct2))-(n3_486*Pct3+n4_486*Pct4+np2_486*(1-Pct3-Pct4))                                 
                                        # DN_587 = xxxx
                                        Dn587 = (n1_587*Pct1+n2_587*Pct2+np1_587*(1-Pct1-Pct2))-(n3_587*Pct3+n4_587*Pct4+np2_587*(1-Pct3-Pct4))                                 
                                        # DN_656 = xxxx
                                        Dn656 = (n1_656*Pct1+n2_656*Pct2+np1_656*(1-Pct1-Pct2))-(n3_656*Pct3+n4_656*Pct4+np2_656*(1-Pct3-Pct4))                                 
                                        # Pdf_hi = xxxx
                                        Pdf_hi = ((n1_587*Pct1+n2_587*Pct2+np1_587*(1-Pct1-Pct2))-(n1_486*Pct1+n2_486*Pct2+np1_486*(1-Pct1-Pct2)))
                                        Pdf_hi = Pdf_hi/((n1_656*Pct1+n2_656*Pct2+np1_656*(1-Pct1-Pct2))-(n1_486*Pct1+n2_486*Pct2+np1_486*(1-Pct1-Pct2)))
                                        # Pdf_lo = xxxx
                                        Pdf_lo = ((n3_587*Pct3+n4_587*Pct4+np2_587*(1-Pct3-Pct4))-(n3_486*Pct3+n4_486*Pct4+np2_486*(1-Pct3-Pct4)))
                                        Pdf_lo = Pdf_lo/((n3_656*Pct3+n4_656*Pct4+np2_656*(1-Pct3-Pct4))-(n3_486*Pct3+n4_486*Pct4+np2_486*(1- Pct3- Pct4)))                                  
                                        # PDF = xxxx
                                        if Dn656 == Dn486:
                                            PDf = 1e10
                                        else:
                                            PDf = (Dn587-Dn486)/(Dn656 - Dn486)
                                        # Vgrin = xxxx
                                        if Dn486 == Dn656:
                                            Vgrin = 1e10
                                        else: 
                                            Vgrin = Dn587/(Dn486 - Dn656)
                                        # Dnavg = xxxx
                                        Dnavg = (Dn486 + Dn587 + Dn656)/3                                  
                                  # IF ABS(Pdf_hi-Pdf_lo)<maxDiffPdfs
                                     # IF ABS(PDf)<maxPDf
                                        # IF ABS(Vgrin)>minVgrin
                                           # IF ABS(Dnavg)>minDnAvg
                                             # IF q + r <= 50
                                               # IF o + p <= 50
                                        if (abs(Pdf_hi - Pdf_lo) <= maxDiffPdfs
                                                and abs(PDf) <= maxPDf
                                                and abs(Vgrin) >= minVgrin 
                                                and abs(Dnavg) >= minDnAvg):
# Write "i,j,k,l,m,n,o,p,q,r,PCT1, PCT2,PCT3,PCT4,N1_486,N1_587,N1_656,N2_486,
#N2_587,N2_656,N3_486,N3_587,N3_656,N4_486,N4_587,N4_656,NP1_486,NP1_587,NP1_656
#,NP2_486,NP2_587,NP2_656,DN_486,DN_587,DN_656,Pdf_hi,Pdf_lo,ABS(Pdf_hi-Pdf_lo),
#ABS(PDF),ABS(Vgrin),ABS(Dnavg)"
                                            line = repr (i) 						# POLYMER2 ROW
                                            line = line + "," + repr(j)				# POLYMER1 ROW
                                            line = line + "," + repr(k)				# DOPANT4 ROW
                                            line = line + "," + repr(l)				# DOPANT3 ROW
                                            line = line + "," + repr(m)				# DOPANT2 ROW
                                            line = line + "," + repr(n)				# DOPANT1 ROW
                                            line = line + "," + repr(o)				# DOPANT4 INT%
                                            line = line + "," + repr(p)				# DOPANT3 INT%
                                            line = line + "," + repr(q)				# DOPANT2 INT%
                                            line = line + "," + repr(r)				# DOPANT1 INT%
                                            line = line + "," + repr(Pct1)			# DOPANT1 FLOAT%
                                            line = line + "," + repr(Pct2)			# DOPANT2 FLOAT%
                                            line = line + "," + repr(Pct3)			# DOPANT3 FLOAT%
                                            line = line + "," + repr(Pct4)			# DOPANT4 FLOAT%
                                            line = line + "," + repr(n1_486)		# DOPANT1 N(486)
                                            line = line + "," + repr(n1_587)		# ETC...
                                            line = line + "," + repr(n1_656)
                                            line = line + "," + repr(n2_486)
                                            line = line + "," + repr(n2_587)
                                            line = line + "," + repr(n2_656)
                                            line = line + "," + repr(n3_486)
                                            line = line + "," + repr(n3_587)
                                            line = line + "," + repr(n3_656)
                                            line = line + ","+ repr (n4_486)
                                            line = line + "," + repr(n4_587)
                                            line = line + "," + repr(n4_656)
                                            line = line + ","+ repr(np1_486)		# POLYMER1 N(486)
                                            line = line + ","+repr(np1_587)			# ETC...
                                            line = line + ","+repr(np1_656)
                                            line = line + ","+repr(np2_486)
                                            line = line + ","+repr(np2_587)
                                            line = line + ","+repr(np2_656)
                                            line = line + ","+repr(Dn486)			
                                            line = line + "," + repr(Dn587)
                                            line = line + "," + repr(Dn656)
                                            line = line + ","+repr(Pdf_hi)
                                            line = line + ","+repr(Pdf_lo)
                                            line = line+","+repr(abs(Pdf_hi-Pdf_lo))
                                            line = line + ","+repr(abs(PDf))
                                            line = line+","+repr(abs(Vgrin))
                                            line = line+","+repr(abs(Dnavg))
  
                                            print(line)
                                 
                                            doc.write(line+"\r\n")
# end
doc.close()