from leitura import lerArquivos
import reconhece
import subprocess
import cv2
import face_recognition
import sys

url = 0
filePath = "/home/felipe/Área de Trabalho/face-recon/registrados"

def cabecalho():
  print("-"*30)
  print("É Tu? v 2.0")
  print("-"*30)
  print("")
  print("MENU DE OPÇÕES:\n  \n  1.Cadastrar Face\n  2.Reconhecer Face\n  3.Sair")

def cadastrar(nome):
  camera = cv2.VideoCapture(url)
  loop = True
  file = "{}/{}.jpg".format(filePath,nome)
         
  print("Digite <ESC> para sair / <s> para Salvar")   

  while(loop):
    retval, img = camera.read()
    cv2.imshow('Foto', img)     
    k = cv2.waitKey(100)
     
    if k == 27:      
      loop = False
         
    elif k == ord('s'):   
      cv2.imwrite(file,img)
      loop= False

  cv2.destroyAllWindows()
  camera.release()

  print("\nCadastro efetuado com sucesso.") 

def compararRosto():
  nFrames = 30
  camera = cv2.VideoCapture(url)
  loop = True
  global resultados, nomeDoReconhecido
  resultados = []
  nomeDoReconhecido = ""

  file = "/home/felipe/Área de Trabalho/face-recon/desconhecido/desconhecido.jpg"
          
  print("Digite <ESC> para sair / <s> para Salvar")   
  while(loop):
    retval, img = camera.read()
    cv2.imshow("Foto", img)      
    k = cv2.waitKey(100)
      
    if k == 27:        
      loop = False
          
    elif k == ord('s'):    
      cv2.imwrite(file,img)
      loop = False
  

  cv2.destroyAllWindows()
  camera.release()

  resultados = comparaRostos.coletaBiodados()
  nomeDoReconhecido = comparaRostos.verificaResultado(resultados)

  print(nomeDoReconhecido)

if __name__ == "__main__":
  opcao = 1
  while opcao != 3:
    cabecalho()
    opcao = int(input("\nInsira a opção desejada: "))

    if opcao == 1:
      nome = str(input("\nEstamos efetuando seu cadastro...\nInsira seu nome por favor: "))

      while nome == "":
        nome = str(input("\nInsira seu nome por favor: "))

      cadastrar(nome)
    
    elif opcao == 2:
      compararRosto()

    else:
      print("\nOpção inválida")