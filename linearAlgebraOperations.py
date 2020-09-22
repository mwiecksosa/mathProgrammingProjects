from copy import copy, deepcopy
import numpy as np
import time
import math

def pivot(Ab):
    """
    pivot accepts an augmented matrix. It finds
    the row with the largest first entry and swaps it with the first row if
    the first row doesn't already have largest first entry.
    """
    nrows = Ab.shape[0]
    ncols = Ab.shape[1]

    piv = np.abs(Ab[0,0]) #start with element in first row, first column
    piv_row = 0

    for i in range(nrows):
        if np.abs(Ab[i,0]) > piv:
            piv = np.abs(Ab[i,0])
            piv_row = i

    if piv_row > 0: #only swap if not already top row
        tempRow = deepcopy(Ab[0])
        Ab[0] = Ab[piv_row]
        Ab[piv_row] = tempRow

    return Ab

def elim(Ab):
    """
    elim accepts an augmented matrix. It implements row operations
    to put zeros below the diagonal in first column and so on.
    """
    nrows = Ab.shape[0]
    ncols = Ab.shape[1]

    piv = 1.0 / float(Ab[0,0])

    for row in range(1,nrows):
        c = Ab[row,0] * piv
        for col in range(0,ncols):
            Ab[row,col] = Ab[row,col] - c*Ab[0,col]

    return Ab

def ech_form(Ab):
    """
    ech_form accepts an augmented matrix. It puts it in upper triangular form.
    """

    nrows = Ab.shape[0]
    ncols = Ab.shape[1]

    for i in range(nrows-1):
        Ab[i:nrows,i:ncols] = pivot(Ab[i:nrows,i:ncols])
        Ab[i:nrows,i:ncols] = elim(Ab[i:nrows,i:ncols])
    return Ab

def BackSub(Ab):
    """
    Solve the upper triangular system Ux = b by backward
    substitution.
    """

    nrows = Ab.shape[0]
    ncols = Ab.shape[1]

    x = np.zeros((ncols,1))
    
    x[nrows-1] = Ab[nrows-1,nrows] / Ab[nrows-1,nrows-1]

    for i in range(int(nrows-1),int(-1),int(-1)):
        for j in range(int(i+1),int(nrows)):
            Ab[i,nrows] = float(float(Ab[i,nrows]) - float(Ab[i,j]) * float(x[j]))
        x[i] = Ab[i,nrows] / Ab[i,i]
    return x


def Solve(A, b, *args, **kwargs):
    """
    Solve accepts an n by n ndarray A for the coefficient matrix
    and an n by 1 ndarray b for the right hand side. The return x
    is the n by 1 solution vector. The function solves the system
    Ax = b by the method of Gaussian elimination with pivoting.
    The function lets the user know if Gaussian elimination
    encounters a row of zeros (rank(A) < n), in which case it aborts.
    """


    if "bfile" in kwargs:
        filename = kwargs['bfile']
        b = np.loadtxt(filename)
        
    if "afile" in kwargs:
        filename = kwargs['afile']
        A = np.loadtxt(filename)

    A = A.reshape(A.shape[0],1)
    b = b.reshape(b.shape[0],1)
    
    A_nrows = A.shape[0]
    A_ncols = A.shape[1]

    b_nrows = b.shape[0]
    b_ncols = b.shape[1]

    A_len = A_nrows * A_ncols
    b_len = b_nrows * b_ncols

    A_new_ncols = (A_len / b_len)
    A_new_nrows = (A_len / A_new_ncols)

    A = A.reshape(int(A_new_nrows),int(A_new_ncols))
    b = b.reshape(int(b_len),int(1))
        
    Ab = np.hstack((A,b))

    try:
        if "timing" in args:
            t0 = time.perf_counter() #measure time
        Ab = ech_form(Ab)
        if "timing" in kwargs:
            t1 = time.perf_counter() - t0 #seconds elasped in process
            print("Time elapsed in Gaussian elimination process is",t1)
        if "timing" in args:
            t2 = time.perf_counter() #measure time
        x = BackSub(Ab)
        if "timing" in kwargs:
            t3 = time.perf_counter() - t2 #seconds elasped in process
            print("Time elapsed in Backward Substitution process is",t3)
    except ZeroDivisionError:
        print("ZeroDivisionError: Encountered a row of zeros (rank(A) < n). Cannot divide by zero")

    if "xfile" in kwargs:
        np.savetxt(kwargs["xfile"],x.T) #transpose of solution vector to return, dim 1 by n
    if "absolute" in args:
        r = b - A@x
        print("Norm of residual is",r)
    if "relative" in args:
        r = b - A@x
        re = np.linalg.norm(r) / np.linalg.norm(b)
        print("The relative error is",re)

    return x.T #transpose of solution vector to return, dim 1 by n
