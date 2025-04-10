# 📊 Causal ATE Estimation API

This project implements a Flask-based API that estimates the **Average Treatment Effect (ATE)** using a linear regression model inspired by the **Rubin Causal Model**. It determines the causal impact of a treatment (e.g. participation in a carbon offset program) on engagement score, controlling for sustainability spending.

---

## 🧠 Model

The regression formula used is:

```
Yᵉ = α + τ·Wᵉ + β·Xᵉ + εᵉ
```

Where:
- **Yᵉ**: Engagement Score (observed outcome)
- **Wᵉ**: Treatment indicator (1 = participated, 0 = did not)
- **Xᵉ**: Sustainability Spending ($1,000s)
- **α, τ, β**: Parameters to be estimated
- **τ**: Interpreted as the **Average Treatment Effect (ATE)**

---

## 🚀 Quickstart with Docker

### 💠 Build and Run

```bash
docker build -t my-api .
docker run -p 5000:5000 my-api
```

---

## 📬 API Usage

Send a POST request with JSON data:

```bash
curl -X POST http://localhost:5000/estimate_ate \
     -H "Content-Type: application/json" \
     -d @data.json
```

---

## 📦 Project Files

```
causal-ate-api/
├── app.py                # Flask API with OLS regression
├── requirements.txt      # Python dependencies
├── Dockerfile            # Build container image
├── data.json             # Sample input data
├── output.txt            # Logs the estimated ATE
└── README.md             # This file
```

---

## 📄 Sample Input (`data.json`)

See below or use directly in your project.

---

## 📄 Sample Output

```json
{
  "alpha": 95.97,
  "tau (ATE)": -9.11,
  "beta": 1.51,
  "p_value_tau": 0.0003
}
```

And saved to:

```txt
Estimated ATE (tau): -9.1057
```

---

## 🧹 .gitignore (Recommended)

```
__pycache__/
*.pyc
output.txt
.env
*.log
```
## 🔍 Component Explanations

- **`app.py`** defines the core logic of the application: it loads input JSON data, fits a linear regression model to estimate the Average Treatment Effect (ATE), and returns the results via a Flask API.

- **`Dockerfile`** creates a reproducible environment for running the application, ensuring all dependencies and configurations are consistent across systems without needing to install anything locally.

- **Containerization** with Docker improves portability and reproducibility by packaging the application and its dependencies into a single unit that runs identically on any machine or cloud environment.

---
