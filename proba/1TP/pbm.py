# -*- coding: utf-8 -*-
# ********************
#
# TP1 - Proba-Stat-ThI
#
# Fonction de lecture/ecrite de fichiers pbm
#
#

# fonction writepbm
# arg :
#       filename: nom du fichier dans lequel écrire
#       x: dimension horizontal
#       y: dimension vertical
#       im: tableau 1D contenant l'image
#
# Ecrit dans filename l'image au format pbm
#
def writepbm(filename,x,y,im):
    f = open(filename,"w")
    f.write("P1\n")
    f.write(str(x)+" "+str(y)+"\n")
    for i in range(x*y):
        f.write(str(im[i]))
        if((i+1)%70==0):
            f.write("\n")
    f.close()
    

# fonction writepbm
# arg :
#       filename: nom du fichier dans lequel écrire
#
# Lit depuis filename l'image au format pbm
# retourne un tableau 1D corrspondant à l'image, ses dimension et le type
# (image,x,y,type)
#
# usage im,x,y,t = readpbm("im.pbm")
def readpbm(filename):
    f = open(filename,"r")
    s = f.readlines()
    im=[]
    deb=False
    size_x=0
    size_y=0
    nbline=0
    type_f=""
    for line in s:
        if((line[0]!='#') and (deb)):
            for c in line:
                if(c!='\n'):
                    im.append(int(c))
        elif(line[0]!='#'):
            if(nbline==0):
                print(line)
                type_f=str.split(line)[0]
                nbline+=1
            elif(nbline==1):
                print(line)
                words = str.split(line)
                size_x=int(words[0])
                size_y=int(words[1])
                nbline+=1
                deb=True
    f.close()
    return im,size_x,size_y,type_f
