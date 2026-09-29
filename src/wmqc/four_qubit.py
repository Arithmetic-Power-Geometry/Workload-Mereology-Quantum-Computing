from __future__ import annotations

import math
import numpy as np

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def kron4(a, b, c, d):
    return np.kron(np.kron(np.kron(a, b), c), d)


def op_on_qubit(op: np.ndarray, q: int) -> np.ndarray:
    ops = [I2, I2, I2, I2]
    ops[q] = op
    return kron4(*ops)


def zz(q1: int, q2: int) -> np.ndarray:
    ops = [I2, I2, I2, I2]
    ops[q1] = Z
    ops[q2] = Z
    return kron4(*ops)


def hamiltonian(J: float = 1.0) -> np.ndarray:
    return J * (zz(0, 1) + zz(2, 3))


def unitary(J: float, t: float) -> np.ndarray:
    H = hamiltonian(J)
    vals, vecs = np.linalg.eigh(H)
    return (vecs * np.exp(-1j * vals * t)) @ vecs.conj().T


def heisenberg_x1(J: float, t: float) -> np.ndarray:
    U = unitary(J, t)
    x1 = op_on_qubit(X, 0)
    return U.conj().T @ x1 @ U


def analytic_heisenberg_x1(J: float, t: float) -> np.ndarray:
    x1 = op_on_qubit(X, 0)
    y1z2 = kron4(Y, Z, I2, I2)
    return math.cos(2 * J * t) * x1 - math.sin(2 * J * t) * y1z2


def workload_scrambling_proxy(J: float, t: float) -> float:
    return math.sin(2 * J * t) ** 2


def physical_scrambling_proxy(J: float, t: float) -> float:
    _ = (J, t)
    return 0.0


def commutator_scrambling(J: float, t: float) -> float:
    """Normalized squared commutator between X1(t) and X2.

    For this benchmark the normalization gives sin^2(2 J t).
    """
    a_t = heisenberg_x1(J, t)
    b = op_on_qubit(X, 1)
    comm = a_t @ b - b @ a_t
    d = comm.shape[0]
    return float(np.linalg.norm(comm, "fro") ** 2 / (4.0 * d))
