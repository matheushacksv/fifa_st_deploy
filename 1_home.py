import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime


if 'data' not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data[df_data['Value(£)'] > 0]
    df_data = df_data.sort_values(by='Overall', ascending=False)
    st.session_state['data'] = df_data

st.markdown('# FIFA 2023 OFFICIAL DATASET!')

btn = st.link_button('Acesse os dados no Kaggle!', 'https://www.kaggle.com/datasets/bryanb/fifa-player-stats-database')

st.markdown('''
            O conjunto de dados contém mais de 17 mil jogadores únicos e mais de 60 colunas, incluindo informações gerais e todos os KPIs que o famoso videogame oferece. Como o cenário dos esportes eletrônicos continua crescendo, especialmente no FIFA, pensei que isso poderia ser útil para a comunidade (usuários do Kaggle e/ou jogadores).\n
            # Contexto\n
            Os dados foram obtidos por meio de um crawler que coleta:
            - Dados agregados, como nome dos jogadores, idade e país
            - Dados detalhados, como potencial ofensivo, defesa e aceleração
            ''')

