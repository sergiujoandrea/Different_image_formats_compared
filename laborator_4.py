from CAV_laborator_4.predictie import codor_predictie_reversibila_diff, decodor_predictie_reversibila_diff, cuantizare, save_img
from CAV_laborator_4.huffman import codare_huffman, decodare_msg_codare_huffman
from CAV_laborator_4.helper import obtine_cod_sursa_lista_chr,obtine_cod_sursa_str


def calcul_lungime_medie(A, C):
    L = 0

    for el in A.keys():
        L += A[el] * C[el]
    # TODO: calculati lungimea medie

    return L


def calcul_entropie(A):
    import math

    H = 0
    # TODO: calculati entropia
    for el in A.keys():
        H += A[el] * math.log2(A[el])

    H = -H

    return H


def calcul_randament(L, H):
    n = 0
    # TODO: calculati randamentul
    return H/L


def rata_de_compresie(dim_compress, dim_org):
    rc = 0
    # TODO: calculati rata de compresie
    rc = dim_compress/dim_org
    return rc


def factor_salvare(dim_compress, dim_org):
    rc = 0
    # TODO: calculati rata de compresie
    rc = (dim_org - dim_compress)/dim_org
    return rc


def obtinere_alfabet_sursa(cod_sursa):
    # print("Codul codului: \n", cod_sursa)
    # print("Dimensiunea codului in biti: \n", len(cod_sursa) * 8)
    # obtinem alfabetul sursei
    alfabet_cod = list(set(cod_sursa))
    print("Alfabetul codului: \n", alfabet_cod)
    # cream un dictionarul pentru alfabetul A
    A = dict()
    for el in alfabet_cod:
        A[el] = cod_sursa.count(el)/len(cod_sursa)
    # sortam dictionarul
    A = dict(sorted(A.items(), key=lambda x: x[1], reverse=True))
    # print("A:\n", A)
    # verificam ca A este creat corect
    # assert sum(A.values()) >= 1, "Alfabetul codului nu este corect generat: {}".format(sum(A.values()))

    return A


def codam_huffman_caracter(locatie):
    print("\nCodam folosind codul Huffman fiecare bit:")
    msg_input = obtine_cod_sursa_lista_chr(locatie)
    dim_orginal = len(msg_input) * 10
    # print("Mesaj intrare: \n", msg_input)
    print("Dimensiunea codului in biti: \n", dim_orginal)

    # Codul Huffman pentru comparatie
    # obtineam alafebetul
    A_msg = obtinere_alfabet_sursa(msg_input)
    # print("Alfabetul mesajului, A= :\n", A_msg)
    # Codarea cu Huffman
    cod_huf, C_huf, msg_huf = codare_huffman(alfabet=A_msg.copy(), msg=msg_input)
    dim_codat = len(msg_huf)
    # print("Cod mesajului:\n", cod_huf)
    # print("Alfabetul codului, C=:\n", C_huf)
    # print("Mesaj codat cu lungime variabila B:\n", msg_SF)
    print("Dimensiune mesaj codat cu Huffman cu fiecare bit:\n", dim_codat)
    # Calculam Lungimea medie
    L_SF = calcul_lungime_medie(A=A_msg, C=C_huf)
    print("L_huff_bit = ", L_SF)
    # Calculam Entropia
    H = calcul_entropie(A=A_msg)
    print("H_huff_bit = ", H)
    # Calculam randamentul
    n = calcul_randament(L=L_SF, H=H)
    print("n_huff_bit = ", n)
    # Testam codarea
    new_msg = decodare_msg_codare_huffman(msg=msg_huf, cod=cod_huf, debug=False)
    assert msg_input == new_msg, "Mesajul decodat nu este identic cu cel codat!"
    # Calculati rata de compresie
    rc = rata_de_compresie(dim_compress=dim_codat, dim_org=dim_orginal)
    print("rc_huff_bit = ", rc)
    # Calculati factorul de salvare
    fs = factor_salvare(dim_compress=dim_codat, dim_org=dim_orginal)
    print("fs_huff_bit = ", fs)

def codam_huffman_byte(locatie):
    print("\nCodam folosind codul Huffman fiecare byte:")
    msg_input = obtine_cod_sursa_str(locatie)
    dim_orginal = len(msg_input) * 10
    # print("Mesaj intrare: \n", msg_input)
    print("Dimensiunea codului in biti: \n", dim_orginal)

    # Codul Huffman pentru comparatie
    # obtineam alafebetul
    A_msg = obtinere_alfabet_sursa(msg_input)
    # print("Alfabetul mesajului, A= :\n", A_msg)
    # Codarea cu Huffman
    cod_huf, C_huf, msg_huf = codare_huffman(alfabet=A_msg.copy(), msg=msg_input)
    dim_codat = len(msg_huf)
    # print("Cod mesajului:\n", cod_huf)
    # print("Alfabetul codului, C=:\n", C_huf)
    # print("Mesaj codat cu lungime variabila B:\n", msg_SF)
    print("Dimensiune mesaj codat cu Huffman fiecare byte:\n", dim_codat)
    # Calculam Lungimea medie
    L_SF = calcul_lungime_medie(A=A_msg, C=C_huf)
    print("L_huff_byte = ", L_SF)
    # Calculam Entropia
    H = calcul_entropie(A=A_msg)
    print("H_huff_byte = ", H)
    # Calculam randamentul
    n = calcul_randament(L=L_SF, H=H)
    print("n_huff_byte = ", n)
    # Testam codarea
    new_msg = decodare_msg_codare_huffman(msg=msg_huf, cod=cod_huf, debug=False)
    # assert msg_input == new_msg, "Mesajul decodat nu este identic cu cel codat!"
    # Calculati rata de compresie
    rc = rata_de_compresie(dim_compress=dim_codat, dicodam_huffman_caracterm_org=dim_orginal)
    print("rc_huff_byte = ", rc)
    # Calculati factorul de salvare
    fs = factor_salvare(dim_compress=dim_codat, dim_org=dim_orginal)
    print("fs_huff_byte = ", fs)


