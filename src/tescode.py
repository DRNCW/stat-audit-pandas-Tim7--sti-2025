
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


#SEL 5 Misahin 2 periode : rilis pandas 2.0
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




#SEL 7 - VISUALISASI
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

#Plot 1 - Time series
ax1 = axes[0]
pre_dates = df[df['period'] == 'pre_v2']['timestamp']
post_dates = df[df['period'] == 'post_v2']['timestamp']

ax1.plot(pre_dates, pre.values, color='steelblue', marker='o', markersize=4, label='Pre v2.0')
ax1.plot(post_dates, post.values, color='tomato', marker='o', markersize=4, label='Post v2.0')
ax1.axvline(pd.Timestamp('2023-04-01'), color='black', linestyle='--', linewidth=1.5, label='Rilis Pandas 2.0')
ax1.axhline(pre.mean(), color='steelblue', linestyle=':', alpha=0.7)
ax1.axhline(post.mean(), color='tomato', linestyle=':', alpha=0.7)
ax1.set_title('Bug Reports per Bulan (Jan 2021 - Dec 2025)', fontsize=13)
ax1.set_xlabel('Bulan')
ax1.set_ylabel('Jumlah Bug')
ax1.legend()
ax1.grid(alpha=0.3)


#Plot 2 - Boxplot
ax2= axes[1]
bp = ax2.boxplot([pre.values, post.values],
                 patch_artist=True,
                 labels=['Pre v2.0', 'Post v2.0'],
                 widths=0.5)
bp['boxes'][0].set_facecolor('steelblue')
bp['boxes'][1].set_facecolor('tomato')
ax2.set_title('Distribusi Bug Per Bulan', fontsize=13)
ax2.grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('../data/clean/hypothesis_plot.png', dpi=150, bbox_inches='tight')
plt.show()
print("Plot tersimpan di data/clean/hypothesis_plot.png")



