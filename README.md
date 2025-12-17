# LIF Model

This is a project for a computational neuroscience course to simulate a leaky integrate-and-fire neuron in python using basic Euler approximation. It generates plots of membrane potential traces under different input noise conditions, Inter-spike interval (ISI) histograms with coefficient of variation (CV), and Spike rate vs input noise level. The model can be used to explore stochastic firing properties of neurons and to visualize how input variability affects neural coding.

## Example Outputs:
Starting membrane potential = -55mV  
Starting input current = 2 V/s
<img width="1200" height="500" alt="lif_eg" src="https://github.com/user-attachments/assets/12a50bc0-37e5-4c43-985e-65396122cf17" />

## Background
The **Leaky Integrate-and-Fire model** is a simplified neuron model which has low computational requirements and relatively low biological accuracy compared to a model like the Hodgkin–Huxley model or the more recent Izhikevich model.


The membrane voltage follows a leaky integration dynamic. When the voltage crosses threshold, the neuron spikes, and after spiking, the voltage resets, which simulates a refractory period.    

## References
-   Dayan & Abbott, _Theoretical Neuroscience_ (2001)
    
-   Gerstner & Kistler, _Spiking Neuron Models_ (2002)
