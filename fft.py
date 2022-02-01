#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from threading import Thread



class Display_fft:
    def __init__(self, data_array, signal_time, sampling_interval, start=False) -> None:

        self.dataset= data_array # []

        self.signal_total_time= signal_time  # TOTAL duration of signal
        self.sample_time=sampling_interval   # sampling time of signal
        self.thread= Thread(target=self.show) 
        if start:
            self.thread.start()
        

    def show(self) -> None:
        no_vals=len(self.dataset)
        print("Len of dataset ", no_vals)

        #time  = np.arange(0, self.signal_total_time, self.sample_time)  # Time points
      
        ## fourier transform
        f = np.fft.fft(self.dataset)/len(self.dataset)
        fourierTransform = f[ range ( int(len(self.dataset)/2  ))] # Exclude sampling frequency

        values= np.arange(int(len(fourierTransform)))  
        frequencies= values/self.signal_total_time
        
        plt.xlabel('frequency (HZ)')
        plt.ylabel('Amplitude')
        plt.grid(False)  # grid lines
        #plt.legend(loc='best') # legend box
                
        plt.plot(frequencies, abs(fourierTransform))
        plt.show()
        
        

if __name__=='__main__':

    samplingFrequency   = 2000  # sampling frequency must be atleast greater than twice of signal frequency bandwidth
    samplingInterval       = 1 / samplingFrequency

    # total duration of the signal
    signalTime             = 1000; 

    # Frequency of the signals
    signal1Frequency     = 8
    signal2Frequency     = 800
    signal3Frequency     = 50
    signal4Frequency     = 90

    # Time points
    time        = np.arange(0, signalTime, samplingInterval)

    # Create 4 sine waves
    amplitude1 = np.sin(2*np.pi*signal1Frequency*time)
    amplitude2 = np.sin(2*np.pi*signal2Frequency*time)
    amplitude3 = np.sin(2*np.pi*signal3Frequency*time)
    amplitude4 = np.sin(2*np.pi*signal4Frequency*time)/10

    # Add the sine waves to create mixed signal
    Mixed_amplitude = amplitude1 + amplitude2  + amplitude3 + amplitude4

    j=Display_fft(Mixed_amplitude, signalTime,samplingInterval)
    j.show()
    

    


