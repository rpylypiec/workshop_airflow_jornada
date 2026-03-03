# poetry add streamlit pandas

import streamlit as st
import pandas as pd
import subprocess
import os
import sys


# Função para carregar os dados do arquivo CSV
def load_data():
    if os.path.exists("execution_logs.log"):
        try:
            df = pd.read_csv("execution_logs.log")
            return df
        except Exception as e:
            st.error(f"Erro ao carregar arquivo: {e}")
            return pd.DataFrame()
    else:
        st.warning("Arquivo execution_logs.log não encontrado.")
        return pd.DataFrame()


# Função para executar o script Python
def run_python_script():
    try:
        result = subprocess.run(
            [sys.executable, "pipeline/pipeline.py"],  # usa o python do container
            capture_output=True,
            text=True
        )
        return result
    except Exception as e:
        st.error(f"Erro ao executar script: {e}")
        return None


# Layout do aplicativo Streamlit
def main():
    st.title("Visualização de Logs e Execução de Scripts")
    
    if os.path.exists("pics/elyflow.png"):
        st.image("pics/elyflow.png")

    # Carregar os dados do arquivo CSV
    df = load_data()

    # Exibir os dados na interface do Streamlit
    st.subheader("Logs de Execução")
    st.dataframe(df)

    # Botão para atualizar os dados
    if st.button("Atualizar Dados"):
        df = load_data()
        st.success("Dados Atualizados com Sucesso!")
        st.dataframe(df)

    # Botão para executar o script Python
    if st.button("Executar Script Python"):
        result = run_python_script()

        if result is not None:
            if result.returncode == 0:
                st.success("Script executado com sucesso!")
                st.text(result.stdout)
            else:
                st.error("Erro ao executar o script")
                st.text(result.stderr)


if __name__ == "__main__":
    main()