import WieckSosaMichael_Lab3mod as vector

#sum function
xvec=[2.3,-4.6,2.9,11.13]
yvec=[3.2,4.2,-3.3,7.3]
sumvec=vector.sum(xvec,yvec)
print ("The sum of",xvec,"and",yvec,"is",sumvec)

#diff function
xvec=[3.32,-2.34,6.43,32.3]
yvec=[2.24,3.2,-4.3,6.8]
diffvec=vector.diff(xvec,yvec)
print("The difference of",xvec,"and",yvec,"is",diffvec)

#scale function
scal=4.3
xvec=[2.3,6.63,-2.5,9.9]
scalevec=vector.scale(xvec,scal)
print("The scalar multiplication of scalar",scal,"and vector",xvec,"is",scalevec)

#lincomb function
xListVec=[[5.55,-3.22,8.32],[2.34,-7.43,9.7],[-6.32,3.66,9.22]]
scalList=[3.22,4.33,-7.88]
linearComb=vector.lincomb(xListVec,scalList)
print ("The linear combination of scalars",scalList,"and vectors",xListVec,"is",linearComb)

#dot function
xvec=[-3.22,4.66,3.33,9.99]
yvec=[9.32,4.21,-6.32,2.39]
dotProd=vector.dot(xvec,yvec)
print("The dot product of vectors",xvec,"and",yvec,"is",dotProd)

#proj function
xvec=[-1.11,9.87,3.21,9.11]
yvec=[3.2,-0.1,-10.1,-2.33]
projxOntoy=vector.proj(xvec,yvec)
print("The projection of vector",xvec,"onto",yvec,"is",projxOntoy)


#perp function
xvec=[-3.2,4.3,9.2,1.1]
yvec=[6.4,2.3,-9.33,-3.2]
perpvec=vector.perp(xvec,yvec)
print("The vector of length",xvec,"perpendicular to",yvec,"is",perpvec)


#refl function
xvec=[-3.32,2.33,4.99,10.77]
yvec=[5.66,9.22,-10.3,4.2]
reflvec=vector.refl(xvec,yvec)
print("The reflection of vector",xvec,"across vector",yvec,"is",reflvec)

#angle function
xvec=[9.2,3.1,-10.2,4.9]
yvec=[9.9,-7.2,3.2,4.1]
angleDegDefault=vector.angle(xvec,yvec)
print("The angle between vector",xvec,"and",yvec,"is",angleDegDefault)
