'''Parameters for a Leaky Integrate-and-Fire (LIF) Neuron Simulation, by Lyza Marino'''
from dataclasses import dataclass

@dataclass
class NeuronParams:
    """Parameters for a Leaky Integrate-and-Fire neuron."""
    v_rest: float = -65
    v_reset: float = -70
    v_thresh: float = -50
    v_spike: float = 40
    tau: float = 20
    time_step: float = 0.1
    run_time: float = 100