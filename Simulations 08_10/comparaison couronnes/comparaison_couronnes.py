#!/usr/bin/env python
# coding: utf-8

# * importing packages

# In[1]:


from numpy import linspace, pi
from matplotlib.pyplot import show, figure
from matplotlib import rcParams
from magpylib.source.magnet import Cylinder
from magpylib import Collection, displaySystem

from magforce import plot_1D_along_x, plot_1D_along_y, plot_1D_along_z
from magforce import plot_2D_plane_x, plot_2D_plane_y, plot_2D_plane_z
from magforce import plot_3D
from magforce import getF


# * setting up figure size for notebook

# In[2]:


# make figures bigger on notebook
width = 9
height = 9
rcParams['figure.figsize'] = [width, height]


# * defining a cobalt spherical sample, with 4mm diameter, Ms of 1.4e6 A/m and demagnetizing factor of 1/3
# 
# * the sample variable needs to be a dictionary for magforce's functions to work, and it must include the 'demagnetizing_factor', 'volume' and 'M_saturation' keys

# In[3]:


demagnetizing_factor = 1/3             # sphere
volume = 4 / 3 * pi * (4 / 1000) ** 3  # V sphere r=4mm [m3]
M_saturation = 1.400e6                 # Ms Co room temperature [A/m]

sample = {'demagnetizing_factor': demagnetizing_factor, 
          'volume': volume, 
          'M_saturation': M_saturation}


# * defining diferent magnets

# * couronne_10_15_30
#     * mag 1300mT
#     * 10mm diametre interne
#     * 15mm diametre externe
#     * 30mm hauteur
#     * suface du bas a z=0

# In[4]:


couronne_10_15_30_out = Cylinder(mag=[0, 0, 1300], 
                                 dim=[15, 30], 
                                 pos=[0, 0, 15])

couronne_10_15_30_in = Cylinder(mag=[0, 0, -1300], 
                                dim=[10, 30], 
                                pos=[0, 0, 15])

couronne_10_15_30 = Collection(couronne_10_15_30_out, couronne_10_15_30_in)


# * couronne_10_20_50
#     * mag 1300mT
#     * 10mm diametre interne
#     * 20mm diametre externe
#     * 50mm hauteur
#     * suface du bas a z=0

# In[5]:


couronne_10_20_50_out = Cylinder(mag=[0, 0, 1300], 
                                 dim=[20, 50], 
                                 pos=[0, 0, 25])

couronne_10_20_50_in = Cylinder(mag=[0, 0, -1300], 
                                dim=[10, 50], 
                                pos=[0, 0, 25])

couronne_10_20_50 = Collection(couronne_10_20_50_out, couronne_10_20_50_in)


# * comparaison les 2 couronnes dans l'axe

# In[6]:


# plot for couronne_10_15_30
plot_1D_along_z(x = 0, 
                y = 0, 
                zs = linspace(-30 , 0, 1000), 
                collection = couronne_10_15_30, 
                sample = sample, 
                BF = 'F', 
                saveCSV = False)


# In[7]:


# plot for couronne_10_20_50
plot_1D_along_z(x = 0, 
                y = 0, 
                zs = linspace(-30 , 0, 1000), 
                collection = couronne_10_20_50, 
                sample = sample, 
                BF = 'F', 
                saveCSV = False)


# In[8]:


# F for couronne_10_15_30 a 20mm de hauteur
f_20_couronne_10_15_30 = getF(point = [0, 0, -20],
                              collection = couronne_10_15_30,
                              sample = sample)

# F for couronne_10_20_50 a 20mm de hauteur
f_20_couronne_10_20_50 = getF(point = [0, 0, -20],
                              collection = couronne_10_20_50,
                              sample = sample)

print(f"F for couronne_10_15_30 a 20mm de hauteur: {f_20_couronne_10_15_30}")
print(f"F for couronne_10_20_50 a 20mm de hauteur: {f_20_couronne_10_20_50}")


# * comparaison les 2 cylindres hors l'axe (2mm en x 2mm en y)

# In[9]:


# plot for couronne_10_15_30
plot_1D_along_z(x = 2, 
                y = 2, 
                zs = linspace(-30 , 0, 1000), 
                collection = couronne_10_15_30, 
                sample = sample, 
                BF = 'F', 
                saveCSV = False)


# In[10]:


# plot for couronne_10_20_50
plot_1D_along_z(x = 2, 
                y = 2, 
                zs = linspace(-30 , 0, 1000), 
                collection = couronne_10_20_50, 
                sample = sample, 
                BF = 'F', 
                saveCSV = False)


# In[11]:


# F for couronne_10_15_30 a 20mm de hauteur
f_20_couronne_10_15_30 = getF(point = [2, 2, -20],
                              collection = couronne_10_15_30,
                              sample = sample)

# F for couronne_10_20_50 a 20mm de hauteur
f_20_couronne_10_20_50 = getF(point = [2, 2, -20],
                              collection = couronne_10_20_50,
                              sample = sample)

print(f"F for couronne_10_15_30 a 20mm de hauteur: {f_20_couronne_10_15_30}")
print(f"F for couronne_10_20_50 a 20mm de hauteur: {f_20_couronne_10_20_50}")


# In[ ]:




