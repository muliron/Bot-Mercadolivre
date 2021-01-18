from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#LEIA O ARQUIVO "README"!!


nome_do_produto = input("Digite o produto que deseja encontrar: ")
full = input("Deseja utilizar a função full? (SIM/NÃO): ")
frete = input("Deseja filtrar por Frete Gratis? (SIM/NÃO): ")
menor_valor = input("Deseja filtrar por menor valor? (SIM/NÃO): ")

#Caminho necessario para encontrar o executável do Webdriver
caminho_driver = r"C:\Users\roberta\Downloads\Nova pasta\chromedriver"

#Carregando o Webdriver do navegador
driver = webdriver.Chrome(executable_path=caminho_driver)
driver.get("http://www.mercadolivre.com.br")
driver.maximize_window()
#Esperando a pagina carregar
time.sleep(4)
             
#Encontrando a barra de pesquisa e escrevendo o input do usuário.             
a = driver.find_element_by_xpath("/html/body/header/div/form/input")
a.send_keys(nome_do_produto)
a.send_keys(Keys.RETURN)

#Condicional checando se o usuário quer usar a função FULL do Mercadolivre.
try:
    if (full == "sim" or full == "SIM"):
        time.sleep(3)
        b = driver.find_element_by_xpath("/html/body/main/div/div[1]/aside/section[2]/dl[1]/div/dd/div[2]/a/span")
        b.click()
    else:
        pass
except:
       
    print("\nEstamos cientes do erro da função Full e vamos corrigi-lo o mais rapido possivel. Fique ligade no Git :)")

try:
    if (frete == "sim" or frete == "SIM"):
        time.sleep(5)
        e = driver.find_element_by_class_name("ui-search-filter-results-qty")
        time.sleep(6)
        e.click()
    else:
        pass
except:
    
    print("\nEstamos cientes do erro da função frete grátis e vamos corrigi-lo o mais rapido possivel. Fique ligade no Git :)")

try:
    if (menor_valor == "sim" or menor_valor == "SIM"):
        time.sleep(3)
        #
        c = driver.find_element_by_class_name("andes-dropdown__trigger")
        c.click()
        d = driver.find_element_by_xpath("/html/body/main/div/div[1]/aside/section[2]/div[2]/div[1]/div/div/div/ul/li[2]/a/div/div")
        d.click()
    else:
        pass
except:
    
    print("\nEstamos cientes do erro da função menor valor e vamos corrigi-lo o mais rapido possivel. Fique ligade no Git :)")







