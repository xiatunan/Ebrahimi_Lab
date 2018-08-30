# -*- coding: UTF-8 -*-

import numpy as np
import matplotlib.pyplot as plt

gf_Cu=np.loadtxt('GF1_1_Cu tape-Z-Theta.txt')
gf_Cu_freq_raw=gf_Cu[:,0]
gf_Cu_res_raw=gf_Cu[:,1]
gf_Cu_pha_raw=gf_Cu[:,2]
gf_Cu_freq=[]
gf_Cu_res=[]
gf_Cu_pha=[]
for i in range(len(gf_Cu_freq_raw)):
    if -90.<gf_Cu_pha_raw[i]<90.:
        if gf_Cu_res_raw[i]<2.*10**6:
            gf_Cu_freq.append(np.log10(gf_Cu_freq_raw[i]))
            gf_Cu_res.append(np.log10(gf_Cu_res_raw[i]))
            gf_Cu_pha.append(gf_Cu_pha_raw[i])
        else:
            continue
    else:
        continue
plt.figure()
plt.plot(gf_Cu_freq,gf_Cu_res,'o',color='blue')
plt.plot(gf_Cu_freq,gf_Cu_res,'-',color='red')
plt.xlabel('$log_{10}f$')
plt.ylabel('$log_{10}|Z|$')
plt.title('Amplitude of fiber with copper')
plt.savefig('./GF1_1_Cu_R.jpeg')
plt.figure()
plt.plot(gf_Cu_freq,gf_Cu_pha,'o',color='blue')
plt.plot(gf_Cu_freq,gf_Cu_pha,'-',color='red')
plt.xlabel('$log_{10}f$')
plt.ylabel(r'$\theta / ^{\circ}$')
plt.title('Phase of fiber with copper')
plt.savefig('./GF1_1_Cu_Th.jpeg')

gf_1_1=np.loadtxt('GF1_1.txt-Z-Theta.txt')
gf_1_1_freq_raw=gf_1_1[:,0]
gf_1_1_res_raw=gf_1_1[:,1]
gf_1_1_pha_raw=gf_1_1[:,2]
gf_1_2=np.loadtxt('GF1_2.txt-Z-Theta.txt')
gf_1_2_freq_raw=gf_1_2[:,0]
gf_1_2_res_raw=gf_1_2[:,1]
gf_1_2_pha_raw=gf_1_2[:,2]
gf_1_3=np.loadtxt('GF1_3.txt-Z-Theta.txt')
gf_1_3_freq_raw=gf_1_3[:,0]
gf_1_3_res_raw=gf_1_3[:,1]
gf_1_3_pha_raw=gf_1_3[:,2]
gf_1_freq=[]
gf_1_res_mean=[]
gf_1_res_err=[]
gf_1_pha_mean=[]
gf_1_pha_err=[]
for i in range(len(gf_1_1_freq_raw)):
    list_pha=[]
    list_res=[]
    if -90.<gf_1_1_pha_raw[i]<90.:
        list_pha.append(gf_1_1_pha_raw[i])
    if -90.<gf_1_2_pha_raw[i]<90.:
        list_pha.append(gf_1_2_pha_raw[i])
    if -90.<gf_1_3_pha_raw[i]<90.:
        list_pha.append(gf_1_3_pha_raw[i])
    if gf_1_1_res_raw[i]<2.*10**6:
        gf_1_1_res_raw[i]=np.log10(gf_1_1_res_raw[i])
        list_res.append(gf_1_1_res_raw[i])
    if gf_1_2_res_raw[i]<2.*10**6:
        gf_1_2_res_raw[i] = np.log10(gf_1_2_res_raw[i])
        list_res.append(gf_1_2_res_raw[i])
    if gf_1_3_res_raw[i]<2.*10**6:
        gf_1_3_res_raw[i] = np.log10(gf_1_3_res_raw[i])
        list_res.append(gf_1_3_res_raw[i])
    else:
        continue
    gf_1_freq.append(np.log10(gf_1_1_freq_raw[i]))
    res=np.mean(list_res)
    res_err=np.std(list_res)/np.sqrt(float(len(list_res)))
    pha = np.mean(list_pha)
    pha_err = np.std(list_pha) / np.sqrt(float(len(list_pha)))
    gf_1_res_mean.append(res)
    gf_1_res_err.append(res_err)
    gf_1_pha_mean.append(pha)
    gf_1_pha_err.append(pha_err)
