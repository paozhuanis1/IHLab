%% Cleaning Part
clc;
clear all;
close all;

%% Loading Audio/Creating needed vector

[st, Fs] = audioread('lsb_secret.wav');
st=st(:,1);

L = max(size(st));
t = (1:L)'/Fs;
f_0 = 25000;
a = 1;
x_m = a*sin(2*pi*f_0*t);
sr=st-x_m;
sr=sr./x_m;
[b,a]=butter(10, 1200/(Fs/2),'low');%听不见就条这个参�?
sr_filtered = filter(b,a,sr);
SR = abs(fft(sr_filtered(:,1)))./L;
f_axis = [0:L-1]*Fs/L;
plot(f_axis(1:L/2), SR(1:L/2),'color','r')
ST = abs(fft(st(:,1)))./L;
%plot(f_axis(1:L/2), ST(1:L/2),'color','b')
%% Save the signal in a flat audioformat 
audiowrite('getsecret.wav', sr_filtered, Fs,'BitsPerSample',32);

