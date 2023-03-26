
def scale(value, r_min, r_max, t_min, t_max):
    new_value = int((value - r_min)/(r_max - r_min)*(t_max - t_min) + t_min)
    return new_value


def cuantizare(msg, bits_actual, bits):
    new_msg = list()

    for el in msg:
        new_msg.append(str(scale(value=int(el), r_min=0, r_max=2**bits_actual-1, t_min=0, t_max=2**bits-1)))

    return new_msg


def byte_to_bit(msg_input):
     # cream o noua lista
    new_sursa = list()
    # tranformam din string in int toate valorile
    for el in msg_input:
        if el != "":
            for ch in el:
                new_sursa.append(ch)

    return new_sursa

def decodor_predictie_reversibila_diff(msg_input, scalar=False, bits=10, debug=False):
    new_msg = []

    if debug:
        print("Msg intrare:\n", msg_input)

    for el in msg_input:

        if len(new_msg) == 0:
            new_msg.append(el)
        else:
            new_el = int(new_msg[-1]) + int(el)
            new_msg.append(str(new_el))
    if debug:
        print("Eroare nescalata:\n", new_msg)

    if scalar:
        for el in range(len(new_msg)):
            new_msg[el] = str(
                scale(value=int(new_msg[el]), r_max=2 ** (bits) - 1, r_min=0 - (2 ** (bits) - 1), t_min=0, t_max=2 ** (bits + 1)))
        if debug:
            print("Eroare :\n", new_msg)

    return new_msg


def codor_predictie_reversibila_diff(msg_input, scalar=False, bits=10, debug=False):
    new_msg = []

    if debug:
        print("Msg intrare:\n", msg_input)
    tmp = '0'
    for el in msg_input:

        if len(new_msg) == 0:
            new_msg.append(el)
        else:
            new_msg.append(str(int(tmp) - int(el)))
        tmp = el
    if debug:
        print("Eroare nescalata:\n", new_msg)

    if scalar:
        for el in range(len(new_msg)):
            new_msg[el] = str(scale(value=int(new_msg[el]), r_max=2**(bits)-1, r_min=0-(2**(bits)-1), t_min=0, t_max=2**(bits+1)))
        if debug:
            print("Eroare :\n", new_msg)

    return new_msg



def save_img(information, size, name):
    import os, sys

    t = os.getcwd()

    f = open( t + '/' + name + ".txt", "w")

    for i in range(len(information)):
        if i%size == 0 and i!=0:
                f.write("\n")

        f.write("{:3} ".format(information[i]))
    f.close()