plt.figure()
plt.plot(gf_1_freq,gf_1_res_mean,'-',color='red')
plt.errorbar(gf_1_freq,gf_1_res_mean,yerr=gf_1_res_err,fmt='o',color='blue',ecolor='green')
plt.xlabel('$log_{10}f$')
plt.ylabel('$log_{10}|Z|$')
plt.title('Amplitude of fiber 1')
plt.savefig('./GF_1_R.jpeg')
plt.figure()
plt.plot(gf_1_freq,gf_1_pha_mean,'-',color='red')
plt.errorbar(gf_1_freq,gf_1_pha_mean,yerr=gf_1_pha_err,fmt='o',color='blue',ecolor='green')
plt.xlabel('$log_{10}|Z|$')
plt.ylabel(r'$\theta / ^{\circ}$')
plt.title('Phase of fiber 1')
plt.savefig('./GF_1_Th.jpeg')

gf_2_1=np.loadtxt('GF2_1.txt-Z-Theta.txt')
gf_2_1_freq_raw=gf_2_1[:,0]
gf_2_1_res_raw=gf_2_1[:,1]
gf_2_1_pha_raw=gf_2_1[:,2]
gf_2_2=np.loadtxt('GF2_2.txt-Z-Theta.txt')
gf_2_2_freq_raw=gf_2_2[:,0]
gf_2_2_res_raw=gf_2_2[:,1]
gf_2_2_pha_raw=gf_2_2[:,2]
gf_2_3=np.loadtxt('GF2_3.txt-Z-Theta.txt')
gf_2_3_freq_raw=gf_2_3[:,0]
gf_2_3_res_raw=gf_2_3[:,1]
gf_2_3_pha_raw=gf_2_3[:,2]
gf_2_freq=[]
gf_2_res_mean=[]
gf_2_res_err=[]
gf_2_pha_mean=[]
gf_2_pha_err=[]
for i in range(len(gf_2_1_freq_raw)):
    list_pha=[]
    list_res=[]
    if -90.<gf_2_1_pha_raw[i]<90.:
        list_pha.append(gf_2_1_pha_raw[i])
    if -90.<gf_2_2_pha_raw[i]<90.:
        list_pha.append(gf_2_2_pha_raw[i])
    if -90.<gf_2_3_pha_raw[i]<90.:
        list_pha.append(gf_2_3_pha_raw[i])
    if gf_2_1_res_raw[i]<2.*10**6:
        gf_2_1_res_raw[i]=np.log10(gf_2_1_res_raw[i])
        list_res.append(gf_2_1_res_raw[i])
    if gf_2_2_res_raw[i]<2.*10**6:
        gf_2_2_res_raw[i] = np.log10(gf_2_2_res_raw[i])
        list_res.append(gf_2_2_res_raw[i])
    if gf_2_3_res_raw[i]<2.*10**6:
        gf_2_3_res_raw[i] = np.log10(gf_2_3_res_raw[i])
        list_res.append(gf_2_3_res_raw[i])
    else:
        continue
    gf_2_freq.append(np.log10(gf_2_1_freq_raw[i]))
    res=np.mean(list_res)
    res_err=np.std(list_res)/np.sqrt(float(len(list_res)))
    pha = np.mean(list_pha)
    pha_err = np.std(list_pha) / np.sqrt(float(len(list_pha)))
    gf_2_res_mean.append(res)
    gf_2_res_err.append(res_err)
    gf_2_pha_mean.append(pha)
    gf_2_pha_err.append(pha_err)
plt.figure()
plt.plot(gf_2_freq,gf_2_res_mean,'-',color='red')
plt.errorbar(gf_2_freq,gf_2_res_mean,yerr=gf_2_res_err,fmt='o',color='blue',ecolor='green')
plt.xlabel('$log_{10}f$')
plt.ylabel('$log_{10}|Z|$')
plt.title('Amplitude of fiber 2')
plt.savefig('./GF_2_R.jpeg')
plt.figure()
plt.plot(gf_2_freq,gf_2_pha_mean,'-',color='red')
plt.errorbar(gf_2_freq,gf_2_pha_mean,yerr=gf_2_pha_err,fmt='o',color='blue',ecolor='green')
plt.xlabel('$log_{10}f$')
plt.ylabel(r'$\theta / ^{\circ}$')
plt.title('Phase of fiber 2')
plt.savefig('./GF_2_Th.jpeg')

