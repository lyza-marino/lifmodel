"""
Leaky Integrate-and-Fire (LIF) neuron model with Euler method.
Simulates spiking activity, plots ISI histograms, membrane potential traces,
and coefficient of variation (CV) vs spike rate across input noise levels.
By Lyza Marino (fixed CV).
"""

import matplotlib.pyplot as plt
import numpy as np


#LIF model simulation with no bells or whistles
def run_lif(std_list, run_time=5000, time_step=0.1,
            v_rest=-65, v_reset=-70, v_thresh=-50, v_spike=40,
            tau=20, input_current=1.3, v_init=-55):
    n_steps = int(run_time / time_step)
    spike_times = [[] for _ in std_list]
    x_list = [[0] for _ in std_list]
    y_list = [[v_init] for _ in std_list]

    for n, sigma in enumerate(std_list):
        v = v_init
        for i in range(1, n_steps + 1):
            # Euler update with noisy input
            slope = ((-1 / tau) * (v - v_rest)) + np.random.normal(input_current, sigma)
            v += slope * time_step

            # Spike condition
            if v >= v_thresh:
                spike_times[n].append(time_step * i)
                v = v_reset

            x_list[n].append(time_step * i)
            y_list[n].append(v)

    return x_list, y_list, spike_times


#Sweep over noise levels (With bells and whistles)
def run_lif_many_std(std_range=np.arange(0, 100, 0.5)):
    run_time = 5000
    time_step = 0.1
    n_steps = int(run_time / time_step)

    spike_times = [[] for _ in std_range]
    spike_rate = np.zeros(len(std_range))
    cv_list = np.zeros(len(std_range))

    for n, sigma in enumerate(std_range):
        v = -55
        for i in range(1, n_steps + 1):
            slope = ((-1 / 20) * (v + 65)) + np.random.normal(1.3, sigma)  # v_rest = -65
            v += slope * time_step

            if v >= -50:
                spike_times[n].append(time_step * i)
                v = -70

        # Spike statistics
        isi = np.diff(spike_times[n])
        spike_rate[n] = (len(spike_times[n]) / run_time) * 1000 if len(spike_times[n]) > 0 else 0
        cv_list[n] = np.std(isi) / np.mean(isi) if len(isi) > 1 else 0

    return spike_rate, std_range, cv_list


# Analysis helpers
def compute_isi(spike_times):
    return [np.diff(times) for times in spike_times]


def compute_cv(isi_list):
    return [np.std(isi) / np.mean(isi) if len(isi) > 1 else 0 for isi in isi_list]


#Plot figures
def plot_isi(isi_list, std_list, cv):
    for i, isi in enumerate(isi_list):
        if len(isi) > 0:
            plt.hist(isi, bins=20, edgecolor='black')
            plt.xlabel("ISI Duration (ms)")
            plt.ylabel("Count")
            plt.title(f'ISI Histogram, σ={std_list[i]}, CV={cv[i]:.2f}')
            plt.show()


def plot_membrane_potential(x_list, y_list, std_list):
    for i, sigma in enumerate(std_list):
        plt.plot(x_list[i][:1000], y_list[i][:1000], ls='-')
        plt.xlabel("Time (ms)")
        plt.ylabel("Membrane Potential (mV)")
        plt.title(f'LIF Membrane Potential, σ={sigma}')
        plt.show()


def plot_cv_spike_rate(cv, spike_rate, std_list):
    fig, ax1 = plt.subplots()

    ax1.plot(std_list, spike_rate, color='blue', label='Spike Rate')
    ax1.set_xlabel("Input Noise σI")
    ax1.set_ylabel("Spike Rate (Hz)", color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    ax2 = ax1.twinx()
    ax2.plot(std_list, cv, color='orange', label='CV')
    ax2.set_ylabel("Coefficient of Variation", color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')

    plt.title("Spike Rate and CV vs Noise Level")
    plt.show()


def main():
    std_list = [0.1, 1.0, 10.0]

    # Single-run LIF
    x_list, y_list, spike_times = run_lif(std_list)
    isi_list = compute_isi(spike_times)
    cv = compute_cv(isi_list)

    # Sweep over many std values
    spike_rate, std_range, cv_range = run_lif_many_std()

    # Plot results
    plot_isi(isi_list, std_list, cv)
    plot_membrane_potential(x_list, y_list, std_list)
    plot_cv_spike_rate(cv_range, spike_rate, std_range)


if __name__ == "__main__":
    main()
