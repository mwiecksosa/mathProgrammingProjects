#Name: Michael Wieck-Sosa
#Date: Feb 14, 2019
#Assignement: Lab 2

#1
#import libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.collections as coll

x = np.linspace(-2.0,1,1000) #set domain and # of pts
plt.plot(x,x**3+x**2+1.0,'-g') #plot fn
#create standard 2-dim Cartesian plane
plt.title('Cubic Function Graph')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend(['y = x**3 + x**2 + 1'], loc='upper left')
#plot blue quadrilaterial
#vertices at origin, y-int, x-int, local max
z = [0, 0, -0.75, -1.5, 0]
w = [0, 1, 1.15, -0.15, 0]
plt.fill(z, w, 'b')
plt.show()
        
#2
def Real(z):
        a=[]
        for i in range(0,len(z)):
                a.append(z[i].real)
        return a
def Imag(z):
        b=[]
        for i in range(0,len(z)):
                b.append(z[i].imag)
        return b
z=[(2+9j),(10+4j),(4+5j)]
a=Real(z)
b=Imag(z)
print("Complex list:",z)
print("Real part:",a)
print("Imag part:",b)

#3a
def GetBunnyCloudData(): #define function "GetBunnyCloudData()"
    f=open("bunny_cloud.dat", "r") #open "bunny_cloud.dat" data file for 'r'eading is assigned to f
    DATA=f.readlines() #Data from "bunny_clout.dat" is read onto and stored in DATA               
    N=len(DATA) #N is the number of lines of the data stored in DATA  
    z=[] #z is empty list
    for s in DATA: #s is iterating through each line in DATA
        ss=s.split() #s.split returns a list of two strings, stored in ss
        a=float(ss[0]) #the first element of list ss is stored in a, and changed to float type
        b=float(ss[1]) #the second element of list ss is stored in b, and changed to float type
        z.append(a+b*1j) # "a+b*1j" is appended to the list z
    return z #returns z, the list of all complex numbers from data file, after for loop is done

#3b
z=GetBunnyCloudData()
a=Real(z)
b=Imag(z)
plt.plot(a, b, 'yo')
#create standard 2-dim Cartesian plane
plt.title('Plot of Yellow Bunny and House')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()


#3c
x_vals=[0,0,0.5,1,1,1,0,0,1]
y_vals=[0,1,1.25,1,0,1,1,0,0]
plt.plot(x_vals,y_vals,'-y', a, b, 'yo')
plt.title('Plot of Yellow Bunny and House')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()


#4
def scale(z,c):
        z_scale=[x*c for x in z]
        return z_scale

def trans(z,z0):
        z_trans=[x+z0 for x in z]
        return z_trans

def conju(z):
        b=Imag(z)
        b2=[x*(-2) for x in b]
        zero_b2_list=[]
        for i in range(0,len(b2)):
                zero_b2_list.append(0+b2[i]*1j)
        z_conju=[sum(x) for x in zip(z,zero_b2_list)]
        return z_conju

import math
def rotat(z,a):
        x_val=Real(z)
        y_val=Imag(z)
        x_cos=[x*math.cos(a) for x in x_val]
        y_sin=[y*(-1*math.sin(a)) for y in y_val]
        x_rotat=[sum(x) for x in zip(x_cos,y_sin)]
        x_sin=[x*math.sin(a) for x in x_val]
        y_cos=[y*math.cos(a) for y in y_val]
        y_rotat=[sum(y) for y in zip(x_sin,y_cos)]
        z_rotat=[]
        for i in range(0,len(z)):
                z_rotat.append(x_rotat[i]+y_rotat[i]*1j)
        return z_rotat

#5
zb=GetBunnyCloudData()

zh=[]
x_vals=[0,0,0.5,1,1,1,0,0,1]
y_vals=[0,1,1.25,1,0,1,1,0,0]
for i in range(0,len(x_vals)):
        zh.append(x_vals[i]+y_vals[i]*1j)

