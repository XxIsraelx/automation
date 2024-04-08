from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import PySimpleGUI as sg
from time import sleep


#criar janela que peça ao usuario seu login
layout = [
    [sg.Text('Digite seu CPF:'), sg.InputText(key='-CPF-')],
    [sg.Text('Digite sua senha:'), sg.InputText(key='-Senha-', password_char='*')],
    [sg.Button('Enviar')]
]

window = sg.Window('Login', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Enviar':
        cpf = values['-CPF-']
        senha_login = values['-Senha-']
        window.close()

window.close()

#acessar site
driver = webdriver.Chrome()
driver.get('https://web.ciee.org.br/login')
sleep(5)

#adicionar CPF
acessar = driver.find_element(By.XPATH,"//input[@id='acesso-input']")
acessar.send_keys(cpf)
sleep(2)

#clicar botao proximo
botao_proximo = driver.find_element(By.XPATH,"//button[@class='btn btn-lg btn-ciee-login-empresa-backoffice']")
botao_proximo.click()

#esperar até que a senha seja visível
wait = WebDriverWait(driver, 10)
senha = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='senha-input']")))

#adicionar senha
senha.send_keys(senha_login)
sleep(2)

#clicar botao acessar
botao_acessar = driver.find_element(By.XPATH,"//button[@class='btn-ciee-login-estudante btn btn-lg btn-block clicavel']")
botao_acessar.click()
sleep(20)