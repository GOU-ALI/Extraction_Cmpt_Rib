
def conversion_Rib_to_compte(rib):
    if len(rib) == 24 :                                       # le rib est tjr en 24 caracteres

        agence = rib[8:12]
        serie = rib[13:22]
        A = rib[6:8]
        M = agence[0]
        #L = agence
        N = agence[1:]
        O = M
        Q = N
        #R = serie
        S = serie[0:3]
        P = S
        T = serie[3:]
        U = T
        V = O + P
        J = 13
        K = 16

        if V == "0000":
            W = 11
        else : W = 15

        if A =="00":
            X = "MAD"
        else : X = "DEV"

        if X == "MAD":
            Y = A
        else : Y = Q

        if X == "MAD":
            Z = Q
        else : Z = A

        AA = U
        AB = V
        AC = Y + Z + AA + AB
        AD = int(AC[0])*(J-1)
        AE = int(AC[1])*(J-2) + AD
        AF = int(AC[2])*(J-3) + AE
        AG = int(AC[3])*(J-4) + AF
        AH = int(AC[4])*(J-5) + AG
        AI = int(AC[5])*(J-6) + AH
        AJ = int(AC[6])*(J-7) + AI
        AK = int(AC[7])*(J-8) + AJ
        AL = int(AC[8])*(J-9) + AK
        AM = int(AC[9])*(J-10) + AL
        AN = int(AC[10])*(J-11) + AM

        AO = 0
        AP = 0
        AQ = 0
        AR = 0
        if W == 11 :
            AO = AN
            AP = AO
            AQ = AP
            AR = AQ
        else :
            AO = int(AC[11])*(K-12) + AN
            AP = int(AC[12])*(K-13) + AO
            AQ = int(AC[13])*(K-14) + AP
            AR = int(AC[14])*(K-15) + AQ

        AS = AR
        AT = AS % 11
        AU = 11 - AT

        if AU == 1 : cle = "A"
        elif AU == 2 : cle = "B"
        elif AU == 3 : cle = "C"
        elif AU == 4 : cle = "D"
        elif AU == 5 : cle = "E"
        elif AU == 6 : cle = "V"
        elif AU == 7 : cle = "N"
        elif AU == 8 : cle = "H"
        elif AU == 9 : cle = "R"
        elif AU == 10 : cle = "X"
        elif AU == 11 : cle = "S"
        else : "NOT FOUND"

        final = A + agence + cle + serie

    else :
        return "LE CODE RIB EST INCORRECT"

    return final