#Scaling by c = 3 in red
zb_scale=scale(zb,3)
zh_scale=scale(zh,3)

zb_scale_x=Real(zb_scale)
zb_scale_y=Imag(zb_scale)
zh_scale_x=Real(zh_scale)
zh_scale_y=Imag(zh_scale)

plt.plot(zb_scale_x,zb_scale_y,'ro',zh_scale_x,zh_scale_y,'-r')
plt.title('Plot of Red Scaled Bunny and House Transformation')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#Translation by z0 = 1 - 2j in blue
zb_trans=trans(zb,(1-2*1j))
zh_trans=trans(zh,(1-2*1j))

zb_trans_x=Real(zb_trans)
zb_trans_y=Imag(zb_trans)
zh_trans_x=Real(zh_trans)
zh_trans_y=Imag(zh_trans)

plt.plot(zb_trans_x,zb_trans_y,'bo',zh_trans_x,zh_trans_y,'-b')
plt.title('Plot of Translated Blue Bunny and House Transformation')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#Conjugation in green
zb_conju=conju(zb)
zh_conju=conju(zh)

zb_conju_x=Real(zb_conju)
zb_conju_y=Imag(zb_conju)
zh_conju_x=Real(zh_conju)
zh_conju_y=Imag(zh_conju)

plt.plot(zb_conju_x,zb_conju_y,'go',zh_conju_x,zh_conju_y,'-g')
plt.title('Plot of Conjugate Green Bunny and House Transformation')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#Rotation by a = 3 pi / 4 in black 'k'
zb_rotat=rotat(zb,(3.14159*0.75))
zh_rotat=rotat(zh,(3.14159*0.75))

zb_rotat_x=Real(zb_rotat)
zb_rotat_y=Imag(zb_rotat)
zh_rotat_x=Real(zh_rotat)
zh_rotat_y=Imag(zh_rotat)

plt.plot(zb_rotat_x,zb_rotat_y,'ko',zh_rotat_x,zh_rotat_y,'-k')
plt.title('Plot of Rotated Black Bunny and House Transformation')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#6

#Rotation by a = 3 pi / 4 in black 'k'
zb_rotat=rotat(zb,(3.14159*0.75))
zh_rotat=rotat(zh,(3.14159*0.75))

#Translation by z0 = 1 - 2j in blue
zb_trans=trans(zb_rotat,(1-2*1j))
zh_trans=trans(zh_rotat,(1-2*1j))

zb_trans_x=Real(zb_trans)
zb_trans_y=Imag(zb_trans)
zh_trans_x=Real(zh_trans)
zh_trans_y=Imag(zh_trans)

plt.plot(zb_trans_x,zb_trans_y,'co',zh_trans_x,zh_trans_y,'-c')
plt.title('Plot of Rotated then Translated Cyan Bunny and House Transformation')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

#Translation by z0 = 1 - 2j in blue
zb_trans=trans(zb,(1-2*1j))
zh_trans=trans(zh,(1-2*1j))
#Rotation by a = 3 pi / 4 in black 'k'
zb_rotat=rotat(zb_trans,(3.14159*0.75))
zh_rotat=rotat(zh_trans,(3.14159*0.75))

zb_rotat_x=Real(zb_rotat)
zb_rotat_y=Imag(zb_rotat)
zh_rotat_x=Real(zh_rotat)
zh_rotat_y=Imag(zh_rotat)

plt.plot(zb_rotat_x,zb_rotat_y,'mo',zh_rotat_x,zh_rotat_y,'-m')
plt.title('Plot of Translated then Rotated Magenta Bunny and House Transformation')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

