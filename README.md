# Sentiment Analysis API with Flask

[![CI pipeline testing](https://github.com/AbdulDD/Sentimental-Analysis-API-with-Flask-Continuous-Integration-CI-pipeline/actions/workflows/makefile.yml/badge.svg)](https://github.com/AbdulDD/Sentimental-Analysis-API-with-Flask-Continuous-Integration-CI-pipeline/actions/workflows/makefile.yml)

**Overview**

- This repository contains a **Sentiment Analysis API** built with **Flask** and integrated into a **Continuous Integration (CI)** pipeline using **GitHub Actions**.

- The API leverages a pre-trained sentiment analysis model from Hugging Face to classify text inputs as positive or negative. The focus of this project is on inference only, demonstrating how to automate testing, validation, and deployment readiness using CI practices — a key skill in MLOps workflows.

**Key Features**

- **Pre-trained Model Integration:** Uses Hugging Face models for quick deployment without training.

- **API Development:** Provides a lightweight web service with Flask to serve predictions.- 

- **Continuous Integration Pipeline:** GitHub Actions automatically tests your code whenever changes are pushed or pull requests are created.

- **Automated Testing:** Validates the API endpoints and inference outputs with unit tests.

- **Environment Reproducibility:** Developed inside GitHub Codespaces for consistent cloud-based development.

**Tools and Technologies**

Python | Flask | ML Model (Hugging Face Transformers) | Testing (Pytest) | Linting | CI using GitHub Actions | GitHub Codespaces | Dependency Management (requirements.txt)
