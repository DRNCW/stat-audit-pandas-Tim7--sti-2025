# Statistical Audit: pandas-dev/pandas

> **Mata Kuliah:** Statistika & Probabilitas — S1 Teknik Informatika 2024  
> **Kelas:** S124  
> **Semester:** Genap 2025/2026

---

## 1. Deskripsi Proyek

Repository ini berisi **Statistical Health Report** dari proyek open-source [pandas-dev/pandas](https://github.com/pandas-dev/pandas) — library Python paling populer untuk manipulasi dan analisis data, dengan lebih dari 42.000 ⭐ di GitHub.

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

## 3. Temuan Utama (diperbarui setiap checkpoint)

> ⏳ *Akan diisi setelah semua notebook selesai (10 Juni 2026)*

---

## 4. Cara Menjalankan

### Prasyarat
- Python 3.10+
- Git

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
```
01_eda.ipynb          → Jalankan pertama (menghasilkan data/clean/dataset.csv)
02_estimation.ipynb   → Jalankan setelah 01
03_confidence_interval.ipynb  → Setelah 02
04_hypothesis_testing.ipynb   → Setelah 02
05_simulation.ipynb           → Setelah semua selesai
```

---

## 5. Struktur Repository

```
stat-audit-pandas-sti-2025/
├── README.md
├── AI_USAGE_LOG.md
├── requirements.txt
├── data/
│   ├── raw/          ← Data mentah dari GitHub API (jangan diubah)
│   └── clean/        ← dataset.csv hasil cleaning
├── src/
│   ├── __init__.py
│   ├── collect_data.py   ← Pengumpulan data GitHub API
│   ├── estimator.py      ← MLE, Beta posterior (Member B)
│   ├── inference.py      ← CI frequentist & Bayesian (Member C)
│   ├── hypothesis.py     ← Z-test satu & dua sampel (Member D)
│   └── simulation.py     ← Monte Carlo, Bloom Filter, MCMC (Member E)
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_estimation.ipynb
│   ├── 03_confidence_interval.ipynb
│   ├── 04_hypothesis_testing.ipynb
│   └── 05_simulation.ipynb
├── report/
│   └── statistical_health_report.pdf
└── presentation/
    └── video_link.md
```

---

## 6. Tim

| Member | Nama | NIM | Peran |
|--------|------|-----|-------|
| A | [Nama Member A] | [NIM] | Data Engineer |
| B | [Nama Member B] | [NIM] | Estimation Analyst |
| C | [Nama Member C] | [NIM] | Inference Analyst |
| D | [Nama Member D] | [NIM] | Hypothesis Analyst |
| E | [Nama Member E] | [NIM] | Computation Analyst |

---

## 7. Sumber Data

- **Repository:** https://github.com/pandas-dev/pandas
- **API:** GitHub REST API v3 (`/repos/pandas-dev/pandas/issues`, `/pulls`)
- **Rentang data:** Januari 2020 — Mei 2026
- **Keterbatasan:** GitHub API membatasi 5.000 request/jam per token; data diambil menggunakan pagination

---

*Semua formula mengacu pada: Tsun, Probability & Statistics with Applications to Computing, 2020, Chapters 7–9.*
