"""Taken from https://github.com/CullanHowlett/NFWdist/blob/master/python/NFWdist.py

The Standard Distribution Functions for the 3D NFW Profile

Density, distribution function, quantile function and random generation for the 3D NFW profile

Usage:
dnfw(x, con = 5, log = FALSE)
pnfw(q, con = 5, logp = FALSE)
qnfw(p, con = 5, logp = FALSE)
rnfw(n, con = 5)

dnfw gives the density, pnfw gives the distribution function, qnfw gives the quantile function, and rnfw generates random deviates.

Arguments:
  x, q: array_like
    Vector of quantiles. This is scaled such that x=R/Rvir for NFW. This means the PDF is only defined between 0 and 1.

  p: array_like
    Vector of probabilities

  n: array_like
    Number of observations. If n has the attribute 'len()', i.e., is not a scalar, the length is taken to be the number required.

  con: scalar/array_like, optional
    The NFW profile concentration parameter, where c=Rvir/Rs.
    If con is scalar then the output of the routines is array_like with with shape(len(q)).
    If con is array_like then the output of the routines is array_like with shape(len(q),len(con))

  log, logp: logical, optional
    if True, probabilities/densities p are returned as log(p).

Examples:
  see test.py

Notes:
  The novel part of this package is the general solution for the CDF inversion (i.e. qnfw).
  As far as we can see this has not been published anywhere, and it is a useful function for populating halos in something like an HOD.
  This seems to work at least as efficiently as accept/reject, but it is ultimately much more elegant code in any case.

Authors:
  Cullan Howlett & Aaron Robotham
"""

import numpy as np
from scipy import special


def pnfwunorm(q, con=5):
    if hasattr(con, "__len__"):
        y = np.outer(q, con)
    else:
        y = q * con
    return np.log(1.0 + y) - y / (1.0 + y)


def dnfw(x, con=5, log=False):
    if hasattr(con, "__len__"):
        con = np.array(con)
        d = np.outer(x, con**2) / (
            (np.outer(x, con) + 1.0) ** 2
            * (1.0 / (con + 1.0) + np.log(con + 1.0) - 1.0)
        )
    else:
        d = (x * con**2) / (
            ((x * con) + 1.0) ** 2 * (1.0 / (con + 1.0) + np.log(con + 1.0) - 1.0)
        )
    if hasattr(x, "__len__"):
        d[x > 1] = 0
        d[x <= 0] = 0
    else:
        if x > 1:
            d = 0
        elif x <= 0:
            d = 0
    if log:
        return np.log(d)
    else:
        return d


def pnfw(q, con=5, logp=False):
    p = pnfwunorm(q, con=con) / pnfwunorm(1, con=con)
    if hasattr(q, "__len__"):
        p[q > 1] = 1
        p[q <= 0] = 0
    else:
        if q > 1:
            p = 1
        elif q <= 0:
            p = 0
    if logp:
        return np.log(p)
    else:
        return p


def qnfw(p, con=5, logp=False):
    if logp:
        p = np.exp(p)
    if hasattr(p, "__len__"):
        p[p > 1] = 1
        p[p <= 0] = 0
    else:
        if p > 1:
            p = 1
        elif p <= 0:
            p = 0
    if hasattr(con, "__len__"):
        p = np.outer(p, pnfwunorm(1, con=con))
    else:
        p *= pnfwunorm(1, con=con)
    return (-(1.0 / np.real(special.lambertw(-np.exp(-p - 1)))) - 1) / con


def rnfw(n, con=5):
    if hasattr(n, "__len__"):
        n = len(n)
    return qnfw(np.random.rand(int(n)), con=con)
