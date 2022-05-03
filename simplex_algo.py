#given a lop problem in standardform (max, Ax<=b, b>=0, x>=0=)
import numpy as np
from pandas import pivot

#coeffs of z(x) (two vars)
z = np.array([1,2], dtype=np.int32)
#coeffs of system of ineqs.
A = np.array([[1,4],[1,1],[4,1]], dtype=np.int32)
#rhs of system of ineqs.
b = np.array([28,10,28], dtype=np.int32)
#m-num rows/ineqs. n-num vars witho. slack vars
m,n=A.shape[0],A.shape[1]
#identity mat. in m*m dim.
E = np.identity(m, dtype=np.int32)
#extended A by E for simplex
AE = np.append(A, E, axis=1)
n+=m

#indices [1,n]
#indices of base_vars
base_vars = set(range((n-m)+1, n+1))
#indices of non_base_vars
non_base_vars = set(range(1, (n-m)+1))

def compute_delta_zj(AE, z, nbv):
    result = 10e6
    pivot_col = 0
    m = len(z)
    for v in nbv:
        curr = 0
        for i in range(m):
            curr += AE[i][v-1]*z[i]
        if curr < result:
            pivot_col = v
    if pivot_col>0:
        return -1
    return pivot_col

def compute_theta_min(AE, b, pivot_col):
    result = 10e6
    pivot_row = 0
    m = len(b)
    for i in range(m):
        curr = b[i]/AE[i][pivot_col-1]
        if curr < result:
            pivot_row = i+1
    return pivot_row

def kreisregel(AE, b=None, row, col, pivot_row, pivot_col, pivot_el):
    if not b:
        return AE[row][col]-(AE[row][pivot_col]*AE[pivot_row][col])/pivot_el
    return b[row]-(AE[row][pivot_col]*b[pivot_row])*pivot_el



#AE-extended coeff. matrix
#b-rhs
#z-coeffs of z(x)
#m-num. of rows/ineqs.
#n-num. of vars incl. slack vars
def simplex(AE, b, z, bv, nbv):
    m,n=AE.shape[0],AE.shape[1]
    #start with base sol.
    pivot_col = compute_delta_zj(AE, z, nbv)
    pivot_row = compute_theta_min(AE, b, pivot_col)
    pivot_el = AE[pivot_row][pivot_col]
    
    #exchange pivot_col+1 for pivot_row+1 from nbv to bv
    nbv.remove(pivor_col+1)
    nbv.add(pivot_row+1)
    bv.remove(pivot_row+1)
    bv.add(pivot_col+1)
    
    while pivot_col!=-1:
        for i in range(m):
            for j in range(n):
                if j+1 not in bv and i!= pivot_col:
                    if j<n:
                        AE[i][j]=kreisregel(AE, i, j, pivot_row, pivot_col, pivot_el)
                    else:
                        AE[i][j]=kreisregel(AE, b, i, j, pivot_row, pivot_col, pivot_el)
        pivot_col = compute_delta_zj(AE, z, nbv)
        pivot_row = compute_theta_min(AE, b, pivot_col)
        pivot_el = AE[pivot_row][pivot_col]
        
        nbv.remove(pivor_col+1)
        nbv.add(pivot_row+1)
        bv.remove(pivot_row+1)
        bv.add(pivot_col+1)
        
        compute_z_val(z, bv)
        get_edge(b, bv)
        
        

    #find pivot col (which var to include)
    #find pivot row (which var to exclude)
    #kreisregel on everything except pivot row and base cols
    #compute z(x) and edge coors.




