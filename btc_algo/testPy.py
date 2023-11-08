from colorama import init, Fore, Back, Style

from ast import literal_eval




def new_sub_str(a , i ) :
    a = a[::-1]
    new_str = ""
    #print(a)
    a = a[::-1]
    first_string = ""
    for m in range(0,i):
        first_string+=a[m]

    theone_idx = None
    for j in range(i,len(a)):
        if (a[j] == "1") :
            if (theone_idx == None) :
                theone_idx = j

    # this for i elem it was 0 thats why i have this condition
    data = ""
    for k in range(i+1,theone_idx):
        #new_str += "1"
        data+="1"
    # this is for theone_idx item it used to be one but now it is a 0
    end_string = ""
    if (theone_idx != None) :
        l = theone_idx+1
        while l < len(a) :

            end_string+=a[l]
            l+= 1

    new_str = end_string[::-1]
    new_str += "0"
    new_str += data
    new_str += "1"
   
    new_str = new_str[::-1]
    new_str = first_string  + new_str
    return new_str

def BinSub(a,b) :
    res = ""
    if (len(b)>len(a)) :
        a,b = b,a 
    if (len(b) <= len(a)) :
        if (len(b)!= len(a)) :
            add_str = ""
            for k in range(len(a)-len(b)):
                add_str+="0"
            b =  add_str + b

        a = a[::-1]
        b = b[::-1]

        for i in range(0,len(a)) :
            #print("i   " + str(i)+"    " , (a) , b  , res   , end="\n")
            if (i <= len(b)-1 ) :
                if (a[i] == "1" and b[i] == "0" ):
                    res += "1"
                if (a[i] == "1" and b[i] == "1" ) :
                    res += "0"
                if (a[i] == "0" and b[i] == "0" ) :
                    res += "0"
                
                # borrowing condition
                if (a[i] == "0" and b[i] == "1" ) :
                    res += "1"
                   
                    new_a = new_sub_str(a , i )
                    #print(new_a[::-1], 'newa' , a[::-1] , b[::-1] )
                    new_b =  b

                    b = new_b
                    a = new_a
        
            #print(f"i   " +  str(i)+"    " , (a[0:i])+(Style.BRIGHT+ Fore.RED +str(a[i]))+a[i+1:] ,(b[0:i])+(Style.BRIGHT+ Fore.RED +str(b[i]))+b[i+1:]  , res, end="\n"

            init(autoreset=True)

    return res[::-1]

def binary_to_float(number) :
    return float(literal_eval("0b"+str(number)))

def deleteFirstZeros(binaryNum) :
    newBinaryNum = ""
    status = False
    for i in range(0,len(binaryNum)) :
        if (binaryNum[i] == "1") :
            status = True   
        if (status):
            newBinaryNum += binaryNum[i]

    return newBinaryNum 

def GetBiggerNumber (a,b,i) :
    if (len(a)< len(b)) : 
        return False
    else :

        Suba = a[i:len(b)]
        if binary_to_float(Suba) > binary_to_float(b):
            Suba = a[i:len(b)]
        else :
            if len(a) >= len(b)+1 : 
                Suba = a[i:len(b)+1]
            else :
                Suba = False 

        return Suba 

def FloorDevAndMod(a,b,restofSub) :

    a , b = deleteFirstZeros(a) , deleteFirstZeros(b)

    tempRestLen = len(restofSub)
    Rest = restofSub

    if binary_to_float(a) > binary_to_float(b):
        elem_tosubFrom = ""
        for i in range(0,len(a)):
            #print(a[i])
            elem_tosubFrom += a[i]
            #print("restofSub3   "+str(restofSub))
            length_Condition1 = ( len(elem_tosubFrom) == len(b) - (tempRestLen) )
            length_Condition2 = ( len(elem_tosubFrom) == len(b) +1  - (tempRestLen))
            length_Condition= ( length_Condition1 or length_Condition2) 

            if ( length_Condition ) :
                print(i) 
                print("restofSub  "+str(restofSub) + "  "+"elem_tosubFrom  "+str(elem_tosubFrom)) 

                #elem_tosubFrom  = elem_tosubFrom[::-1]
                elem_tosubFrom  = restofSub + elem_tosubFrom

                if ( binary_to_float(elem_tosubFrom) > binary_to_float(b)) :
                    print(Rest)
                    print("restofSub  "+str(Rest) + "  "+"elem_tosubFrom  "+str(elem_tosubFrom)) 
                    print("restofSub+elem_tosubFrom[::-1]  "+ str(elem_tosubFrom))

                    print("\n")

                    result_of_sub = deleteFirstZeros(BinSub(elem_tosubFrom,b))
                    new_a = a[len(elem_tosubFrom):]

                    # print("elem_tosubFrom  " +str(elem_tosubFrom) +"  - "+str(b)+"  =  "+str(result_of_sub))
                    #print("new_a   "+str(new_a))
                    FloorDevAndMod(new_a,b,result_of_sub)

    

    return 0 



"""

Binary value:
10101010 ÷ 1101
= 01101 Remainder : 1

Decimal value:
170 ÷ 13
= 13 Remainder : 1


"""
#a = "1110100010101011"
#b = "101"

a = "10101010"
b= "1101"
FloorDevAndMod = FloorDevAndMod(a,b,"")
#res = BinSub("11001111100000000000010110000011","10111010101110111","")
#print("res   " + str(res))

#FloorDevAndMod(a,b,"")

def addBinTemp(a,b):
    new_a = int(a,2)
    new_b = int(b,2)
    thesum  = new_a + new_b
    return bin(thesum)[2:]


def MultiplyBin(a,b):
    AddElemArr = []
    for i in range(0,len(b)):
        oneBit = b[i]
        if ( oneBit == "0" ):
            AddElem = (len(a)+i)*"0"
        if ( oneBit == "1" ):
            AddElem = a+(i)*"0"
        AddElemArr.append(AddElem)

    
    FinalBin = "0"
    for elem in AddElemArr :
        FinalBin = addBinTemp(elem,FinalBin)

    return FinalBin 


a = "11111000"
b = "1111"

#BinSub = BinSub(a,b)

#print("BinSub", BinSub)
print("FloorDevAndMod" , FloorDevAndMod)
print("MultiplyBin" , MultiplyBin(a,b) ) 
