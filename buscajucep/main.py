import os
from tkinter import *

# path_dir = r"C:\Users\04985470430\Downloads"
# nome_arquivo = '450-2021'

def OnClick():
    path_dir = et_dir.get()
    nome_arquivo = et_arq.get()
    # buscaArquivo(path_dir, nome_arquivo)
    lb_resultado['text'] = buscaArquivo(path_dir, nome_arquivo)
    et_resporta['text'] = buscaArquivo(path_dir, nome_arquivo)


def buscaArquivo(path_dir, nome_arquivo):

    contador = 0
    for raiz, diretorios, arquivos in os.walk(path_dir):
        for arquivo in arquivos:
            if nome_arquivo in arquivo:
                try:
                    contador += 1
                    caminho_completo = os.path.join(raiz, arquivo)
                    # nomeArq, extArq = os.path.splitext(arquivo)

                    lb_resultado['text'] = caminho_completo
                except PermissionError as e:
                    print("você não tem permissão.")
                except FileNotFoundError as e:
                    print("arquivos não existe.")
                except Exception as e:
                    print("erro: ", e)

    print()
    cont = f'{contador} arquivo(s) encontra(s).'
    lb_cont['text'] = cont

win = Tk()
win.title('Buscador JUCEP')
win.geometry('600x300')
win.resizable(width=1, height=1)

txt_local_dir = Label(win, text='Coloque o caminha do diretorio: ')
et_dir = Entry(win)
txt_arquivo = Label(win, text='Digite o nome do arquivo: ')
et_arq = Entry(win)

txt_local_dir.grid(column=0, row=0 )
et_dir.grid(column=1, row=0)
txt_arquivo.grid(column=0, row=1 )
et_arq.grid(column=1, row=1 )

botao = Button(win, text='Busca o arquivo', command=OnClick)
botao.grid(column=0, row=2 )


lb_resultado = Label(win, text="resultado")
lb_resultado.grid(column=0, row=3 )
lb_cont = Label(win, text="quantidade")
lb_cont.grid(column=0, row=4 )

et_resporta = Entry(win)
et_resporta.grid(column=0, row=5 )
win.mainloop()
