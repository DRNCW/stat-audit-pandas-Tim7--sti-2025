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
print(f"Dataset Shape: {df.shape}")   
print(df.head())

# ============================================================
# SEL 5: SPLIT DATA BERDASARKAN RILIS PANDAS 2.0
# ============================================================
cut = pd.Timestamp('2023-04-01')
pre = df[df['timestamp'] < cut].copy()
post = df[df['timestamp'] >= cut].copy()

print(f"Data sebelum April 2023 (Pre-v2.0): {len(pre)} bulan")
print(f"Data sesudah April 2023 (Post-v2.0): {len(post)} bulan")

# ============================================================
# SEL 6: HITUNG RATA-RATA LAJU BUG BULANAN (MLE POISSON)
# ============================================================
pre_mean = pre['bug_count'].mean()
post_mean = post['bug_count'].mean()

print(f"Rata-rata bug per bulan (Pre-v2.0): {pre_mean:.4f}")
print(f"Rata-rata bug per bulan (Post-v2.0): {post_mean:.4f}")

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
save_path_plot = os.path.join(current_dir, '..', 'data', 'clean', 'hypothesis_plot.png')
plt.savefig(save_path_plot, dpi=150, bbox_inches='tight')
plt.show()
print(f"Plot komparasi tersimpan di: {save_path_plot}")

# ============================================================
# SEL 8: INDEPENDENT TWO-SAMPLED Z-TEST (KONSISTENSI POISSON)
# Di bawah asumsi model Poisson, nilai Variansi = Nilai Mean
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

print("\n" + "="*50)
print("   - HASIL POISSON Z-TEST DUA SAMPEL (REVISI) -   ")
print("="*50)
print(f"  Mean Laju Bug Pre-v2.0 ($\lambda_1$)  = {pre_mean:.4f}  (n={n1})")
print(f"  Mean Laju Bug Post-v2.0 ($\lambda_2$) = {post_mean:.4f}  (n={n2})")
print(f"  Selisih Efek Absolut (D)      = {pre_mean - post_mean:.4f}")
print(f"  Standard Error Poisson (SE)   = {SE:.4f}")
print(f"  Z hitung                      = {Z:.4f}")
print(f"  Z kritis (alpha=0.05, 2-tail) = +-{z_crit:.4f}")
print(f"  p-value                       = {p_value:.6e}")
print("-" * 50)

if p_value < alpha:
    print(f"  Keputusan: p-value ({p_value:.4e}) < alpha ({alpha}) -> TOLAK Ho")
    print("  Kesimpulan: Ada perbedaan laju bug bulanan yang sangat signifikan pasca rilis Pandas 2.0.")
else:
    print(f"  Keputusan: p-value ({p_value:.4e}) >= alpha ({alpha}) -> GAGAL TOLAK Ho")
    print("  Kesimpulan: Tidak cukup bukti statistik untuk menyatakan adanya perbedaan laju bug.")
print("="*50 + "\n")

# ============================================================
# SEL 9: VISUALISASI DAERAH PENOLAKAN Z-TEST
# ============================================================
fig, ax = plt.subplots(figsize=(10, 5))
x_axis = np.linspace(-4, 12, 500) # Perlebar batas x karena nilai Z hitung kalian sangat tinggi
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
save_path_z = os.path.join(current_dir, '..', 'data', 'clean', 'z_distribution_plot.png')
plt.savefig(save_path_z, dpi=150, bbox_inches='tight')  
plt.show()
print(f"Plot distribusi Z-test berhasil diperbarui dan disimpan di: {save_path_z}")