import numpy as np
import h5py

class world(object):
    def __init__(self, data, L):
        self.data = data
        self.L = L
        self.set_step(-1)
    def set_step(self, step):
        """Set the step from which to take the positions"""
        self._step = step
        self._r = self.data[step]
        self._L = np.copy(self.L[step])
    def dist_sq(self, i, j):
        """Computes the minimum image squared distance"""
        rij = self._r[i]-self._r[j]
        L = np.copy(self._L)
        for idx in range(3):
            if rij[idx]<-L[idx]/2.:
                rij[idx] += L[idx]
            elif rij[idx]>L[idx]/2.:
                rij[idx] -= L[idx]
        return np.sum(rij**2)

    def loop_rdf(self):
        dx = 0.1
        N_bins = 40
        rdf = np.zeros(N_bins)
        rsq_max = (N_bins*dx)**2
        for i in range(self._r.shape[0]):
            for j in range(i+1,self._r.shape[0]):
                rsq = self.dist_sq(i,j)
                if rsq<=rsq_max:
                    rdf[np.floor(np.sqrt(rsq)/dx)] += 1
        rdf[:] = rdf[:]/(2*np.pi*dx**3*(np.arange(N_bins)+0.5)**2*self._r.shape[0])
        return dx, rdf

    def semi_vector_rdf(self):
        dx = 0.08
        N_bins = 50
        rdf = np.zeros(N_bins)
        rsq_max = (N_bins*dx)**2
        L = np.copy(self._L)
        for i in range(self._r.shape[0]):
            r0 = np.copy(self._r[i]).reshape((1,-1))
            r0ri = r0 - self._r
            for idx in range(3):
                mask = (r0ri < -L[idx]/2.)
                r0ri[mask] += L[idx]
                mask = (r0ri > L[idx]/2.)
                r0ri[mask] -= L[idx]
            dist = np.sqrt(np.sum(r0ri**2, axis=1))
            rdf += np.bincount(np.array(np.floor(dist/dx), dtype=np.int64), minlength=N_bins)[:N_bins]
        rdf[:] = rdf[:]/(4*np.pi*dx**3*(np.arange(N_bins)+0.5)**2*self._r.shape[0])
        rdf[0] = 0
        return dx, rdf

import sys
a = h5py.File(sys.argv[1], 'r')
W = world(a['/particles/all/position/value'], a['/particles/all/box/edges/value'])

rdf_data = []
for step in range(0,W.data.shape[0]//2):
    W.set_step(step)
    dx, rdf = W.semi_vector_rdf()
    rdf_data.append(np.copy(rdf))
rdf_data = np.array(rdf_data)

m = rdf_data.mean(axis=0)
r = dx*np.arange(len(m))

np.savetxt(sys.argv[2], np.array((r, m)).T)
