import tkinter as tk
from tkinter import filedialog, messagebox
from main import aplicar_marca_dagua


def selecionar_pasta():
    pasta = filedialog.askdirectory()
    if pasta:
        entry_pasta.delete(0, tk.END)
        entry_pasta.insert(0, pasta)


def selecionar_logo():
    arquivo = filedialog.askopenfilename(
        filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")]
    )
    if arquivo:
        entry_logo.delete(0, tk.END)
        entry_logo.insert(0, arquivo)


def executar():
    pasta = entry_pasta.get()
    logo = entry_logo.get()
    sufixo = entry_sufixo.get() or "_marca"

    try:
        total = aplicar_marca_dagua(pasta, logo, sufixo)
        messagebox.showinfo(
            "Concluído",
            f"{total} imagens processadas com sucesso!"
        )
    except Exception as erro:
        messagebox.showerror("Erro", str(erro))


# ================= INTERFACE =================

janela = tk.Tk()
janela.title("Aplicador de Marca d'Água")
janela.geometry("500x260")
janela.resizable(False, False)

tk.Label(
    janela,
    text="Automação de Marca d'Água",
    font=("Arial", 14, "bold")
).pack(pady=10)

frame = tk.Frame(janela)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="Pasta das imagens:").grid(row=0, column=0, sticky="w")
entry_pasta = tk.Entry(frame, width=40)
entry_pasta.grid(row=0, column=1, padx=5)
tk.Button(frame, text="Selecionar", command=selecionar_pasta).grid(row=0, column=2)

tk.Label(frame, text="Logo:").grid(row=1, column=0, sticky="w", pady=8)
entry_logo = tk.Entry(frame, width=40)
entry_logo.grid(row=1, column=1, padx=5)
tk.Button(frame, text="Selecionar", command=selecionar_logo).grid(row=1, column=2)

tk.Label(frame, text="Sufixo:").grid(row=2, column=0, sticky="w")
entry_sufixo = tk.Entry(frame, width=40)
entry_sufixo.insert(0, "_marca")
entry_sufixo.grid(row=2, column=1, columnspan=2)

tk.Button(
    janela,
    text="Aplicar Marca d'Água",
    command=executar,
    bg="#2ecc71",
    fg="white",
    font=("Arial", 10, "bold"),
    width=30
).pack(pady=15)

janela.mainloop()
