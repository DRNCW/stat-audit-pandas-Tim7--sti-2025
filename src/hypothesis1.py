
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


print("  ")


#SEL 7 - VISUALISASI
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1 - Time series Subplot
ax1 = axes[0]
ax1.plot(pre['timestamp'], pre['bug_count'].values, color='steelblue', marker='o', markersize=4, label='Pre v2.0')
ax1.plot(post['timestamp'], post['bug_count'].values, color='tomato', marker='o', markersize=4, label='Post v2.0')
ax1.axvline(pd.Timestamp('2023-04-01'), color='black', linestyle='--', linewidth=1.5, label='Rilis Pandas 2.0')
ax1.axhline(pre['bug_count'].mean(), color='steelblue', linestyle=':', alpha=0.7)
ax1.axhline(post['bug_count'].mean(), color='tomato', linestyle=':', alpha=0.7)
ax1.set_title('Bug Reports per Bulan (Jan 2021 - Dec 2025)', fontsize=13)
ax1.set_xlabel('Bulan')
ax1.set_ylabel('Jumlah Bug')
ax1.legend()
ax1.grid(alpha=0.3)


# Plot 2 - Boxplot
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
save_path = os.path.join(current_dir, '..', 'data', 'clean', 'hypothesis_plot.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight')  # ← tambah ) di sini
plt.show()
print("Plot tersimpan di data/clean/hypothesis_plot.png")


print("  ")


# ============================================================
# Z-TEST DUA SAMPEL INDEPENDEN
# Asumsi distribusi Poisson → variansi ≈ rata-rata (MLE)
# ============================================================

n1, n2     = len(pre), len(post)
x_bar1     = pre['bug_count'].mean()
x_bar2     = post['bug_count'].mean()

# Untuk data count (Poisson), var = mean → gunakan var sampel
var1 = pre['bug_count'].var(ddof=1)   # s1²
var2 = post['bug_count'].var(ddof=1)  # s2²

# Hitung Z statistik secara manual
SE   = np.sqrt(var1/n1 + var2/n2)    # Standard Error
Z    = (x_bar1 - x_bar2) / SE        # Z statistic
# p-value two-tailed
p_value = 2 * (1 - stats.norm.cdf(abs(Z)))

# Z kritis untuk α = 0.05 two-tailed
alpha    = 0.05
z_crit   = stats.norm.ppf(1 - alpha/2)   # ≈ 1.96

print("=" * 50)
print("   - HASIL Z-TEST DUA SAMPEL -   ")
print("=" * 50)
print(f"  x_bar pre-v2      = {x_bar1:.4f}  (n={n1})")
print(f"  x_bar post-v2     = {x_bar2:.4f}  (n={n2})")
print(f"  Selisih (D)    = {x_bar1 - x_bar2:.4f}")
print(f"  Standard Error = {SE:.4f}")
print(f"  Z hitung       = {Z:.4f}")
print(f"  Z kritis (a=0.05, 2-tail) = +-{z_crit:.4f}")
print(f"  p-value        = {p_value:.6f}")
print()
if p_value < alpha:
    print(f"   p-value ({p_value:.4f}) < a ({alpha}) -> TOLAK Ho")
    print("  Ada perbedaan signifikan setelah pandas 2.0")
else:
    print(f"   p-value ({p_value:.4f}) >= a ({alpha}) -> GAGAL TOLAK Ho")
    print("  Tidak ada bukti perbedaan signifikan")
print("=" * 50)



print("  ")



# SEL 9 - VISUALISASI Z-TEST
fig, ax = plt.subplots(figsize=(10, 5))

x = np.linspace(-4, 4, 400)
y = stats.norm.pdf(x)

ax.plot(x, y, 'black', linewidth=2)

# Arsir rejection region
ax.fill_between(x, y, where=(x <= -z_crit), color='tomato', alpha=0.4, label=f'Rejection region (|Z| > {z_crit:.2f})')
ax.fill_between(x, y, where=(x >=  z_crit), color='tomato', alpha=0.4)

# Garis Z hitung
ax.axvline(Z, color='blue', linestyle='--', linewidth=2, label=f'Z hitung = {Z:.4f}')
ax.axvline(-z_crit, color='red', linestyle=':', linewidth=1.5)
ax.axvline( z_crit, color='red', linestyle=':', linewidth=1.5, label=f'Z kritis = +-{z_crit:.2f}')

ax.set_title('Distribusi Z — Uji Hipotesis Dua Sisi (a = 0.05)', fontsize=13)
ax.set_xlabel('Z')
ax.set_ylabel('Densitas')
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
save_path = os.path.join(current_dir, '..', 'data', 'clean', 'hypothesis_plot.png')
plt.savefig(save_path, dpi=150, bbox_inches='tight')  
plt.show()
print("Plot Z-test tersimpan di data/clean/hypothesis_plot.png")









