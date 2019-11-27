from leitura import lerArquivos
import face_recognition
import cv2
import os

#definindo constantes
registradosFilePath = "/home/felipe/Área de Trabalho/face-recon/registrados/"
desconhecidoFilePath = "/home/felipe/Área de Trabalho/face-recon/desconhecido/"
listaDeNomes = lerArquivos.leitorDeNomes("{}".format(registradosFilePath))
listaDeArquivos = lerArquivos.leitorDeArquivos("{}".format(registradosFilePath))
lista = listaDeArquivos
url = 0

def efetuarCadastro(nome):
  camera = cv2.VideoCapture(url)
  print("Digite <ESC> para sair / <s> para Salvar")

  loop = True
  while loop:
    retorno, imagem = camera.read()
    cv2.imshow('Efetuando Cadastro', imagem)
    tecla = cv2.waitKey(100)

    #usuário aperta esc
    if tecla == 27:
      loop = False
    
    #usuario aperta s
    elif tecla == ord('s'):
      cv2.imwrite("{}{}.jpg".format(registradosFilePath, nome), imagem)
      loop = False

  try:
    imagemNovoCadastro = face_recognition.load_image_file("{}{}.jpg".format(registradosFilePath,nome))
    biodadoNovoCadastro = face_recognition.face_encodings(imagemNovoCadastro)[0]

  except IndexError:
    print("Não foi detectado rosto algum na imagem")
    os.remove("{}{}.jpg".format(registradosFilePath,nome))
    quit()

  cv2.destroyAllWindows()
  camera.release()

def capturarDesconhecido():
  camera = cv2.VideoCapture(url)
  print("Digite <ESC> para sair / <s> para Salvar")

  loop = True
  while loop:
    retorno, imagem = camera.read()
    cv2.imshow('Foto', imagem)
    tecla = cv2.waitKey(100)

    #usuário aperta esc
    if tecla == 27:
      loop = False
    
    #usuario aperta s
    elif tecla == ord('s'):
      cv2.imwrite("{}desconhecido.jpg".format(desconhecidoFilePath), imagem)
      loop = False

  cv2.destroyAllWindows()
  camera.release()

#preenche a lista de biodados conhecidos
def coletarBiodados():
  if len(lista) < 1:
    return "Erro: não há resistro algum no banco"

  if len(lista) <= 1:
      imagem = face_recognition.load_image_file("{}{}".format(registradosFilePath, lista[0]))
      biodadosConhecidos.append(face_recognition.face_encodings(imagem)[0])

      return biodadosConhecidos

  else:
      indice = lista.pop(0)
      imagem = face_recognition.load_image_file("{}{}".format(registradosFilePath, indice))
      biodadosConhecidos.append(face_recognition.face_encodings(imagem)[0])

  return coletarBiodados()

#verifica se algum rosto foi reconhecido e mostra o resultado
def verificarResultado(resultado):
  global indice
  indice = -1

  index = 0
  for i in resultado:
      for j in i:
          if j == True:
              indice = index
          index += 1

  if indice != -1:
      return listaDeNomes[indice]
    
  else:
    return "Não foi possível reconhecer nenhum rosto já registrado"

#inicializando variáveis e coletando o biodado da pessoa a ser reconhecida    
resultado = []
biodadosConhecidos = []
nomeDoReconhecido = ""
imagemNaoRegistrada = face_recognition.load_image_file("{}desconhecido.jpg".format(desconhecidoFilePath))
biodadoNaoConhecido = face_recognition.face_encodings(imagemNaoRegistrada)[0]

#preenche a lista biodados com os biodados
coletarBiodados()

for i in range(len(biodadosConhecidos)):
    resultado.append(face_recognition.compare_faces([biodadosConhecidos[i]], biodadoNaoConhecido, tolerance = 0.6))

#efetua a veriicação do resultado e printa ele
nomeDoReconhecido = verificarResultado(resultado)
print(nomeDoReconhecido)
