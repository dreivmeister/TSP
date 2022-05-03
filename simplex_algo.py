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
base_vars = np.array(range((n-m)+1, n+1))
#indices of non_base_vars
non_base_vars = np.array(range(1, (n-m)+1))

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

def kreisregel(AE, b, nbv, pivot_r, pivot_c):
    pass



#AE-extended coeff. matrix
#b-rhs
#z-coeffs of z(x)
#m-num. of rows/ineqs.
#n-num. of vars incl. slack vars
def simplex(AE, b, z, bv, nbv):
    #start with base sol.
    pivot_col = compute_delta_zj(AE, z, nbv)
    pivot_row = compute_theta_min(AE, b, pivot_col)

    #find pivot col (which var to include)
    #find pivot row (which var to exclude)
    #kreisregel on everything except pivot row and base cols
    #compute z(x) and edge coors.




