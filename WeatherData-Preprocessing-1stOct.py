#!/usr/bin/env python
# coding: utf-8

# In[5]:


"""Predicting Solar Intensity Using Weather Data
June 2019
Alex Kim and Dane Stocks
This module defines common utility functions, especially regarding data
cleaning and structuring.
"""
import numpy as np


def read_data(data_paths):
    """Read the data files and combine them into a single dataset.
    Args:
        data_paths (list): Strings of the paths to the data files.
    Returns:
        A single NumPy array consisting of the data from all datasets
    """
    # Read the first data file
    first_path = data_paths[0]
    full_data = np.genfromtxt(first_path, delimiter=',', skip_header=2,
            names=True)

    # Append all remaining data files
    num_files = len(data_paths)
    for i in range(1, num_files):
        path = data_paths[i]
        new_data = np.genfromtxt(path, delimiter=',', skip_header=2,
                names=True)
        full_data = np.hstack((full_data, new_data))

    return full_data


def trim_vars(data):
    """Trim extraneous variables and observations from the data.
    Args:
        data (ndarray): The full unprocessed dataset
    Returns:
        The full dataset with extraneous variables and observations
        trimmed off.
    """
    # Remove all columns with names in `rm_vars`
    rm_vars = ['Unnamed: 0','DHI', 'DNI', 'Clearsky_DHI', 'Clearsky_DNI',
            'Clearsky_GHI', 'Fill_Flag','Global_Horizontal_UV_Irradiance_280400nm','Global_Horizontal_UV_Irradiance_295385nm', 'f0', 'f1',
       'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12',
       'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20']
    var_names = list(data.dtype.names)
    var_names
    keep_vars = [_ for _ in var_names if _ not in rm_vars]
    #print("keep_vars")
    #print(keep_vars)
    data_trimmed = data[keep_vars]
    return data_trimmed


def generate_ids(data):
    """Generate a unique ID for each row of the data. Each ID encodes
    the date and time of the solar intensity measurement.
    """
    pass


def recode_time(data):
    """Recode the 'Hour' column to encapsulate both the hour and the
    minute, and then remove the 'Minute' column.
    Args:
        data (ndarray): The full unprocessed dataset
    Returns:
        The full dataset with extraneous variables and observations
    """
    # Recode 'Hour'
    data['Hour'] = data['Hour'] + data['Minute'] / 60

    # Remove 'Minute'
    var_names = list(data.dtype.names)
    keep_vars = [_ for _ in var_names if _ != 'Minute']
    
    data_trimmed = data[:, keep_vars]
    return data_trimmed


def featurize(data, n_time_points):
    """
    """
    pass


def cluster_transform():
    """Transform the data for k-means clustering.
    This function generates a transformed dataset where each row
    corresponds to a day, and each column corresponds to a time during
    the day (48 columns total). The cells are populated with solar
    intensity values. All predictor variables (weather data) are ignored
    here.
    Args:
    Returns:
    """


def split_data():
    """
    """
    pass


def read_and_preprocess():
    """
    """
    data_paths = ['/Users/ritu/Downloads/new_weatherdata/pre_allcombined_copy.csv']
    dat = read_data(data_paths)
    dat = trim_vars(dat)
    #print("printing")
    #print(dat)

    return dat


if __name__ == "__main__":
    pass


# In[6]:


import numpy as np
read_and_preprocess()


# In[7]:


#code to save cleaned and processed combine datafile in local system
import pandas as pd 
pd.DataFrame(read_and_preprocess()).to_csv("/Users/ritu/Downloads/new_weatherdata/all_cities_transformed_combined.csv")


# In[ ]:




