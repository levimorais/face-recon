import lerArquivos
import face_recognition

path = "/home/levi/dev/ap2/face-recon/registrados/"
imagensRegistradas = []
lista = []
resultado = []
biodadosConhecidos = []
foto = face_recognition.load_image_file("/home/levi/dev/ap2/face-recon/desconhecido/desconhecido.jpg")
biodadoNaoConhecido = face_recognition.face_encodings(foto)[0]

lista = lerArquivos.leitorDeArquivos("/home/levi/dev/ap2/face-recon/registrados/")

def preencheBiodados(tamanho):
    if len(lista) <= 1:
        x = face_recognition.load_image_file("{}{}".format(path, lista[0]))
        biodadosConhecidos.append(face_recognition.face_encodings(x)[0])

        return biodadosConhecidos

    else:
        indice = lista.pop(0)
        imagem = face_recognition.load_image_file("{}{}".format(path, indice))
        biodadosConhecidos.append(face_recognition.face_encodings(imagem)[0])

    return preencheBiodados(len(lista))

preencheBiodados(len(lista))

for i in range(len(biodadosConhecidos)):
    resultado.append(face_recognition.compare_faces([biodadosConhecidos[i]], biodadoNaoConhecido, tolerance=0.6))

print(resultado)
 
