# Statistical Audit: pandas-dev/pandas

> **Mata Kuliah:** Statistika & Probabilitas — S1 Sistem Teknologi Informasi 2025 
> **Kelas:** A  
> **Semester:** Genap 2025/2026

---

## Daftar Isi
1. [Deskripsi Proyek](#1-deskripsi-proyek)
2. [Research Questions](#2-research-questions)
3. [Finding](#3-Finding)
4. [How-to-Run](#4-How-to-Run)
5. [Team Table](#5-tim)
6. [Sumber Data & Referensi](#6-sumber-data--referensi)

---

## 1. Deskripsi Proyek

Repository ini berisi **Statistical Health Report** dari proyek open-source [pandas-dev/pandas](https://github.com/pandas-dev/pandas) — library Python paling populer untuk manipulasi dan analisis data, dengan jutaan pengguna aktif di seluruh dunia.

Repositori ini dipilih karena memenuhi seluruh kriteria teknis (≥1.000 closed issues, ≥500 merged PRs, data bertimestamp lengkap), sekaligus memiliki momen rilis pandas 2.0 (3 April 2023) yang menjadi titik pemisah alami untuk menguji perubahan perilaku proyek secara statistik.

Analisis mencakup data dari 1 Januari 2021 hingga 31 Desember 2025, dan diambil melalui GitHub REST API v3.

Audit statistik ini menerapkan konsep dari **Minggu 11–14**:
- **Estimasi Parameter** (MLE, Beta Posterior)
- **Interval Kepercayaan** (Frequentist & Bayesian)
- **Pengujian Hipotesis** (Z-test satu & dua sampel)
- **Probabilitas Komputasional** (Monte Carlo, Bloom Filter, MCMC)

---

## 2. Research Questions

Ketiga pertanyaan penelitian berikut menjadi **benang merah** seluruh analisis:

| # | Research Question | Layer | Teknik |
|---|-------------------|-------|--------|
| **RQ1** | *"Berapa probabilitas estimasi sebuah Pull Request (PR) di pandas-dev/pandas akan di-merge, dan seberapa tidak pasti estimasi tersebut?"* | Estimasi | MLE Bernoulli + Beta Posterior |
| **RQ2** | *"Apakah rata-rata tingkat laporan bug per bulan mengalami perubahan yang signifikan secara statistik setelah rilis pandas 2.0 (April 2023)?"* | Inferensi & Hipotesis | MLE Poisson + Z-test Dua Sampel |
| **RQ3** | *"Berapa probabilitas sebuah issue membutuhkan waktu lebih dari 30 hari untuk di-close, dan seberapa akurat sistem Bloom Filter dalam mendeteksi laporan duplikat?"* | Simulasi | Monte Carlo + Bloom Filter + MCMC |

---

## 3. Findings (diperbarui setiap checkpoint)

>### Member A – Data Engineer (EDA & Data Collection)

Research Questions Addressed: RQ1, RQ2, RQ3

Data dikumpulkan dari GitHub API repositori pandas-dev/pandas (Jan 2021 – Des 2025),
menghasilkan tiga dataset bersih: prs_clean.csv (3.228 PR valid), monthly_bugs.csv
(60 bulan data bug), dan issues_full.csv (seluruh issue valid). EDA menunjukkan
mayoritas PR berhasil di-merge (~70%), rata-rata bug turun dari 60.56 menjadi
43.39/bulan pasca rilis Pandas 2.0, dan distribusi waktu penyelesaian issue bersifat
right-skewed dengan sebagian issue melampaui 30 hari.


### Member B – Parameter Estimator (MLE Bernoulli & Poisson)

Research Questions Addressed: RQ1, RQ2

Dari 3.228 sampel PR, MLE Bernoulli menghasilkan θ‌ = 0.7085 (70.85% PR
berhasil di-merge) dengan Beta posterior α = 2288, β = 942. Untuk RQ2, MLE
Poisson menghasilkan laju bug λ‌₁ = 60.56/bulan (pre-v2.0) dan
λ‌₂ = 43.39/bulan  (post-v2.0). Kedua nilai λ ini diteruskan sebagai
input utama pengujian hipotesis di Notebook 04.


### Member C - Inference Analyst ( Confidence Interval )

Research Questions : 
RQ1 – Probabilitas Pull Request Di-merge

Analisis menunjukkan bahwa probabilitas sebuah pull request berhasil di-merge diperkirakan sebesar 70,85%. Confidence Interval Bernoulli 95% ((0,6928 ; 0,7242)) dan Bayesian Credible Interval 95% ((0,6926 ; 0,7239)) memberikan hasil yang hampir identik. Temuan ini menunjukkan bahwa probabilitas merge berada pada kisaran 69%–72% dengan tingkat ketidakpastian yang relatif rendah.

RQ2 – Laju Laporan Bug Bulanan

Analisis Poisson menghasilkan estimasi rata-rata jumlah bug sebesar 50,95 bug per bulan dengan Confidence Interval 95% ((49,16 ; 52,79)). Rentang interval yang relatif sempit menunjukkan bahwa laju laporan bug bulanan cukup stabil selama periode observasi. Hasil ini menjadi dasar untuk pengujian hipotesis pada tahap berikutnya guna mengevaluasi apakah terdapat perubahan signifikan setelah rilis pandas 2.0.

Secara keseluruhan, hasil inferensi menunjukkan bahwa estimasi parameter memiliki tingkat presisi yang baik. Probabilitas merge pull request diperkirakan berada pada rentang 69%–72%, sedangkan laju rata-rata bug bulanan berada pada rentang 49–53 bug per bulan.


### Member D – Hypothesis Analyst (Two-Sample Z-Test)

Research Question: Apakah rata-rata jumlah laporan bug per bulan berubah
secara signifikan setelah rilis Pandas 2.0 (April 2023)?

Pengujian two-sample Z-test berbasis model Poisson terhadap 60 data bulanan
menunjukkan rata-rata bug turun dari 60.56 menjadi 43.39/bulan (selisih
17.16). Z hitung = 9.0985 jauh melampaui Z kritis ±1.96 dengan p-value ≈ 0,
sehingga H₀ ditolak — terdapat penurunan signifikan pada laporan bug
setelah rilis Pandas 2.0, dikonfirmasi pula oleh visualisasi boxplot yang
menunjukkan kedua periode tidak tumpang tindih.


### Member E – Computational Analyst (Monte Carlo, Bloom Filter, MCMC)

Research Question: RQ3 — Probabilitas issue > 30 hari & akurasi Bloom Filter

Simulasi Monte Carlo (10.000 sampel bootstrap) memperkirakan probabilitas issue
membutuhkan waktu lebih dari 30 hari sebesar 41.17%, mengonfirmasi distribusi
right-skewed pada data. Bloom Filter dengan kapasitas 10.000 bit mengalami saturasi
(fill rate 86.62%) sehingga FPR teoritis mencapai 65.39% — kapasitas optimal
yang direkomendasikan adalah 37.880 bit. Simulasi MCMC (Metropolis-Hastings,
10.000 iterasi) turut mengeksplorasi anomali long-tail sebagai landasan proyeksi
risiko backlog jangka panjang.

---

## 4. How-to-Run

### Prasyarat
- Python 3.10+
- Git
- GitHub Personal Access Token (PAT) dengan scope `public_repo`

### Instalasi

```bash
# 1. Clone repository ini
git clone https://github.com/<username>/stat-audit-pandas-sti-2025.git
cd stat-audit-pandas-sti-2025

# 2. Buat virtual environment
python -m venv venv
source venv/bin/activate        # Linux/Mac
# atau: venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Jalankan pengumpulan data (butuh GitHub token)
# Buat file .env dan isi: GITHUB_TOKEN=ghp_xxxxx
python src/collect_data.py

# 5. Jalankan Jupyter
jupyter notebook notebooks/
```

### Urutan Notebook

> Jalankan secara **berurutan** — setiap notebook bergantung pada output notebook sebelumnya.

```
01_eda.ipynb          → Jalankan pertama (menghasilkan data/clean/dataset.csv)
02_estimation.ipynb   → Jalankan setelah 01
03_confidence_interval.ipynb  → Setelah 02
04_hypothesis_testing.ipynb   → Setelah 02
05_simulation.ipynb           → Setelah semua selesai
```

---

## 5. Team Table

| Member | Nama | NIM | Peran |
|--------|------|-----|-------|
| A | [Darren Chandra Wijaya] | [1519625019] | Data Engineer |
| B | [Muhammad Zulhaydar Omar Rafiq] | [1519625046] | Estimation Analyst |
| C | [Michelle Fiorentina Won] | [1519625024] | Inference Analyst |
| D | [Bonita Zhafira Mulyowijoyo] | [1519625035] | Hypothesis Analyst |
| E | [Kumara Tsany Widyadana] | [1519625034] | Computation Analyst |

> Rantai ketergantungan: **A → B → C, D → E**

---

## 6. Sumber Data & Referensi

**Data**
- Repositori target: ["pandas-dev/pandas"](https://github.com/pandas-dev/pandas)
- API: [GitHub REST API v3](https://docs.github.com/en/rest) — endpoint "/repos/{owner}/{repo}/pulls" dan "/search/issues"
- Rentang data: 1 Januari 2021 – 31 Desember 2025

**Referensi**
- Tsun. (2020). *Probability & Statistics with Applications to Computing*, Chapters 7–9.
- [pandas 2.0.0 Release Notes](https://pandas.pydata.org/docs/whatsnew/v2.0.0.html) *(rilis: 3 April 2023)*

*Semua formula mengacu pada: Tsun, Probability & Statistics with Applications to Computing, 2020, Chapters 7–9.*

---


