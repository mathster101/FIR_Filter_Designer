# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 21:33:53 2021

@author: mpanicker
"""

import numpy as np
import scipy.signal as ss



def dummy_signal(f_sample,num_sample):
	# a mix of 4Hz and 100Hz signals
	t = np.arange(num_sample)/f_sample
	signal = np.sin(2 * 3.1415 * 4 * t) + 0.1 * np.cos(2 * 3.1415 * 100 * t)
	return signal


def design_filter(cutoff_frequency, f_sample, filter_length, window_function):
	f_nyquist = f_sample /2
	if filter_length%2 == 0:
		filter_length += 1
	if window_function != 'kaiser':
		filter_coefficients = ss.firwin(filter_length, cutoff_frequency / f_nyquist, window = window_function)
	return filter_coefficients



def kaiser_filter(cutoff_frequency, stop_band_atten, f_sample):
	f_nyquist = f_sample / 2
	transition_width = 5 /f_nyquist
	N, beta = ss.kaiserord(stop_band_atten, transition_width)
	filter_coefficients = ss.firwin(N, cutoff_frequency/f_nyquist, window=('kaiser', beta))
	return filter_coefficients

def filter_signal(input_signal, filter_coefficients):
	return ss.lfilter(filter_coefficients, 1, input_signal)

fs = 1000
sig = dummy_signal(fs,2000)


#taps = kaiser_filter(10, 40, fs, sig)
taps = design_filter(10,fs,30,'hamming')
filtered = filter_signal(sig, taps)