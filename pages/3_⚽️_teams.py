import streamlit as st

st.set_page_config(
    page_title="Players",
    page_icon="🏃🏼",
    layout="wide"
)
# pega o dataframe do estado da sessão
df_data = st.session_state["data"]

# pega os clubes únicos do dataframe
clubes = df_data["Club"].unique().tolist()

# cria um select box para selecionar o clube
club = st.sidebar.selectbox("Clube", clubes)

# cria um dataframe com os dados do clube selecionado
df_filtered = df_data[(df_data["Club"] == club)].set_index("Name")

st.image(df_filtered.iloc[0]["Club Logo"])
st.markdown(f"## {club}")

# cria uma lista de colunas para exibir no dataframe
columns = ["Age", "Photo", "Flag", "Overall", 'Value(£)', 'Wage(£)', 'Joined', 
           'Height(cm.)', 'Weight(lbs.)',
           'Contract Valid Until', 'Release Clause(£)']

# exibe o dataframe com as colunas selecionadas
# usa-se o dataframe filtrado e as colunas selecionadas pois ele permite usar configurações de coluna
# e permite utilizar imagens e flags, de forma mais flexível
# em resumo permite utilizar todos os outros elementos do streamlit
st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100
                 ),
                 "Wage(£)": st.column_config.ProgressColumn("Weekly Wage", format="£%f", 
                                                    min_value=0, max_value=df_filtered["Wage(£)"].max()),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
             })