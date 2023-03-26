import cv2
# import matplotlib.pyplot as plt
# import numpy as np

def save_img_to_txt_plot(img_file, resize_dim):

    img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

    img = cv2.resize(img, resize_dim)

    f = open("img/Lenna_{}.txt".format(resize_dim[0]), "w")

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            f.write("{:3} ".format(img[i][j]))
        f.write('\n')
    f.close()

    imgplot = plt.imshow(img, cmap='gray')

    plt.savefig('img\plot_Lenna_{}.jpg'.format(resize_dim[0]))
    plt.show()


def obtine_cod_sursa_int(fisier):
    # citim codul sursa din fisier
    sursa = open(fisier, "r").read()
    # eliminam end of line character
    sursa = sursa.replace('\n','')
    sursa = sursa.replace('  ',' ')
    # facem split la fiecare spatiu
    sursa = sursa.split(" ")
    # cream o noua lista
    new_sursa = list()
    # tranformam din string in int toate valorile
    for el in sursa:
        if el != "":
            new_sursa.append(int(el))

    return new_sursa


def obtine_cod_sursa_str(fisier):
    # citim codul sursa din fisier
    sursa = open(fisier, "r").read()
    # eliminam end of line character
    sursa = sursa.replace('\n','')
    sursa = sursa.replace('  ',' ')
    # facem split la fiecare spatiu
    sursa = sursa.split(" ")
    # cream o noua lista
    new_sursa = list()
    # tranformam din string in int toate valorile
    for el in sursa:
        if el != "":
            new_sursa.append((el))

    return new_sursa


def obtine_cod_sursa_lista_chr(fisier):
    # citim codul sursa din fisier
    sursa = open(fisier, "r").read()
    # eliminam end of line character
    sursa = sursa.replace('\n','')
    sursa = sursa.replace('  ',' ')
     # cream o noua lista
    new_sursa = list()
    # tranformam din string in int toate valorile
    for el in sursa:
        if el != "":
            new_sursa.append((el))

    return new_sursa


def codare_lungime_variabila_b(cod_sursa, alfabet_sursa, debug=False):
    # obtinem lista cu cuvinte din alfabet
    lista_cuvinte = list(alfabet_sursa.keys())
    # cream un dictionar pt a stoca codul
    cod = dict()
    # cream codul B
    for el in range(len(alfabet_sursa)):
        cod[lista_cuvinte[el]] = el * '0' + '1'
    if debug:
        print("cod:\n", cod)
    # cream C
    C = dict()
    for el in cod:
        C[el] = len(cod[el])
    if debug:
        print("C:\n", C)
    # codam mesajul
    msg_codat = ""
    for ch in cod_sursa:
        msg_codat += cod[ch]
    if debug:
        print("Mesaj codat cu lungime variabila B:\n", msg_codat)
        print("Dimensiune mesaj codat cu lungime variabila B:\n", len(msg_codat))

    return cod, C, msg_codat


def decodare_msg_codare_lungime_variabila_b(msg, cod, debug=False):
    new_msg = ""
    if debug:
        # print('Mesaj receptionat', msg)
        print('Cod receptionat: \n', cod)

    cuvant = ""
    for ch in msg:
        if ch == '1':
            cuvant += ch
            value = [i for i in cod if cod[i] == cuvant]
            new_msg += value[0]
            cuvant = ""
        else:
            cuvant += ch

    if debug:
        print('Mesaj decodat: \n', new_msg)



    return new_msg


def obtine_cod_sursa_numpy(fisier):
    # img = cv2.imread(fisier, cv2.IMREAD_GRAYSCALE)
    # np.save('img/Lenna_256', img)
    tmp = np.load(fisier)
    return tmp


if __name__=="__main__":
    save_img_to_txt_plot(img_file="img/Lenna_256.png", resize_dim=(256, 256))
    save_img_to_txt_plot(img_file="img/Lenna_256.png", resize_dim=(100, 100))
    save_img_to_txt_plot(img_file="img/Lenna_256.png", resize_dim=(30, 30))
