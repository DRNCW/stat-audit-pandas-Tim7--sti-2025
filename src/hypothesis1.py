import os 
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, '..', 'data', 'clean', 'monthly_bugs.csv')

# ============================================================
# SEL 4: LOAD DATA CLEAN
# ============================================================
df = pd.read_csv(file_path)  
df['timestamp'] = pd.to_datetime(df['timestamp'])   

# ============================================================
# SEL 5: SPLIT DATA BERDASARKAN RILIS PANDAS 2.0
# ============================================================
cut = pd.Timestamp('2023-04-01')
pre = df[df['timestamp'] < cut].copy()
post = df[df['timestamp'] >= cut].copy()

# ============================================================
# SEL 6: HITUNG RATA-RATA LAJU BUG BULANAN (MLE POISSON)
# ============================================================
pre_mean = pre['bug_count'].mean()
post_mean = post['bug_count'].mean()

# ============================================================
# SEL 7: VISUALISASI TIME-SERIES & BOXPLOT
# ============================================================
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Subplot 1: Time Series
ax1 = axes[0]
ax1.plot(pre['timestamp'], pre['bug_count'].values, color='steelblue', marker='o', markersize=4, label=f'Pre v2.0 (Mean: {pre_mean:.2f})')
ax1.plot(post['timestamp'], post['bug_count'].values, color='tomato', marker='o', markersize=4, label=f'Post v2.0 (Mean: {post_mean:.2f})')
ax1.axvline(pd.Timestamp('2023-04-01'), color='black', linestyle='--', linewidth=1.5, label='Rilis Pandas 2.0')
ax1.axhline(pre_mean, color='steelblue', linestyle=':', alpha=0.7)
ax1.axhline(post_mean, color='tomato', linestyle=':', alpha=0.7)
ax1.set_title('Bug Reports per Bulan (Jan 2021 - Dec 2025)', fontsize=13)
ax1.set_xlabel('Bulan')
ax1.set_ylabel('Jumlah Bug')
ax1.legend()
ax1.grid(alpha=0.3)

# Subplot 2: Boxplot
ax2 = axes[1]
bp = ax2.boxplot([pre['bug_count'].values, post['bug_count'].values],
                 patch_artist=True,
                 labels=['Pre v2.0', 'Post v2.0'],
                 widths=0.5)
bp['boxes'][0].set_facecolor('steelblue')
bp['boxes'][1].set_facecolor('tomato')
ax2.set_title('Distribusi Bug Per Bulan', fontsize=13)
ax2.grid(alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

# ============================================================
# SEL 8: INDEPENDENT TWO-SAMPLED Z-TEST (KONSISTENSI POISSON)
# ============================================================
n1, n2 = len(pre), len(post)

# KOREKSI UTAMA: Variansi disamakan dengan mean sesuai karakteristik distribusi Poisson
var1_poisson = pre_mean   
var2_poisson = post_mean  

# Hitung Standard Error dan Z-Statistik secara analitik tepat
SE = np.sqrt(var1_poisson/n1 + var2_poisson/n2)    
Z = (pre_mean - post_mean) / SE    
p_value = 2 * (1 - stats.norm.cdf(abs(Z)))

alpha = 0.05
z_crit = stats.norm.ppf(1 - alpha/2)   # Nilai kritis dua sisi (~1.96)

# ============================================================
# SEL 9: VISUALISASI DAERAH PENOLAKAN Z-TEST
# ============================================================
fig, ax = plt.subplots(figsize=(10, 5))
x_axis = np.linspace(-4, 12, 500) # Batas x diperlebar karena nilai Z hitung riil sangat tinggi (9.0985)
y_axis = stats.norm.pdf(x_axis, 0, 1)

ax.plot(x_axis, y_axis, 'black', linewidth=2, label='Distribusi Standar Normal Z')

# Arsir Rejection Region dua sisi
ax.fill_between(x_axis, y_axis, where=(x_axis <= -z_crit), color='tomato', alpha=0.4, label=f'Rejection Region (|Z| > {z_crit:.2f})')
ax.fill_between(x_axis, y_axis, where=((x_axis >= z_crit) & (x_axis <= 4)), color='tomato', alpha=0.4)

# Plot garis posisi Z hitung kelompok
ax.axvline(Z, color='blue', linestyle='--', linewidth=2, label=f'Z hitung = {Z:.4f}')
ax.axvline(-z_crit, color='red', linestyle=':', linewidth=1.5)
ax.axvline(z_crit, color='red', linestyle=':', linewidth=1.5, label=f'Z kritis = +-{z_crit:.2f}')

ax.set_title('Distribusi Z — Uji Hipotesis Dua Sisi (alpha = 0.05)', fontsize=13)
ax.set_xlabel('Z')
ax.set_ylabel('Densitas')
ax.legend(loc='upper right')
ax.grid(alpha=0.3)

plt.tight_layout()
plt.show()