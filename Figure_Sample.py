# Figure Influence of thickness Ts vs Io
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import numpy as np

# preamble='\\usepackage{newtxtext}\n\\usepackage{newtxmath}\n'

preamble='\\usepackage{times}\n\\usepackage{newtxmath}\n\\usepackage{siunitx}\n'
# preamble=preamble+'\\usepackage{amssymb}\n\\usepackage{amsmath}\n'
# preamble=preamble+'\\usepackage{calrsfs}\n\\DeclareMathAlphabet{\pazocal}{OMS}{zplm}{m}{n}\n'

# rc('font',**{'family':'serif','serif':['Times']})
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=preamble)

# plt.rcParams["axes.labelsize"]="large"
# plt.rcParams["font.weight"]="bold"
# plt.rcParams["axes.labelweight"]="bold"
# plt.rcParams["mathtext.fontset"]="stixsans"

A1=np.loadtxt('Mech_Sp_Io_100_Non_illR.dat', delimiter=',',skiprows=0)
figname='Trial_100_Non_illR.pdf'

# plt.rc('text', usetex=True)
r=0.9
fs = 24.0
s_size=10.0
s_space=5
# Say, "the default sans-serif font is COMIC SANS"
matplotlib.rcParams['font.serif'] = "Times New Roman"
# Then, "ALWAYS use sans-serif fonts"
matplotlib.rcParams['font.family'] = "serif"

fig, ax = plt.subplots(figsize=(9.5,6),dpi=50)

# Fig 1
ax.plot(A1[:,0], A1[:,1],'rs-',markersize=s_size,markevery=s_space,linewidth=3.0,label=r'$(1)~1000$')  # Plot some data on the axes.
ax.plot(A1[:,0], A1[:,2],'bo-',markersize=s_size,markevery=s_space,linewidth=3.0,label=r'$(2)~1000(l-x)/l$')  # Plot some data on the axes.
ax.plot(A1[:,0], A1[:,3],'gv-',markersize=s_size,markevery=s_space,linewidth=3.0,label=r'$(3)~1000((l-x)/l)^2$')  # Plot some data on the axes.
ax.plot(A1[:,0], A1[:,4],'m^-',markersize=s_size,markevery=s_space,linewidth=3.0,label=r'$(4)~1000((l-x)/l)^4$')  # Plot some data on the axes.
ax.plot(A1[:,0], A1[:,5],'c*-',markersize=s_size,markevery=s_space,linewidth=3.0,label=r'$(5)~1000e^{(-10x/l)}$')  # Plot some data on the axes.

# ax.plot(A1[:,0], A1[:,6],'bo--',markersize=s_size,markevery=s_space,linewidth=3.0,label=r'$1000 (L-y)/L$')  # Plot some data on the axes.
# ax.plot(A1[:,0], A1[:,7],'gv--',markersize=s_size,markevery=s_space,linewidth=3.0,label=r'$1000 ((L-y)/L)^2$')  # Plot some data on the axes.
# ax.plot(A1[:,0], A1[:,8],'k--',linewidth=3.0)  # Plot some data on the axes.
# ax.plot(A1[:,0], A1[:,9],'y--',linewidth=3.0)



#Choose range
ax.set_xlim(0.0,20.0)
ax.set_ylim(0.0,180.0)
# ax.set_yscale('log')
ax.xaxis.set_ticks(np.arange(0, 21.0, 2.0))

#Choose X and Y Labels
# ax[0].set_title("a",color= 'k', fontsize= fs,loc='left')
ax.set_xlabel(r'$x \: (\SI{}{\milli\meter})$',color= 'k', fontsize= fs)
ax.set_ylabel(r'$\kappa \: (\SI{}{\per\meter})$', color= 'k', fontsize= fs)



#----------------------------------------------------------------------------------------------------------------------------

ax.minorticks_on()

# ax[0].set_xticks(np.arange(0.0, 50.0, step=5))
# ax[0].set_yticks(np.arange(0.0, 1.0, step=0.2))

for tick in ax.get_xticklabels():
    tick.set_fontsize(r*fs)
for tick in ax.get_yticklabels():
    tick.set_fontsize(r*fs)

ax.tick_params(which='major',direction='in', length=10, width=1.5, colors='k')
ax.tick_params(which='minor',direction='in', length=5, width=1.5, colors='k')
ax.tick_params(which='both',top=True, right=True)

legend = ax.legend(bbox_to_anchor=(1.0,0.87), shadow=False, fontsize=r*fs, frameon=False)
legend.get_frame().set_facecolor('w')
fig.text(0.70, 0.83, r'$I_\text{o}(x,y) \: (\SI{}{\watt\per\square\meter})$', {'color': 'k', 'fontsize': fs})

ax.text(12,137,r'(1)',{'color': 'k', 'fontsize': r*fs})
ax.text(8.6,90,r'(2)',{'color': 'k', 'fontsize': r*fs})
ax.text(7.3,68,r'(3)',{'color': 'k', 'fontsize': r*fs})
ax.text(5.5,43,r'(4)',{'color': 'k', 'fontsize': r*fs})
ax.text(3.5,19,r'(5)',{'color': 'k', 'fontsize': r*fs})

fig.subplots_adjust(left=0.001, bottom=0.135, right=0.74, top=0.935)
ratio=1.0
ax.set_aspect(1.0/ax.get_data_ratio()*ratio)
# ax.set_aspect('equal')
plt.savefig(figname,dpi=300);
plt.show();