def codare_predictie_reversibil_byte(locatie):
    msg_input = obtine_cod_sursa_str(locatie)
    dim_orginal = len(msg_input) * 10
    # print("Mesaj intrare: \n", msg_input)
    print("Dimensiunea codului in biti: \n", dim_orginal)

    # Codul cu preditie reversibil, diferenta fata de caracterul anterior pentru comparatie
    msg_codat = codor_predictie_reversibila_diff(msg_input=msg_input)
    # print("Mesaj codat cu lungime variabila B:\n", msg_codat)
    print("Dimensiune mesaj codat cu predictie reversibila:\n", dim_orginal)

    # Codam eroare Huffman
    # obtineam alafebetul
    A_msg = obtinere_alfabet_sursa(msg_codat)
    print("Alfabetul mesajului, A= :\n", A_msg)
    # Codarea cu Huffman
    cod_huf, C_huf, msg_huf = codare_huffman(alfabet=A_msg.copy(), msg=msg_codat)
    dim_codat = len(msg_huf)
    print("Cod mesajului:\n", cod_huf)
    print("Alfabetul codului, C=:\n", C_huf)
    # print("Mesaj codat cu lungime variabila B:\n", msg_SF)
    print("Dimensiune mesaj codat cu Huffman:\n", dim_codat)

    # Calculam Lungimea medie
    L_SF = calcul_lungime_medie(A=A_msg, C=C_huf)
    print("L_huff = ", L_SF)
    # Calculam Entropia
    H = calcul_entropie(A=A_msg)
    print("H_huff = ", H)
    # Calculam randamentul
    n = calcul_randament(L=L_SF, H=H)
    print("n_huff = ", n)
    # Calculati rata de compresie
    rc = rata_de_compresie(dim_compress=dim_codat, dim_org=dim_orginal)
    print("rc_huff = ", rc)
    # Calculati factorul de salvare
    fs = factor_salvare(dim_compress=dim_codat, dim_org=dim_orginal)
    print("fs_huff = ", fs)

    # Testam codarea
    new_msg = decodare_msg_codare_huffman(msg=msg_huf, cod=cod_huf, debug=False)
    assert msg_codat == new_msg, "Mesajul decodat nu este identic cu cel codat!"
    # Testam codarea cu predictie
    new_msg = decodor_predictie_reversibila_diff(msg_input=new_msg)
    save_img(information=new_msg, size=512, name='Lenna_10bit_reconstruct')



def codare_predictie_nereversibil_byte(locatie):
    msg_input = obtine_cod_sursa_str(locatie)
    dim_orginal = len(msg_input) * 10
    # print("Mesaj intrare: \n", msg_input)
    print("Dimensiunea codului in biti: \n", dim_orginal)
    # cuantizam informatia pe 8biti
    msg_input = cuantizare(msg=msg_input, bits_actual=10, bits=8)
    # Codul cu preditie reversibil, diferenta fata de caracterul anterior pentru comparatie
    msg_codat = codor_predictie_reversibila_diff(msg_input=msg_input)
    # print("Mesaj codat cu lungime variabila B:\n", msg_codat)
    print("Dimensiune mesaj codat cu predictie reversibila:\n", len(msg_codat) * 8)

    # Codul Huffman pentru comparatie
    # obtineam alafebetul
    A_msg = obtinere_alfabet_sursa(msg_codat)
    print("Alfabetul mesajului, A= :\n", A_msg)
    # Codarea cu Huffman
    cod_huf, C_huf, msg_huf = codare_huffman(alfabet=A_msg.copy(), msg=msg_codat)
    dim_codat = len(msg_huf)
    print("Cod mesajului:\n", cod_huf)
    print("Alfabetul codului, C=:\n", C_huf)
    # print("Mesaj codat cu lungime variabila B:\n", msg_SF)
    print("Dimensiune mesaj codat cu Huffman:\n", dim_codat)

    # Calculam Lungimea medie
    L_SF = calcul_lungime_medie(A=A_msg, C=C_huf)
    print("L_huff = ", L_SF)
    # Calculam Entropia
    H = calcul_entropie(A=A_msg)
    print("H_huff = ", H)
    # Calculam randamentul
    n = calcul_randament(L=L_SF, H=H)
    print("n_huff = ", n)
    # Calculati rata de compresie
    rc = rata_de_compresie(dim_compress=dim_codat, dim_org=dim_orginal)
    print("rc_huff = ", rc)
    # Calculati factorul de salvare
    fs = factor_salvare(dim_compress=dim_codat, dim_org=dim_orginal)
    print("fs_huff = ", fs)

    # Testam codarea Huffman
    new_msg = decodare_msg_codare_huffman(msg=msg_huf, cod=cod_huf, debug=False)
    assert msg_codat == new_msg, "Mesajul decodat nu este identic cu cel codat!"
    # Testam codarea cu predictie
    new_msg = decodor_predictie_reversibila_diff(msg_input=new_msg)
    save_img(information=new_msg, size=512, name='Lenna_8bit_reconstruct')



if __name__=='__main__':
    poza = 'img/Lenna_10_bits_512.txt'

    codam_huffman_byte(locatie=poza)
    codam_huffman_caracter(locatie=poza)

    codare_predictie_reversibil_byte(poza)
    codare_predictie_nereversibil_byte(poza)

