"""Simulating an LIF neuron via Euler method approximation
   Plotting both membrane potential vs time and firing rate vs input current
   By Lyza Marino
"""

import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass
from params import NeuronParams

def run_lif_trace(v, I, params: NeuronParams):
    """Simulate a single LIF trace for given input current and starting membrane potential."""
    n_steps = int(params.run_time / params.time_step)
    time_points = np.arange(0, params.run_time + params.time_step, params.time_step)

    voltages = [v]
    spike_counter = 0

    for _ in time_points[1:]:
        slope = (-(v - params.v_rest) / params.tau) + I
        v += slope * params.time_step

        if v < params.v_reset:
            v = params.v_reset
            spike_counter = 0
        elif v >= params.v_thresh:
            if spike_counter == 3:
                v = params.v_reset
                spike_counter = 0
            spike_counter += 1
            if spike_counter == 2:
                v = params.v_spike
                spike_counter += 1

        voltages.append(v)

    return time_points, voltages


def run_lif_rate(v, params: NeuronParams, max_current=2.5, step=0.002):
    """Loops over a range of input currents and computes the firing rate for each."""
    n_steps = int(params.run_time / params.time_step)
    input_currents, spike_rates = [], []

    for input_current in np.arange(step, max_current, step):
        spikes = 0
        v_trial = v
        spike_counter = 0

        for _ in range(n_steps):
            slope = (-(v_trial - params.v_rest) / params.tau) + input_current
            v_trial += slope * params.time_step

            if v_trial < params.v_reset:
                v_trial = params.v_reset
                spike_counter = 0
            elif v_trial >= params.v_thresh:
                if spike_counter == 3:
                    v_trial = params.v_reset
                    spike_counter = 0
                spike_counter += 1
                if spike_counter == 2:
                    v_trial = params.v_spike
                    spike_counter += 1
                    spikes += 1

        spike_rate = (spikes / params.run_time) * 1000  # Hz
        input_currents.append(input_current)
        spike_rates.append(spike_rate)

    return input_currents, spike_rates


def plot_results(time_points, voltages, params, currents, rates):
    """Plots membrane potential trace and firing rate curve in one window side by side."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Membrane potential trace
    ax1.plot(time_points, voltages, label="Membrane Potential")
    ax1.hlines(params.v_thresh, 0, time_points[-1], colors="b", linestyles="--", label="V Thresh")
    ax1.hlines(params.v_reset, 0, time_points[-1], colors="purple", linestyles="--", label="V Reset")
    ax1.hlines(params.v_rest, 0, time_points[-1], colors="red", linestyles="--", label="V Rest")
    ax1.hlines(params.v_spike, 0, time_points[-1], colors="green", linestyles="--", label="V Spike")

    ax1.set_xlim(0, time_points[-1])
    ax1.set_ylim(params.v_reset - 5, params.v_spike + 5)
    ax1.set_xlabel("Time (ms)")
    ax1.set_ylabel("Membrane Potential (mV)")
    ax1.legend(loc="upper right")
    ax1.set_title("Membrane Potential vs Time")

    # Firing rate vs current
    ax2.plot(currents, rates)
    ax2.set_xlabel("Input Current (V/sec)")
    ax2.set_ylabel("Firing Rate (Spikes/sec)")
    ax2.set_title("Firing Rate vs Input Current")

    plt.tight_layout()
    plt.show()


def main():
    # Neuron parameters
    params = NeuronParams(run_time=200)  # adjust runtime if desired

    # User input
    v0 = float(input("Enter an initial membrane potential (mV): "))
    I = float(input("Enter the input current: "))

    # Single trace
    time_points, voltages = run_lif_trace(v0, I, params)

    # F-I curve
    fi_params = NeuronParams(run_time=1200)  # longer runtime for rate estimation
    currents, rates = run_lif_rate(v0, fi_params)

    # Plots
    plot_results(time_points, voltages, params, currents, rates)


if __name__ == "__main__":
    main()
