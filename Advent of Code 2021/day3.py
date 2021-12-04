numbs = open("day3.txt", "r")

data = []

for x in numbs:
    data.append(x.strip("\n"))

numbs.close()
#print(data)

def getBit(data):
    class Bits:
        length = 1000
        ValueBit1 = 0
        ValueBit2 = 0
        ValueBit3 = 0
        ValueBit4 = 0
        ValueBit5 = 0
        ValueBit6 = 0
        ValueBit7 = 0
        ValueBit8 = 0
        ValueBit9 = 0
        ValueBit10 = 0
        ValueBit11 = 0
        ValueBit12 = 0
    for x in data:
        Bits.ValueBit1 += int(x[0])
        Bits.ValueBit2 += int(x[1])
        Bits.ValueBit3 += int(x[2])
        Bits.ValueBit4 += int(x[3])
        Bits.ValueBit5 += int(x[4])
        Bits.ValueBit6 += int(x[5])
        Bits.ValueBit7 += int(x[6])
        Bits.ValueBit8 += int(x[7])
        Bits.ValueBit9 += int(x[8])
        Bits.ValueBit10 += int(x[9])
        Bits.ValueBit11 += int(x[10])
        Bits.ValueBit12 += int(x[11])

def getCO2Scrubber(ValueBit, data):

    CO2_ = []


    if ValueBit < 1000 / 2:
        for x in data:
            if int(x[0]) == 1:
                CO2_.append(x)
    else:
        for x in data:
            if int(x[0]) == 0:
                CO2_.append(x)
    ValueBit1 = 0
    CO2_Len = ""
    CO2_1 = []
    for x in CO2_:
        ValueBit1 += int(x[1])
        CO2_Len += x[1]
    if ValueBit1 < len(CO2_Len) / 2:
        for x in CO2_:
            if int(x[1]) == 1:
                CO2_1.append(x)
    else:
        for x in CO2_: 
            if int(x[1]) == 0:
                CO2_1.append(x)
    ValueBit2 = 0
    CO2_Len1 = ""
    CO2_2 = []
    for x in CO2_1:
        ValueBit2 += int(x[2])
        CO2_Len1 += x[2]
    if ValueBit2 < len(CO2_Len1) / 2:
        for x in CO2_1:
            if int(x[2]) == 1:
                CO2_2.append(x)
    else:
        for x in CO2_1: 
            if int(x[2]) == 0:
                CO2_2.append(x)
    ValueBit3 = 0
    CO2_Len2 = ""
    CO2_3 = []
    for x in CO2_2:
        ValueBit3 += int(x[3])
        CO2_Len2 += x[3]
    if ValueBit3 < len(CO2_Len2) / 2:
        for x in CO2_2:
            if int(x[3]) == 1:
                CO2_3.append(x)
    else:
        for x in CO2_2: 
            if int(x[3]) == 0:
                CO2_3.append(x)
    ValueBit4 = 0
    CO2_Len3 = ""
    CO2_4 = []
    for x in CO2_3:
        ValueBit4 += int(x[4])
        CO2_Len3 += x[4]
    if ValueBit4 < len(CO2_Len3) / 2:
        for x in CO2_3:
            if int(x[4]) == 1:
                CO2_4.append(x)
    else:
        for x in CO2_3: 
            if int(x[4]) == 0:
                CO2_4.append(x)
    ValueBit5 = 0
    CO2_Len4 = ""
    CO2_5 = []
    for x in CO2_4:
        ValueBit5 += int(x[5])
        CO2_Len4 += x[5]
    if ValueBit5 < len(CO2_Len4) / 2:
        for x in CO2_4:
            if int(x[5]) == 1:
                CO2_5.append(x)
    else:
        for x in CO2_4: 
            if int(x[5]) == 0:
                CO2_5.append(x)
    ValueBit6 = 0
    CO2_Len5 = ""
    CO2_6 = []
    for x in CO2_5:
        ValueBit6 += int(x[6])
        CO2_Len5 += x[6]
    if ValueBit6 < len(CO2_Len5) / 2:
        for x in CO2_5:
            if int(x[6]) == 1:
                CO2_6.append(x)
    else:
        for x in CO2_5: 
            if int(x[6]) == 0:
                CO2_6.append(x)
    ValueBit7 = 0
    CO2_Len6 = ""
    CO2_7 = []
    for x in CO2_6:
        ValueBit7 += int(x[7])
        CO2_Len6 += x[7]
    if ValueBit7 < len(CO2_Len6) / 2:
        for x in CO2_6:
            if int(x[7]) == 1:
                CO2_7.append(x)
    else:
        for x in CO2_6: 
            if int(x[7]) == 0:
                CO2_7.append(x)
    ValueBit8 = 0
    CO2_Len7 = ""
    CO2_8 = []
    for x in CO2_7:
        ValueBit8 += int(x[8])
        CO2_Len7 += x[8]
    if ValueBit8 < len(CO2_Len7) / 2:
        for x in CO2_7:
            if int(x[8]) == 1:
                CO2_8.append(x)
    else:
        for x in CO2_7: 
            if int(x[8]) == 0:
                CO2_8.append(x)
    print(CO2_7)


