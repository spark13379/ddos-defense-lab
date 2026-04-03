# 🛡️ DDoS Defense Lab

Simulador de carga (stress test) com sistema de defesa contra excesso de requisições.

## 🚀 Funcionalidades

- Simulação de tráfego alto
- Rate limiting por IP
- Bloqueio automático
- Monitoramento de CPU e RAM

## ⚙️ Tecnologias

- Python
- FastAPI
- httpx
- psutil

## ▶️ Como rodar

### 1. Instalar dependências
pip install -r requirements.txt

### 2. Rodar servidor
uvicorn server.app:app --reload

### 3. Rodar ataque (em outro terminal)
python attacker/load_test.py

### 4. Monitoramento
python monitor/metrics.py

## ⚠️ Aviso

Projeto educacional.
Executar apenas em ambiente local (localhost).