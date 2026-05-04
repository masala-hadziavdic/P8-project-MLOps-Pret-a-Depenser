flowchart LR

    subgraph Client
        C[Client HTTP]
    end

    subgraph Backend
        API[FastAPI API<br/>:8000]
        Model[XGBoost Model]
        Logs[Structlog Logs]
    end

    subgraph Data
        DB[(PostgreSQL)]
    end

    subgraph Monitoring
        Drift[Evidently AI]
        Dash[Streamlit<br/>:8501]
    end

    C --> API
    API --> Model
    API --> DB
    DB --> Drift
    Drift --> DB

    API --> Logs

    DB --> Dash
    API --> Dash

    API --> C