def getOxygenGenerator(ValueBit, data):
    Oxy = []

    if ValueBit >= 1000 / 2:
        for x in data:
            if int(x[0]) == 1:
                Oxy.append(x)
    else:
        for x in data:
            if int(x[0]) == 0:
                Oxy.append(x)
    
    ValueBit1 = 0
    OxyLen = ""
    Oxy1 = []
    for x in Oxy:
        ValueBit1 += int(x[1])
        OxyLen += x[1]
    if ValueBit1 >= len(OxyLen) / 2:
        for x in Oxy:
            if int(x[1]) == 1:
                Oxy1.append(x)
    else:
        for x in Oxy: 
            if int(x[1]) == 0:
                Oxy1.append(x)
    ValueBit2 = 0
    OxyLen1 = ""
    Oxy2 = []
    for x in Oxy1:
        ValueBit2 += int(x[2])
        OxyLen1 += x[2]
    if ValueBit2 >= len(OxyLen1) / 2:
        for x in Oxy1:
            if int(x[2]) == 1:
                Oxy2.append(x)
    else:
        for x in Oxy1: 
            if int(x[2]) == 0:
                Oxy2.append(x)
    ValueBit3 = 0
    OxyLen2 = ""
    Oxy3 = []
    for x in Oxy2:
        ValueBit3 += int(x[3])
        OxyLen2 += x[3]
    if ValueBit3 >= len(OxyLen2) / 2:
        for x in Oxy2:
            if int(x[3]) == 1:
                Oxy3.append(x)
    else:
        for x in Oxy2: 
            if int(x[3]) == 0:
                Oxy3.append(x)
    ValueBit4 = 0
    OxyLen3 = ""
    Oxy4 = []
    for x in Oxy3:
        ValueBit4 += int(x[4])
        OxyLen3 += x[4]
    if ValueBit4 >= len(OxyLen3) / 2:
        for x in Oxy3:
            if int(x[4]) == 1:
                Oxy4.append(x)
    else:
        for x in Oxy3: 
            if int(x[4]) == 0:
                Oxy4.append(x)
    ValueBit5 = 0
    OxyLen4 = ""
    Oxy5 = []
    for x in Oxy4:
        ValueBit5 += int(x[5])
        OxyLen4 += x[5]
    if ValueBit5 >= len(OxyLen4) / 2:
        for x in Oxy4:
            if int(x[5]) == 1:
                Oxy5.append(x)
    else:
        for x in Oxy4: 
            if int(x[5]) == 0:
                Oxy5.append(x)
    ValueBit6 = 0
    OxyLen5 = ""
    Oxy6 = []
    for x in Oxy5:
        ValueBit6 += int(x[6])
        OxyLen5 += x[6]
    if ValueBit6 >= len(OxyLen5) / 2:
        for x in Oxy5:
            if int(x[6]) == 1:
                Oxy6.append(x)
    else:
        for x in Oxy5: 
            if int(x[6]) == 0:
                Oxy6.append(x)
    ValueBit7 = 0
    OxyLen6 = ""
    Oxy7 = []
    for x in Oxy6:
        ValueBit7 += int(x[7])
        OxyLen6 += x[7]
    if ValueBit7 >= len(OxyLen6) / 2:
        for x in Oxy6:
            if int(x[7]) == 1:
                Oxy7.append(x)
    else:
        for x in Oxy6: 
            if int(x[7]) == 0:
                Oxy7.append(x)
    ValueBit8 = 0
    OxyLen7 = ""
    Oxy8 = []
    for x in Oxy7:
        ValueBit8 += int(x[8])
        OxyLen7 += x[8]
    if ValueBit8 >= len(OxyLen7) / 2:
        for x in Oxy7:
            if int(x[8]) == 1:
                Oxy8.append(x)
    else:
        for x in Oxy7: 
            if int(x[8]) == 0:
                Oxy8.append(x)
    ValueBit9 = 0
    OxyLen8 = ""
    Oxy9 = []
    for x in Oxy8:
        ValueBit9 += int(x[9])
        OxyLen8 += x[9]
    if ValueBit9 >= len(OxyLen8) / 2:
        for x in Oxy8:
            if int(x[9]) == 1:
                Oxy9.append(x)
    else:
        for x in Oxy8: 
            if int(x[9]) == 0:
                Oxy9.append(x)
    ValueBit10 = 0
    OxyLen9 = ""
    Oxy10 = []
    for x in Oxy9:
        ValueBit10 += int(x[10])
        OxyLen9 += x[10]
    if ValueBit10 >= len(OxyLen9) / 2:
        for x in Oxy9:
            if int(x[10]) == 1:
                Oxy10.append(x)
    else:
        for x in Oxy9: 
            if int(x[10]) == 0:
                Oxy10.append(x)
    ValueBit11 = 0
    OxyLen10 = ""
    Oxy11 = []
    for x in Oxy10:
        ValueBit11 += int(x[11])
        OxyLen10 += x[11]
    if ValueBit11 >= len(OxyLen10) / 2:
        for x in Oxy10:
            if int(x[11]) == 1:
                Oxy11.append(x)
    else:
        for x in Oxy10: 
            if int(x[11]) == 0:
                Oxy11.append(x)
    
    
    print(ValueBit11, Oxy11)

    




def getGammaEpsilon(Bits):
    Gamma = ""
    Epsilon = ""
    if Bits.ValueBit1 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit2 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit3 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit4 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit5 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit6 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit7 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit8 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit9 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit10 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit11 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"
    if Bits.ValueBit12 > Bits.length / 2:
        Gamma += "1"
        Epsilon += "0"
    else: 
        Gamma += "0"
        Epsilon += "1"

    print(Gamma, Epsilon)

Bit = 0

for x in data:
    Bit += int(x[0])
print(Bit)

getOxygenGenerator(Bit, data)
getCO2Scrubber(Bit, data)

#getGammaEpsilon(Bits)

#getBits(data)
