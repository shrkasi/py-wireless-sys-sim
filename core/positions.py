import numpy as np
from scipy.spatial.distance import euclidean


def gen_uni_circ_pos(center, r, n):
    theta = np.random.rand(n) * 2 * np.pi
    r1 = np.random.rand(n) * r
    r2 = np.random.rand(n) * r
    rpos = np.maximum(r1, r2)
    return rpos * np.exp(theta*1j)


def cal_dist_2d(p1, p2):
    """
    Args:
    p1 (numpy array or scalar): positions represented by complex number.
    p2 (numpy array or scalar): positions represented by complex number.
    .. note::
    If both p1 and p2 are numpy arrays, they should be same size.

    Returns:
    numpy array of distances.
    """
    return np.abs(p1 - p2)


def cal_dist_3d(p1, p2):
    """
    Args:
    p1 (numpy array or scalar): x, y, z.
    p2 (numpy array or scalar): x, y, z.
    .. note::
    If both p1 and p2 are numpy arrays, they should be same size.

    Returns:
    numpy array of distances.
    """
    return np.array(map(euclidean, p1, p2))
