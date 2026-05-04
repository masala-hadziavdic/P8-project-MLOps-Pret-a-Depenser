# ==========================================
# Dockerfile - Pret a depenser (MLOps API)
# ==========================================

# Image Python légère
FROM python:3.11-slim

# Métadonnées
LABEL maintainer="Amela Masala"
LABEL description="API de scoring crédit - Pret a depenser"
LABEL version="1.0"

# Répertoire de travail
WORKDIR /app

# Dépendances système (build ML + pandas/sklearn/xgboost)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copier requirements en premier (cache Docker optimisé)
COPY requirements.txt .

# Installer dépendances Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copier code + modèles
COPY app/ ./app/
COPY models/ ./models/

# Sécurité : user non-root
RUN useradd -m appuser
USER appuser

# Port API
EXPOSE 8000

# Lancement API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]