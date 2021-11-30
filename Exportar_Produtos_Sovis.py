from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
from tkinter import *
from tkinter import ttk

#navegador = webdriver.Chrome()
options = Options()
options.add_argument('--headless')
navegador = webdriver.Chrome(executable_path='C:/chromedriver.exe', chrome_options=options)
#Endereço do servidor:porta de acesso
navegador.get("http://192.168.0.1:1122/")
email = "usuário"
senha = "senha"

def abrirExportar():
    #Procura o campo Email e digita o Email definido anteriormente
    navegador.find_element_by_xpath('//*[@id="user-login"]/div[3]/div[1]/div/input').send_keys(email)
    #Procura o campo senha e digita a senha definida anteriormente
    navegador.find_element_by_xpath('//*[@id="user-login"]/div[3]/div[2]/div/input').send_keys(senha)
    #Procura o botão Entrar e clica no mesmo
    navegador.find_element_by_xpath('//*[@id="user-login"]/button').click()

    time.sleep(5)

    try:
        navegador.find_element_by_xpath('/html/body/div[3]/header/nav/ul[1]/li/a').click()
        time.sleep(1)
        navegador.find_element_by_xpath('/html/body/div[3]/aside/div[2]/nav/ul/li[5]/a').click()
        time.sleep(1)
    except:
        #Procura o Menu Exportação e clica
        navegador.find_element_by_xpath('/html/body/div[3]/aside/div[2]/nav/ul/li[5]/a').click()
        time.sleep(1)

    #Dentro do menu Exportação procura o botão exportar e clica
    botaoPesquisar = navegador.find_element_by_xpath('/html/body/div[3]/aside/div[2]/nav/ul/li[5]/ul/li[2]/a').click()
    botaoPesquisar
    time.sleep(5)

abrirExportar()

#Exporta Tudo
def exportaTudo():
    navegador.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div/div/form/div/div[2]/button').click()
    time.sleep(60)

#Exporta apenas os clientes
def exportaCliente():
    #Clica no campo Pesquisar e pesquisa cliente
    navegador.refresh()
    time.sleep(4)
    try:
        navegador.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div/div/form/div/div[1]/input').send_keys('cliente')
        time.sleep(2)
    except:
        time.sleep(10)
        navegador.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div/div/form/div/div[1]/input').send_keys('cliente')
    #Envia CLIENTE
    navegador.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div/div/div/table/tbody/tr[1]/td[3]/button').click()
    time.sleep(10)
    texto_fim["text"] = "Envio CLIENTE completo."
    texto_fim2["text"] = "Progresso - 1/5"
    janela.update()
    #Envia ASSCLIENTEUSUARIO
    try:
        navegador.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div/div/div/table/tbody/tr[2]/td[3]/button').click()
        time.sleep(10)
    except:
        time.sleep(10)
    texto_fim["text"] = "Envio ASSCLIENTEUSUARIO completo."
    texto_fim2["text"] = "Progresso - 2/5"
    janela.update()
    #Envia SALDOCLIENTE
    try:
        navegador.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div/div/div/table/tbody/tr[3]/td[3]/button').click()
        time.sleep(10)
    except:
        time.sleep(10) 
    texto_fim["text"] = "Envio SALDOCLIENTE completo."
    texto_fim2["text"] = "Progresso - 3/5"
    janela.update()
    #Envia ASSPRAZOPAGTOCLIENTE
    try:
        navegador.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div/div/div/table/tbody/tr[4]/td[3]/button').click()
        time.sleep(10)
    except:
        time.sleep(10)
    texto_fim["text"] = "Envio ASSPRAZOPAGTOCLIENTE completo"
    texto_fim2["text"] = "Progresso - 4/5"
    janela.update()
    #Envia ASSFORMAPAGTOCLIENTE
    try:
        navegador.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div/div/div/table/tbody/tr[5]/td[3]/button').click()
        time.sleep(10)
    except:
        time.sleep(10)
    texto_fim["text"] = "Exportação concluida com sucesso."
    texto_fim2["text"] = "Progresso - 5/5"
    janela.update()


def exportaProduto():
    #Clica no campo Pesquisar e pesquisa produto
    navegador.refresh()
    time.sleep(4)
    try:
        navegador.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div/div/form/div/div[1]/input').send_keys('produto')
        time.sleep(2)
    except:
        time.sleep(10)
        navegador.find_element_by_xpath('/html/body/div[3]/main/section/div/div/div/div/form/div/div[1]/input').send_keys('produto')
    texto_fim["text"] = "Em processo de implantação."
    janela.update()
#Fechar tudo
def fechar():
    navegador.quit()


janela = Tk()
janela.geometry('250x100')
janela.title("Exporta Dados")

texto_titulo = Label(janela, text="Selecione a opção desejada")
texto_titulo.place(x=25, y=5, width=200, height=20)

botao = Button(janela, text="Clientes", command=exportaCliente)
botao.place(x=25, y=30, width=60, height=20)

botao2 = Button(janela, text="Produtos", command=exportaProduto)
botao2.place(x=90, y=30, width=60, height=20)

texto_fim = Label(janela, text="")
texto_fim.place(x=25, y=55, width=200, height=20)

texto_fim2 = Label(janela, text="")
texto_fim2.place(x=25, y=80, width=200, height=20)

janela.mainloop()




