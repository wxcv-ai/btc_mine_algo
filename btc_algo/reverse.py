
a = "1110100010101011"
b = "101"
print(a , b)
mod_res = "011"

def findPositionsOfbitInAnumber(NumberInBits , toSearchBit):
    array = []
    for i  in range(0,len(NumberInBits)) :
        bit = NumberInBits[i]
        if (bit == toSearchBit) :
            array.append(i)

    return array

def ReverseMod(mod_res,mod_by , lenght_of_origin) :

    i = 0 
    while i < lenght_of_origin :
        # this is to check if it can have straight from origin bits
        if (i < len(mod_res)) :
            print("possibility one is : "+"from origin "+str(i))
            print("possibility two is : "+"substraction result "+str(i))
            bit = mod_res[i]
            if (bit == "0") :
                zeros_idx = findPositionsOfbitInAnumber(mod_by , "0")
                ones_idx = findPositionsOfbitInAnumber(mod_by , "1")

                print("possibility two option 1 >>>  "+"original bit = 0 and mofby bit == 0  " ,zeros_idx )
                print("possibility two option 2 >>>  "+"original bit = 1 and mofby bit == 1  " , ones_idx )
                print("possibility two option 2 >>>  "+"original bit = 0 and mofby bit == 1 and original bit borowed a 1 in index  >  "+str(i) , "  " , ones_idx)
            if (bit == "1") :
                print("possibility two option 1 >>>  "+"original bit = 1 and mofby bit == 0  ",zeros_idx )
                print("possibility two option 2 >>>  "+"original bit = 0 and mofby bit == 1 and original bit borowed a 1 in index  >  "+str(i) , "  " , ones_idx)

            print("\n")
            print("\n")
            pass

        else :
            pass

        i+=1
    return 0 

ReverseMod(mod_res,b , len(a))
