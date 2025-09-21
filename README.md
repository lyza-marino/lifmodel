# LIF Model

Hello, this is a project I made to simulate a leaky integrate-and-fire neuron in python using basic Euler approximation. It generates plots of membrane potential traces under different input noise conditions, Inter-spike interval (ISI) histograms with coefficient of variation (CV), and Spike rate vs input noise level. The model can be used to explore stochastic firing properties of neurons and to visualize how input variability affects neural coding.

## Features
-   LIF neuron model implemented with Euler integration
-   Adjustable initial membrane potential and constant input current variables - lifmodel
    
-   Adjustable **noise level (σI)** - lifmodel_calccv.py
    
-   Automatic computation of:
    
    -   Inter-spike intervals (ISI)
        
    -   Coefficient of variation (CV = std(ISI)/mean(ISI))
        
    -   Spike rates
        
## Example Outputs
Membrane potential trace as a function of starting membrane potential and input current.
Spike rate vs. input current

Membrane potential trace with noise level σ
ISI histogram
Spike rate and CV vs input noise
## Background
The **Leaky Integrate-and-Fire model** is a simplified neuron model which has low computational requirements and relatively low biological accuracy compared to a model like the Hodgkin–Huxley model or the more recent Izhikevich model.

-   The membrane voltage follows a leaky integration dynamic
    
-   When the voltage crosses threshold, the neuron spikes
    
-   After spiking, the voltage resets, which simulates a refractory period
    

This project also extends the model with **Gaussian noisy input currents**, enabling exploration of how variability impacts firing statistics
## References
-   Dayan & Abbott, _Theoretical Neuroscience_ (2001)
    
-   Gerstner & Kistler, _Spiking Neuron Models_ (2002)
