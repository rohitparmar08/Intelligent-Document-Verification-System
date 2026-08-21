# Intelligent Document Verification System

[![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Framework-Django-092E20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Computer Vision](https://img.shields.io/badge/Vision-OpenCV-5C3EE8?style=flat-square&logo=opencv)](https://opencv.org/)
[![OCR](https://img.shields.io/badge/OCR-EasyOCR-FF6F00?style=flat-square)](https://github.com/JaidedAI/EasyOCR)
[![Database](https://img.shields.io/badge/Database-SQLite-003B57?style=flat-square&logo=sqlite)](https://www.sqlite.org/)

An AI-powered document verification web application built with **Django, OpenCV, and EasyOCR**. The platform automates identity document (Aadhaar) quality analysis, text extraction, validation, and automated report generation.

---

## 📌 Problem Statement

Manual verification of physical or digital identity documents is slow, error-prone, and vulnerable to poor image quality (blurriness, low lighting, heavy image noise). 

This project provides an automated pipeline that:
1. **Evaluates Image Quality**: Pre-screens uploaded documents for blur, noise, brightness, and resolution before OCR processing.
2. **Automates Text Extraction**: Uses OpenCV image processing and EasyOCR to read text fields.
3. **Generates Structured Output**: Validates extracted fields and exports downloadable JSON and PDF reports.

---

## 🔬 Core Pipeline & Architecture

```
┌─────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│ Document Upload │ ──► │ Image Quality Engine │ ──► │     OCR Engine       │
│  (Aadhaar Image)│     │(Blur/Noise/Lighting) │     │ (OpenCV + EasyOCR)   │
└─────────────────┘     └──────────────────────┘     └──────────┬───────────┘
                                                                │
                                                                ▼
┌─────────────────┐     ┌──────────────────────┐     ┌──────────────────────┐
│ Downloadable PDF│ ◄── │   Report Generator   │ ◄── │ Verification Engine  │
│  & JSON Export  │     │  (JSON & ReportLab)  │     │(Regex & Field Match) │
└─────────────────┘     └──────────────────────┘     └──────────────────────┘
```

---

## ✨ Key Features

### 1. Image Quality Analysis Module
Located in `app/image_processing/`:
- **Blur Detection**: Uses OpenCV Laplacian variance thresholding to detect blurry uploads.
- **Noise Analysis**: Evaluates image signal-to-noise ratio (SNR) to filter degraded files.
- **Brightness & Contrast Check**: Measures pixel intensity distribution to detect overexposed or underexposed images.
- **Resolution Validation**: Enforces minimum dimensions required for OCR accuracy.

### 2. OCR & Detail Extraction Pipeline
Located in `app/ocr/` and `app/extractor/`:
- **Pre-processing**: OpenCV grayscale conversion, noise reduction, and thresholding.
- **Text Recognition**: EasyOCR engine extracts text blocks from pre-processed document regions.
- **Field Extractor**: Regex-based parser identifies Aadhaar numbers (12-digit format), Date of Birth (DOB), Name, and Gender.

### 3. Verification & Report Generation
Located in `app/report/` and `document_app/`:
- **JSON Payload Generation**: Structured JSON output containing quality scores, status, and extracted metadata.
- **PDF Report Generation**: Automated downloadable PDF verification report built with ReportLab.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.10+, Django 5.2
- **Computer Vision & OCR**: OpenCV (`opencv-python`), EasyOCR
- **PDF Generation**: ReportLab
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Database**: SQLite3

---

## 🚀 Installation & Setup

### 1. Prerequisites
- Python 3.10 or higher
- `pip` package manager

### 2. Installation Steps

```bash
# Clone the repository
git clone https://github.com/rohitparmar08/Intelligent-Document-Verification-System.git
cd Intelligent-Document-Verification-System

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# Install required dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py migrate

# Start development server
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 🔒 Privacy & Safety Disclaimer

> [!IMPORTANT]
> **Data Privacy Notice**: This repository is designed for educational and demonstration purposes.  
> **No real Aadhaar documents, PII (Personally Identifiable Information), or sensitive identity credentials should ever be uploaded or stored.**  
> Always test using synthetic, dummy, or fully redacted sample documents.
