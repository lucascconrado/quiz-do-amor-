import streamlit as st # LINHA OBRIGATÓRIA: Importa a biblioteca Streamlit

# --- Configurações Iniciais e Variáveis ---
nome_correto = "Thauane" # <<<<< MUITO IMPORTANTE: Mude para o nome exato da sua namorada!

# --- Bloco 1: Validação do Nome ---
# Usamos st.session_state para "lembrar" se o nome já foi validado.
# Se 'nome_validado' não existir ou for False, mostramos o pedido de nome.
if 'nome_validado' not in st.session_state or not st.session_state.nome_validado:
    st.write("--- Vamos Começar! ---")
    st.write("Esse é um programinha feito para você, meu amor! ❤️")

    # st.text_input cria uma caixa de texto para o usuário digitar
    nome_digitado = st.text_input("Qual é o seu nome, meu amor?", key="nome_input_key").strip()
    # .strip() remove espaços extras no começo/fim que a pessoa possa digitar

    # Verifica se o usuário digitou algo e se o nome está correto
    if nome_digitado: # Garante que o usuário digitou algo
        if nome_digitado.lower() == nome_correto.lower():
            st.success(f"Olá, {nome_correto}! Que bom que você veio.") # st.success mostra uma mensagem verde
            st.session_state.nome_validado = True # Define que o nome foi validado para não pedir de novo
            st.rerun() # Reinicia o app para mostrar a próxima parte (a pergunta do amor)
        else:
            st.error(f"Hummm, você digitou '{nome_digitado}', mas não é o nome certo...") # st.error mostra uma mensagem vermelha
            st.info("Tente de novo, por favor! (Pista: o nome começa com a letra 'T'.)") # st.info mostra uma mensagem azul

# --- Bloco 2: Pergunta de Amor (Só aparece SE o nome já foi validado) ---
# Só entra neste bloco se 'nome_validado' existir e for True
if 'nome_validado' in st.session_state and st.session_state.nome_validado:
    st.write("\n--- Pergunta séria: Você me ama? ---")
    st.write("Escolha uma das opções:")

    # st.button cria um botão clicável
    # O 'key' é importante para o Streamlit identificar cada botão
    opcao1 = st.button("1 - Sim", key="btn_sim")
    opcao2 = st.button("2 - Claro", key="btn_claro")
    opcao3 = st.button("3 - Óbvio", key="btn_obvio")

    # Verifica qual botão foi clicado
    if opcao1 or opcao2 or opcao3:
        st.balloons() # Mostra balões subindo (efeito legal!)
        st.success(f"hehehe, eu sabia!!! também te amo, {nome_correto}!")
        st.write("\n--- Fim do nosso quiz, amor! Te amo! ❤️ ---")
        st.stop() # Finaliza a execução do app para não continuar mostrando os botões
    else:
        st.write("Por favor, clique em uma das opções acima.")
