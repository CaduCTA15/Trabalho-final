import tkinter as tk
from tkinter import messagebox

acoes = []
perguntas = [
    "Você ligou o carro?",
    "Você utilizou a seta?",
    "Você girou o volante?"
]

passo = 0

def responder(resposta):
    global passo
    acao = perguntas[passo].replace("Você ", "").replace("?", "").lower()
    acoes.append(f"{acao} - {'Sim' if resposta else 'Não'}")
    passo += 1

    if passo < len(perguntas):
        pergunta_label.config(text=perguntas[passo])
    else:
        mostrar_resumo()

def mostrar_resumo():
    resumo = "\n".join(f"- {a}" for a in acoes)
    messagebox.showinfo("Resumo", resumo)
    botoes.pack_forget()
    btn_reiniciar.pack(pady=10)
    btn_sair.pack(pady=5)

def reiniciar():
    global passo
    passo = 0
    acoes.clear()
    pergunta_label.config(text=perguntas[0])
    btn_reiniciar.pack_forget()
    btn_sair.pack_forget()
    botoes.pack()

janela = tk.Tk()
janela.title("Simulador de Direção")
janela.geometry("360x240")

pergunta_label = tk.Label(janela, text=perguntas[0], font=("Arial", 14))
pergunta_label.pack(pady=20)

botoes = tk.Frame(janela)
botoes.pack()

tk.Button(botoes, text="Sim", width=10, command=lambda: responder(True)).grid(row=0, column=0, padx=10)
tk.Button(botoes, text="Não", width=10, command=lambda: responder(False)).grid(row=0, column=1, padx=10)

btn_reiniciar = tk.Button(janela, text="Nova Simulação", command=reiniciar)
btn_sair = tk.Button(janela, text="Sair", command=janela.quit)

janela.mainloop()