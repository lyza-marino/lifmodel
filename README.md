# LIF Model

This is a project for a computational neuroscience course to simulate a leaky integrate-and-fire neuron in python using basic Euler approximation. It generates plots of membrane potential traces under different input noise conditions, Inter-spike interval (ISI) histograms with coefficient of variation (CV), and Spike rate vs input noise level. The model can be used to explore stochastic firing properties of neurons and to visualize how input variability affects neural coding.

## Example Outputs:
Starting membrane potential = -55mV  
Starting input current = 2 V/s
<img width="1200" height="500" alt="lif_eg" src="https://github.com/user-attachments/assets/12a50bc0-37e5-4c43-985e-65396122cf17" />

#
Standard Deviation = 0.1  
<img width="640" height="480" alt="mv_1" src="https://github.com/user-attachments/assets/9858ecb0-6384-43a4-a710-211db9c6bc8b" />
<img width="640" height="480" alt="isi_cv_1" src="https://github.com/user-attachments/assets/7c853535-adda-4070-8726-d4f96b11c406" />

#
Standard Deviation = 1.0  
<img width="640" height="480" alt="mv_2" src="https://github.com/user-attachments/assets/8d035ceb-06f3-4d8e-a680-a05d3a380898" />
<img width="640" height="480" alt="isi_cv_2" src="https://github.com/user-attachments/assets/2a0e7ba9-41a4-474f-a754-d798ca9e2ce1" />

#
Standard Deviation = 10.0  
<img width="640" height="480" alt="mv_3" src="https://github.com/user-attachments/assets/bfdcd12f-dcd3-42d9-a940-24694ad62604" />
<img width="640" height="480" alt="isi_cv_3" src="https://github.com/user-attachments/assets/7210f3d8-8c70-4cf4-8cce-03747834a0d3" />

#
<img width="640" height="480" alt="mv_isi_1" src="https://github.com/user-attachments/assets/b510f0c1-0ee4-4e9d-846a-ebb43bfa2e59" />

## Background
The **Leaky Integrate-and-Fire model** is a simplified neuron model which has low computational requirements and relatively low biological accuracy compared to a model like the Hodgkin–Huxley model or the more recent Izhikevich model.


The membrane voltage follows a leaky integration dynamic. When the voltage crosses threshold, the neuron spikes, and after spiking, the voltage resets, which simulates a refractory period.    

## References
-   Dayan & Abbott, _Theoretical Neuroscience_ (2001)
    
-   Gerstner & Kistler, _Spiking Neuron Models_ (2002)
