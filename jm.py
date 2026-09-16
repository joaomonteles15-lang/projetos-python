import tkinter as tk
import random

numero_secreto = random.randint(1, 100)
tentativas = 0


def verificar_palpite():
    global tentativas

    try:
        palpite = int(entry_palpite.get())
    except ValueError:
        label_resultado.config(text="Digite um número válido!")
        return

    tentativas += 1

    if palpite > numero_secreto:
        label_resultado.config(text="Maior! Tente um número menor.")
    elif palpite < numero_secreto:
        label_resultado.config(text="Menor! Tente um número maior.")
    else:
        label_resultado.config(
            text=f"Parabéns! Você acertou em {tentativas} tentativa(s)!"
        )
        botao_chutar.config(state="disabled")

    entry_palpite.delete(0, tk.END)


def reiniciar_jogo():
    global numero_secreto, tentativas
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    label_resultado.config(text="Pensei em um número entre 1 e 100!")
    botao_chutar.config(state="normal")
    entry_palpite.delete(0, tk.END)


# --- Montagem da janela ---
root = tk.Tk()
root.title("Jogo de Adivinhação")
root.geometry("320x280")
root.resizable(False, False)

label_titulo = tk.Label(root, text="Adivinhe o número (1-100)", font=("Arial", 14))
label_titulo.pack(pady=10)

entry_palpite = tk.Entry(root, font=("Arial", 12), justify="center")
entry_palpite.pack(pady=5)

botao_chutar = tk.Button(root, text="Chutar", font=("Arial", 11), command=verificar_palpite)
botao_chutar.pack(pady=5)

label_resultado = tk.Label(
    root,
    text="Pensei em um número entre 1 e 100!",
    font=("Arial", 11),
    wraplength=260,
    justify="center",
)
label_resultado.pack(pady=10)

botao_reiniciar = tk.Button(root, text="Jogar de novo", font=("Arial", 10), command=reiniciar_jogo)
botao_reiniciar.pack(pady=5)

root.mainloop()