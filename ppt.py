import tkinter as tk
import random

opcoes = ["pedra", "papel", "tesoura"]
emojis = {"pedra": "🪨", "papel": "📄", "tesoura": "✂️"}

placar = {"jogador": 0, "computador": 0, "empates": 0}


def jogar(escolha_jogador):
    computador = random.choice(opcoes)

    emoji_jogador.config(text=emojis[escolha_jogador])
    emoji_computador.config(text=emojis[computador])

    if escolha_jogador == computador:
        resultado = "Empate!"
        cor = "#f4b400"
        placar["empates"] += 1
    elif (
        (escolha_jogador == "pedra" and computador == "tesoura")
        or (escolha_jogador == "tesoura" and computador == "papel")
        or (escolha_jogador == "papel" and computador == "pedra")
    ):
        resultado = "Você ganhou! 🎉"
        cor = "#0f9d58"
        placar["jogador"] += 1
    else:
        resultado = "Você perdeu!"
        cor = "#db4437"
        placar["computador"] += 1

    label_resultado.config(text=resultado, fg=cor)
    atualizar_placar()


def atualizar_placar():
    label_placar.config(
        text=f"Você {placar['jogador']}  x  {placar['computador']} Computador   "
        f"(Empates: {placar['empates']})"
    )


def reiniciar_placar():
    placar["jogador"] = 0
    placar["computador"] = 0
    placar["empates"] = 0
    atualizar_placar()
    label_resultado.config(text="Placar zerado!", fg="#5f6368")
    emoji_jogador.config(text="❔")
    emoji_computador.config(text="❔")


# --- Janela principal ---
root = tk.Tk()
root.title("Pedra, Papel e Tesoura")
root.geometry("480x650")
root.minsize(460, 600)
root.configure(bg="#1e1e2e")

FONTE_TITULO = ("Segoe UI", 20, "bold")
FONTE_NOME = ("Segoe UI", 13, "bold")
FONTE_NORMAL = ("Segoe UI", 12)
FONTE_EMOJI = ("Segoe UI Emoji", 40)
FONTE_BOTAO = ("Segoe UI", 16)

titulo = tk.Label(
    root,
    text="Pedra, Papel e Tesoura",
    font=FONTE_TITULO,
    bg="#1e1e2e",
    fg="#ffffff",
)
titulo.pack(pady=(20, 10))

# --- Área de exibição das escolhas ---
frame_escolhas = tk.Frame(root, bg="#1e1e2e")
frame_escolhas.pack(pady=10)

frame_jogador = tk.Frame(frame_escolhas, bg="#2a2a3d", width=150, height=140)
frame_jogador.grid(row=0, column=0, padx=10)
frame_jogador.pack_propagate(False)

nome_jogador = tk.Label(frame_jogador, text="Você", font=FONTE_NOME, bg="#2a2a3d", fg="#ffffff")
nome_jogador.pack(pady=(10, 0))

emoji_jogador = tk.Label(frame_jogador, text="❔", font=FONTE_EMOJI, bg="#2a2a3d", fg="#ffffff")
emoji_jogador.pack(expand=True)

label_vs = tk.Label(
    frame_escolhas, text="VS", font=("Segoe UI", 14, "bold"), bg="#1e1e2e", fg="#f4b400"
)
label_vs.grid(row=0, column=1, padx=10)

frame_computador = tk.Frame(frame_escolhas, bg="#2a2a3d", width=150, height=140)
frame_computador.grid(row=0, column=2, padx=10)
frame_computador.pack_propagate(False)

nome_computador = tk.Label(
    frame_computador, text="Computador", font=FONTE_NOME, bg="#2a2a3d", fg="#ffffff"
)
nome_computador.pack(pady=(10, 0))

emoji_computador = tk.Label(
    frame_computador, text="❔", font=FONTE_EMOJI, bg="#2a2a3d", fg="#ffffff"
)
emoji_computador.pack(expand=True)

# --- Resultado ---
label_resultado = tk.Label(
    root, text="Escolha sua jogada!", font=("Segoe UI", 14, "bold"), bg="#1e1e2e", fg="#ffffff"
)
label_resultado.pack(pady=15)

# --- Botões de jogada ---
frame_botoes = tk.Frame(root, bg="#1e1e2e")
frame_botoes.pack(pady=5)

botao_pedra = tk.Button(
    frame_botoes,
    text="🪨 Pedra",
    font=FONTE_BOTAO,
    bg="#3b3b58",
    fg="white",
    activebackground="#50507a",
    relief="flat",
    width=10,
    command=lambda: jogar("pedra"),
)
botao_pedra.grid(row=0, column=0, padx=5, pady=5)

botao_papel = tk.Button(
    frame_botoes,
    text="📄 Papel",
    font=FONTE_BOTAO,
    bg="#3b3b58",
    fg="white",
    activebackground="#50507a",
    relief="flat",
    width=10,
    command=lambda: jogar("papel"),
)
botao_papel.grid(row=1, column=0, padx=5, pady=5)

botao_tesoura = tk.Button(
    frame_botoes,
    text="✂️ Tesoura",
    font=FONTE_BOTAO,
    bg="#3b3b58",
    fg="white",
    activebackground="#50507a",
    relief="flat",
    width=10,
    command=lambda: jogar("tesoura"),
)
botao_tesoura.grid(row=2, column=0, padx=5, pady=5)

# --- Placar ---
label_placar = tk.Label(
    root, text="Você 0  x  0 Computador   (Empates: 0)", font=FONTE_NORMAL, bg="#1e1e2e", fg="#cccccc"
)
label_placar.pack(pady=(20, 5))

botao_reiniciar = tk.Button(
    root,
    text="Zerar placar",
    font=("Segoe UI", 10),
    bg="#db4437",
    fg="white",
    relief="flat",
    command=reiniciar_placar,
)
botao_reiniciar.pack(pady=5)

root.mainloop()