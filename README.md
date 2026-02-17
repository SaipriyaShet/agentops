## 🔮 MLOps Roadmap

Future versions of AgentOps will include:

- ML-based anomaly detection models
- Forecasting models (time series)
- Experiment tracking using MLflow
- Model versioning and performance monitoring
- Automated retraining pipelines

MLOps is intentionally deferred until ML models are introduced.
 # AgentOps – Autonomous Business Intelligence Platform (v1.0)

AgentOps is a stateful, multi-agent AI platform for business intelligence.
It combines SQL analytics, RAG, anomaly detection, forecasting, memory,
adaptive behavior, feedback loops, safety controls, ML models, and a
visual dashboard.

## Features
- Multi-agent orchestration (SQL, RAG, Anomaly, Forecast, Actions)
- Persistent memory with temporal analysis
- Adaptive thresholds and confidence scoring
- Feedback loop for self-evaluation
- Stability layer (rate limiting, circuit breaker, safe mode)
- ML-powered anomaly detection & forecasting
- Simulation engine for stress testing
- Internal dashboard API + Streamlit UI

## Architecture
- Backend: FastAPI
- UI: Streamlit
- ML: scikit-learn
- Storage: SQLite (local)

## Run Backend
```bash
python -m uvicorn app.api.query:app --reload
