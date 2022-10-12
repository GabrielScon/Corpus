#Aluno: Gabriel Sposito Conciani.

#Sua  tarefa  será  transformar  um  conjunto  de  5  sites,  sobre  o  tema  de  processamento  de 
#linguagem natural em um conjunto de cinco listas distintas de sentenças. Ou seja, você fará uma função 
#que, usando a biblioteca Beautifull Soap, faça a requisição de uma url, e extrai todas as sentenças desta 
#url. Duas condições são importantes:  

#a) A página web (url) deve apontar para uma página web em inglês contendo, não menos que 
#1000 palavras.  

#b) O texto desta página deverá ser transformado em um array de senteças.  
 
#Para separar as sentenças você pode usar os sinais de pontuação ou as funções da biblibioteca 
#Spacy. 

from bs4 import BeautifulSoup
import requests

url1 = "https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1"
url2 = "https://www.ibm.com/cloud/learn/natural-language-processing"
url3 = "https://en.wikipedia.org/wiki/Natural_language_processing"
url4 = "https://www.techtarget.com/searchenterpriseai/definition/natural-language-processing-NLP"
url5 = "https://www.datarobot.com/blog/what-is-natural-language-processing-introduction-to-nlp/"

html1 = requests.get(url1)
html2 = requests.get(url2)
html3 = requests.get(url3)
html4 = requests.get(url4)
html5 = requests.get(url5)

sp1 = BeautifulSoup(html1.text,"html.parser")
sp2 = BeautifulSoup(html2.text,"html.parser")
sp3 = BeautifulSoup(html3.text,"html.parser")
sp4 = BeautifulSoup(html4.text,"html.parser")
sp5 = BeautifulSoup(html5.text,"html.parser")

sentensas1=[]
sentensas2=[]
sentensas3=[]
sentensas4=[]
sentensas5=[]

for sentensas in sp1.find_all("p"):  
    sentensas1.append(sentensas.get_text())
for sentensas in sp2.find_all("p"):  
    sentensas2.append(sentensas.get_text())
for sentensas in sp3.find_all("p"):  
    sentensas3.append(sentensas.get_text())
for sentensas in sp4.find_all("p"):  
    sentensas4.append(sentensas.get_text())
for sentensas in sp5.find_all("p"):  
    sentensas5.append(sentensas.get_text())    

print(sentensas1)
print(" ")
print(sentensas2)
print(" ")
print(sentensas3)
print(" ")
print(sentensas4)
print(" ")
print(sentensas5)
print(" ")
