import cv2
import os
import math
import xlsxwriter



def save_img_to_txt_plot(img_file):
        img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

        f = open(img_file.split('.')[0]+'_'+img_file.split('.')[1] + '.txt', "w")
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                f.write("{:3} ".format(img[i][j]))
            f.write('\n')
        f.close()


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

def get_dim(img):
    with open(img, 'r') as file:
        # Initialize counters
        num_lines = 0
        num_rows = 0

        # Iterate through each line in the file
        for line in file:
            # Count the number of lines
            num_lines += 1

            # Count the number of rows (assuming rows are separated by newline characters)
            if line.strip():
                num_rows += 1
    return num_lines, num_rows


def MAE(m1,m2,m,n):
    dif=0
    for (el1, el2) in zip(m1,m2):
        dif+=el1-el2
    return abs(dif/(m*n))


def MSE(m1,m2,m,n):
    dif=0
    for (el1, el2) in zip(m1,m2):
        dif+=(el1-el2)*(el1-el2)
    return dif/(m*n)


def RMSE(m1,m2,m,n):
    dif=0
    for (el1, el2) in zip(m1,m2):
        dif+=(el1-el2)*(el1-el2)
    return math.sqrt(dif)/(m*n)


def SNR(m1,m2,m,n):
    dif=0
    sum=0
    for (el1, el2) in zip(m1,m2):
        sum+=el1*el1
        dif+=(el1-el2)*(el1-el2)
    if(dif!=0):
        return sum/dif
    else:
        return "infinit"

def PSNR(m1,m2,m,n):
    dif=0
    for (el1, el2) in zip(m1,m2):
        dif+=(el1-el2)*(el1-el2)
    if (dif != 0):
        return 10*math.log10((255*255)/((math.sqrt(dif)/(m*n))*(math.sqrt(dif)/(m*n))))
    else:
        return "infinit"

if __name__=='__main__':



    path="C:\\Users\\Sergiu\\PycharmProjects\\CAV_laborator_4\\imgs_test"
    imgs=[f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for el in imgs:
        save_img_to_txt_plot('imgs_test/'+el)


    ## wordul a fost completat manual ruland pentru fiecare poza urmatoarea secventa de cod luand pereche bmp si jpeg/png/tiff
    # m, n = get_dim("imgs_test/16x9 test pattern_bmp.txt")
    # poza1=obtine_cod_sursa_int("imgs_test/tv test pattern 1920x1080_bmp.txt")
    # poza2=obtine_cod_sursa_int("imgs_test/tv test pattern 1920x1080_tiff.txt")
    # print(MAE(poza1,poza2,m,n))
    # print(MSE(poza1,poza2,m,n))
    # print(RMSE(poza1,poza2,m,n))
    # print(SNR(poza1,poza2,m,n))
    # print(PSNR(poza1,poza2,m,n))




    ## excelul a fost generat automat ruland urmatoarea secventa de cod

    imgs_txt=[k for k in imgs if ('.txt' in k and 'bmp' not in k)]
    bmps = [k for k in imgs if ('.txt' in k and 'bmp' in k)]

    imgs_txt_bmp = []

    for element in bmps:
        imgs_txt_bmp.append(element)
        imgs_txt_bmp.append(element)
        imgs_txt_bmp.append(element)
    workbook = xlsxwriter.Workbook('tema_cav.xlsx')
    worksheet = workbook.add_worksheet()
    row = 1
    for (i, j) in zip(imgs_txt_bmp, imgs_txt):
        lista=[]
        column=1

        m, n = get_dim("imgs_test/"+i)
        poza1 = obtine_cod_sursa_int("imgs_test/"+i)
        poza2 = obtine_cod_sursa_int("imgs_test/"+j)
        lista.append(j)
        lista.append(MAE(poza1, poza2, m, n))
        lista.append(MSE(poza1, poza2, m, n))
        lista.append(RMSE(poza1, poza2, m, n))
        lista.append(SNR(poza1, poza2, m, n))
        lista.append(PSNR(poza1, poza2, m, n))

        for element in lista:
            worksheet.write(row, column, element)
            column+=1

        row+=1

    workbook.close()


