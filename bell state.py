from pyquil.api import WavefunctionSimulator
from pyquil import Program
from pyquil.gates import H, CNOT


P = Program(H(1))
P += Program (CNOT(1,0))
wfn = WavefunctionSimulator().wavefunction(p)

print(wfn)