print("The two cyan and magenta plots visualize that rotat(trans(z)) != trans(rotat(z))")
print("Now, we will formally prove that rotation and translation are not commutative transformations")
print("First, we will derive the translation then rotation of a complex pair")
print("Let a+b*j be an element of the set of complex numbers, where a and b are elements of the set of real numbers")
print("Let c+d*j be an element of the set of complex numbers, where c and d are elements of the set of real numbers")
print("The translation of a+b*j by c+d*j is given by: (a+b*i) + (c+d*j) = (a+c)+(b+d)*j")
print("Let t be an element of the set of real numbers from 0 to 360, inclusive")
print("The rotation of (a+c)+(b+d)*j by the angle t is given by Euler's formula")
print("The final result for translation by c+d*j then rotation by t of a+b*j is: ((a+c)*cos(t)-(b+d)*(sin(t))) + ((a+c)*sin(t)+(b+d)*cos(t))*j")
print("Second, we will derlive the rotation then translation of a complex pair")
print("Again, let a+b*j be an element of the set of complex numbers, where a and b are elements of the set of real numbers")
print("Let t be an element of the set of real numbers from 0 to 360, inclusive")
print("The rotation of a+b*j by the angle t is given by Euler's formula")
print("The result of rotation is: (a*cos(t)-b*sin(t)) + (a*sin(t)+b*cos(t))*j")
print("Let c+d*j be an element of the set of complex numbers, where c and d are elements of the set of real numbers")
print("The translation of (a*cos(t)-b*sin(t)) + (a*sin(t)+b*cos(t))*j by c+d*j is given by: ((a*cos(t)-b*sin(t))+c) + ((a*sin(t)+b*cos(t))+d)*j")
print("The final result for rotation by t then translation by c+d*j of a+b*j is: ((a*cos(t)-b*sin(t))+c) + ((a*sin(t)+b*cos(t))+d)*j")
print("Clearly, ((a+c)*cos(t)-(b+d)*(sin(t))) + ((a+c)*sin(t)+(b+d)*cos(t))*j =/= ((a*cos(t)-b*sin(t))+c) + ((a*sin(t)+b*cos(t))+d)*j")
print("Therefore, rotation and translation are not commutative transformations")
print("QED")


#7 (Extra Credit)
zb=GetBunnyCloudData()

zh=[]
x_vals=[0,0,0.5,1,1,1,0,0,1]
y_vals=[0,1,1.25,1,0,1,1,0,0]
for i in range(0,len(x_vals)):
        zh.append(x_vals[i]+y_vals[i]*1j)

#Translation by z0 = 4 + 0j in blue
zb_trans=trans(zb,(4+0*1j))
zh_trans=trans(zh,(4+0*1j))

#Reflection across the line theta = pi / 3
#Corresponds to the linear equation y = (3**2)*x+0
def reflec(z,m,b): #line must be of the form y = mx + b for this function
        x_vals=Real(z)
        y_vals=Imag(z)
        u1=[((1-m**2)*x)/((m**2)+1) for x in x_vals]
        u2=[(2*m*y)/((m**2)+1) for y in y_vals]
        u3=((-1)*2*m*b)/((m**2)+1)
        u_temp=[sum(x) for x in zip(u1,u2)]
        u=[x+u3 for x in u_temp]
        v1=[(((m**2)-1)*y)/((m**2)+1) for y in y_vals]
        v2=[(2*m*x)/((m**2)+1) for x in x_vals]
        v3=(2*b)/((m**2)+1)
        v_temp=[sum(x) for x in zip(v1,v2)]
        v=[x+v3 for x in v_temp]
        z_reflec=[]
        for i in range(0,len(z)):
                z_reflec.append(u[i]+v[i]*1j)
        return z_reflec

zb_reflec=reflec(zb_trans,(3**2),0)
zh_reflec=reflec(zh_trans,(3**2),0)

zb_reflec_x=Real(zb_reflec)
zb_reflec_y=Imag(zb_reflec)
zh_reflec_x=Real(zh_reflec)
zh_reflec_y=Imag(zh_reflec)

plt.plot(zb_reflec_x,zb_reflec_y,'go',zh_reflec_x,zh_reflec_y,'-g')
plt.title('Plot of Translated then Reflected Green Bunny and House Transformation')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

