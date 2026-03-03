#!/bin/bash

echo "🚀 Iniciando Streamlit server com exemplo_04.py..."
touch execution_logs.log
streamlit run exemplo_04.py --server.port=8501 --server.address=0.0.0.0
