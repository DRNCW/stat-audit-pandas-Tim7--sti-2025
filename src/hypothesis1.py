
import os 

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'data', 'clean', 'monthly_bugs.csv')

print("  ")


#SEL 4 Code for Load Data
df = pd.read_csv(file_path)  
df['timestamp'] = pd.to_datetime(df['timestamp'])   
print(df.shape)   #(baris,kolom)
df.head()

print("  ")


#SEL 5 Misahin 2 periode : rilis pandas 2.0  -  SPLIT DATA
cut = pd.Timestamp('2023-04-01')

pre = df[df['timestamp'] < cut].copy()
post = df[df['timestamp'] >= cut].copy()

print(f"Data sebelum April 2023: {len(pre)} baris")
print(f"Data sesudah April 2023: {len(post)} baris")

print("  ")


# SEL 6 : Hitung rata-rata bug per bulan
pre_mean = pre['bug_count'].mean()
post_mean = post['bug_count'].mean()

print(f"Rata-rata bug per bulan before: {pre_mean:.2f}")
print(f"Rata-rata bug per bulan after: {post_mean:.2f}")


# SEL 7 - VISUALISASI
# fig, axes = plt.subplots(1, 2, figsize=(14, 5))

#Plot 1 - Time series
# ax1 = axes[0]
# pre_dates = df[df['period'] == 'pre_v2']['timestamp']
# post_dates = df[df['period'] == 'post_v2']['timestamp']
# 