gf_3_1=np.loadtxt('GF3_1.txt-Z-Theta.txt')
gf_3_1_freq_raw=gf_3_1[:,0]
gf_3_1_res_raw=gf_3_1[:,1]
gf_3_1_pha_raw=gf_3_1[:,2]
gf_3_2=np.loadtxt('GF3_2.txt-Z-Theta.txt')
gf_3_2_freq_raw=gf_3_2[:,0]
gf_3_2_res_raw=gf_3_2[:,1]
gf_3_2_pha_raw=gf_3_2[:,2]
gf_3_3=np.loadtxt('GF3_3.txt-Z-Theta.txt')
gf_3_3_freq_raw=gf_3_3[:,0]
gf_3_3_res_raw=gf_3_3[:,1]
gf_3_3_pha_raw=gf_3_3[:,2]
gf_3_freq=[]
gf_3_res_mean=[]
gf_3_res_err=[]
gf_3_pha_mean=[]
gf_3_pha_err=[]
for i in range(len(gf_3_1_freq_raw)):
    list_pha=[]
    list_res=[]
    if -90.<gf_3_1_pha_raw[i]<90.:
        list_pha.append(gf_3_1_pha_raw[i])
    if -90.<gf_3_2_pha_raw[i]<90.:
        list_pha.append(gf_3_2_pha_raw[i])
    if -90.<gf_3_3_pha_raw[i]<90.:
        list_pha.append(gf_3_3_pha_raw[i])
    if gf_3_1_res_raw[i]<2.*10**6:
        gf_3_1_res_raw[i]=np.log10(gf_3_1_res_raw[i])
        list_res.append(gf_3_1_res_raw[i])
    if gf_3_2_res_raw[i]<2.*10**6:
        gf_3_2_res_raw[i] = np.log10(gf_3_2_res_raw[i])
        list_res.append(gf_3_2_res_raw[i])
    if gf_3_3_res_raw[i]<2.*10**6:
        gf_3_3_res_raw[i] = np.log10(gf_3_3_res_raw[i])
        list_res.append(gf_3_3_res_raw[i])
    else:
        continue
    gf_3_freq.append(np.log10(gf_3_1_freq_raw[i]))
    res=np.mean(list_res)
    res_err=np.std(list_res)/np.sqrt(float(len(list_res)))
    pha = np.mean(list_pha)
    pha_err = np.std(list_pha) / np.sqrt(float(len(list_pha)))
    gf_3_res_mean.append(res)
    gf_3_res_err.append(res_err)
    gf_3_pha_mean.append(pha)
    gf_3_pha_err.append(pha_err)
plt.figure()
plt.plot(gf_3_freq,gf_3_res_mean,'-',color='red')
plt.errorbar(gf_3_freq,gf_3_res_mean,yerr=gf_3_res_err,fmt='o',color='blue',ecolor='green')
plt.xlabel('$log_{10}f$')
plt.ylabel('$log_{10}|Z|$')
plt.title('Amplitude of fiber 3')
plt.savefig('./GF_3_R.jpeg')
plt.figure()
plt.plot(gf_3_freq,gf_3_pha_mean,'-',color='red')
plt.errorbar(gf_3_freq,gf_3_pha_mean,yerr=gf_3_pha_err,fmt='o',color='blue',ecolor='green')
plt.xlabel('$log_{10}f$')
plt.ylabel(r'$\theta / ^{\circ}$')
plt.title('Phase of fiber 3')
plt.savefig('./GF_3_Th.jpeg')

gf_4_1=np.loadtxt('GF4_1.txt-Z-Theta.txt')
gf_4_1_freq_raw=gf_4_1[:,0]
gf_4_1_res_raw=gf_4_1[:,1]
gf_4_1_pha_raw=gf_4_1[:,2]
gf_4_2=np.loadtxt('GF4_2.txt-Z-Theta.txt')
gf_4_2_freq_raw=gf_4_2[:,0]
gf_4_2_res_raw=gf_4_2[:,1]
gf_4_2_pha_raw=gf_4_2[:,2]
gf_4_3=np.loadtxt('GF4_3.txt-Z-Theta.txt')
gf_4_3_freq_raw=gf_4_3[:,0]
gf_4_3_res_raw=gf_4_3[:,1]
gf_4_3_pha_raw=gf_4_3[:,2]
gf_4_freq=[]
gf_4_res_mean=[]
gf_4_res_err=[]
gf_4_pha_mean=[]
gf_4_pha_err=[]
for i in range(len(gf_4_1_freq_raw)):
    list_pha=[]
    list_res=[]
    if -90.<gf_4_1_pha_raw[i]<90.:
        list_pha.append(gf_4_1_pha_raw[i])
    if -90.<gf_4_2_pha_raw[i]<90.:
        list_pha.append(gf_4_2_pha_raw[i])
    if -90.<gf_4_3_pha_raw[i]<90.:
        list_pha.append(gf_4_3_pha_raw[i])
    if gf_4_1_res_raw[i]<2.*10**6:
        gf_4_1_res_raw[i]=np.log10(gf_4_1_res_raw[i])
        list_res.append(gf_4_1_res_raw[i])
    if gf_4_2_res_raw[i]<2.*10**6:
        gf_4_2_res_raw[i] = np.log10(gf_4_2_res_raw[i])
        list_res.append(gf_4_2_res_raw[i])
    if gf_4_3_res_raw[i]<2.*10**6:
        gf_4_3_res_raw[i] = np.log10(gf_4_3_res_raw[i])
        list_res.append(gf_4_3_res_raw[i])
    else:
        continue
    gf_4_freq.append(np.log10(gf_4_1_freq_raw[i]))
    res=np.mean(list_res)
    res_err=np.std(list_res)/np.sqrt(float(len(list_res)))
    pha = np.mean(list_pha)
    pha_err = np.std(list_pha) / np.sqrt(float(len(list_pha)))
    gf_4_res_mean.append(res)
    gf_4_res_err.append(res_err)
    gf_4_pha_mean.append(pha)
    gf_4_pha_err.append(pha_err)
plt.figure()
plt.plot(gf_4_freq,gf_4_res_mean,'-',color='red')
plt.errorbar(gf_4_freq,gf_4_res_mean,yerr=gf_4_res_err,fmt='o',color='blue',ecolor='green')
plt.xlabel('$log_{10}f$')
plt.ylabel('$log_{10}|Z|$')
plt.title('Amplitude of fiber 4')
plt.savefig('./GF_4_R.jpeg')
plt.figure()
plt.plot(gf_4_freq,gf_4_pha_mean,'-',color='red')
plt.errorbar(gf_4_freq,gf_4_pha_mean,yerr=gf_4_pha_err,fmt='o',color='blue',ecolor='green')
plt.xlabel('$log_{10}f$')
plt.ylabel(r'$\theta / ^{\circ}$')
plt.title('Phase of fiber 4')
plt.savefig('./GF_4_Th.jpeg')

plt.figure()
l1,=plt.plot(gf_1_freq,gf_1_res_mean,'-o',color='black',linewidth=2.0)
l2,=plt.plot(gf_2_freq,gf_2_res_mean,'-o',color='blue',linewidth=2.0)
l3,=plt.plot(gf_3_freq,gf_3_res_mean,'-o',color='magenta',linewidth=2.0)
l4,=plt.plot(gf_4_freq,gf_4_res_mean,'-o',color='red',linewidth=2.0)
plt.xlabel('$log_{10}f$')
plt.ylabel('$log_{10}|Z|$')
plt.legend(handles=[l1,l2,l3,l4,],labels=['GO Fiber 1','GO Fiber 2','GO Fiber 3','GO Fiber 4'],loc='best')
plt.title('Amplitude of impedance of 4 fibers')
plt.savefig('./GF_all_R.jpeg')

plt.figure()
l5,=plt.plot(gf_1_freq,gf_1_pha_mean,'-o',color='black',linewidth=2.0)
l6,=plt.plot(gf_2_freq,gf_2_pha_mean,'-o',color='blue',linewidth=2.0)
l7,=plt.plot(gf_3_freq,gf_3_pha_mean,'-o',color='magenta',linewidth=2.0)
l8,=plt.plot(gf_4_freq,gf_4_pha_mean,'-o',color='red',linewidth=2.0)
plt.xlabel('$log_{10}f$')
plt.ylabel(r'$\theta / ^{\circ}$')
plt.legend(handles=[l5,l6,l7,l8,],labels=['GO Fiber 1','GO Fiber 2','GO Fiber 3','GO Fiber 4'],loc='best')
plt.title('Phase of impedance of 4 fibers')
plt.savefig('./GF_all_Th.jpeg')