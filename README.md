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

> *Akan diisi setelah semua notebook selesai (10 Juni 2026)*

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


