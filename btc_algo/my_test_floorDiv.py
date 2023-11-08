
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
    final_index = 0 
    for i in range(0,len(binaryNum)) :
        final_index = i 

        if (binaryNum[i] == "1") :
            status = True   
        if (status):
            newBinaryNum += binaryNum[i]
        
    final_index= final_index+1

    return [newBinaryNum , len(binaryNum) - len(newBinaryNum)  ]

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

def FloorDevAndMod2(a,b,restofSub) :

    #a ,a_zeros,b, b_zeros = deleteFirstZeros(a)[0] ,deleteFirstZeros(a)[1] ,deleteFirstZeros(b)[0] , deleteFirstZeros(b)[1]

    tempRestLen = len(restofSub)
    Rest = restofSub

    if binary_to_float(a) > binary_to_float(b):
        elem_tosubFrom = restofSub
        for i in range(0,len(a)):
            #print(a[i])
            elem_tosubFrom += a[i]
            #print("restofSub3   "+str(restofSub))
            length_Condition1 = ( len(elem_tosubFrom) == len(b) - (tempRestLen) )
            length_Condition2 = ( len(elem_tosubFrom) == len(b) +1  - (tempRestLen))
            length_Condition3 = ( len(elem_tosubFrom) >= len(b) )
            length_Condition= ( length_Condition1 or length_Condition2 or length_Condition3) 

            if ( length_Condition ) :
                #old_elem_tosubFrom = elem_tosubFrom
                #elem_tosubFrom = a_zeros*"0"+elem_tosubFrom
                #elem_tosubFrom  = elem_tosubFrom[::-1]
                #elem_tosubFrom  = restofSub + elem_tosubFrom

                if ( binary_to_float(elem_tosubFrom) >= binary_to_float(b)) :


                    result_of_sub = deleteFirstZeros(BinSub(elem_tosubFrom,b))[0]
                    #result_of_sub = (BinSub(elem_tosubFrom,b))
                    new_a = a[len(elem_tosubFrom)-len(restofSub):]

                    print("equation  " +str(elem_tosubFrom) +"  - "+str(b)+"  =  "+str(result_of_sub))
                    print(a, "new_a   "+str(new_a) , "a_ze")
                    print("\n")

                    FloorDevAndMod(new_a,b,result_of_sub)

    

    return 0 


def FloorDevAndMod(a,b,restofSub) :

    #a ,a_zeros,b, b_zeros = deleteFirstZeros(a)[0] ,deleteFirstZeros(a)[1] ,deleteFirstZeros(b)[0] , deleteFirstZeros(b)[1]

    tempRestLen = len(restofSub)
    Rest = restofSub

    final_rest = "-1"
    i = 0
    if binary_to_float(a) > binary_to_float(b):
        elem_tosubFrom = restofSub
        while i < len(a) :
           
            elem_tosubFrom += a[i]
            #print("restofSub3   "+str(restofSub))
            length_Condition1 = ( len(elem_tosubFrom) == len(b) - (tempRestLen) )
            length_Condition2 = ( len(elem_tosubFrom) == len(b) +1  - (tempRestLen))
            length_Condition3 = ( len(elem_tosubFrom) >= len(b) )
            length_Condition= ( length_Condition1 or length_Condition2 or length_Condition3) 

            if ( length_Condition ) :
                #old_elem_tosubFrom = elem_tosubFrom
                #elem_tosubFrom = a_zeros*"0"+elem_tosubFrom
                #elem_tosubFrom  = elem_tosubFrom[::-1]
                #elem_tosubFrom  = restofSub + elem_tosubFrom
            
                if ( binary_to_float(elem_tosubFrom) >=  binary_to_float(b)) :


                    result_of_sub = deleteFirstZeros(BinSub(elem_tosubFrom,b))[0]
                    #result_of_sub = (BinSub(elem_tosubFrom,b))
                    new_a = a[i+len(elem_tosubFrom)-len(restofSub):]
                    final_rest = result_of_sub + new_a
                    print("equation  " +str(elem_tosubFrom) +"  - "+str(b)+"  =  "+str(result_of_sub)  )
                    print(a, "new_a   "+str(new_a) , "a_ze")
                    print("\n")
                    restofSub = result_of_sub
                    tempRestLen = len(result_of_sub)
                    elem_tosubFrom = (result_of_sub)

                    i+= len(elem_tosubFrom)-len(restofSub)
                    #FloorDevAndMod(new_a,b,result_of_sub)

            
            i+=1

    return final_rest


def addBin (a,b) :



    if len(a) >= len(b):b=  (len(a)-len(b))*"0"+ b
    else :a = a+  (len(b)-len(a))*"0"   
  
    a = "0"+a
    b = "0"+b

    a = a[::-1]
    b = b[::-1]


    res = ""
    saved_bit = "0"
    for i in range(0,len(a)) :

        if (saved_bit == "0" ) :
            if (a[i] == "1" and b[i] == "0" ):
                res += "1"
                saved_bit = "0"

            if (a[i] == "0" and b[i] == "1" ) :
                res += "1"
            saved_bit = "0"

            if (a[i] == "0" and b[i] == "0" ) :
                res += "0"
                saved_bit = "0"

            if (a[i] == "1" and b[i] == "1" ) :
                res += "0"
                saved_bit = "1"
            
        elif (saved_bit == "1" ) :

            if (a[i] == "1" and b[i] == "0" ):
                res += "0"
                saved_bit = "1"

            if (a[i] == "0" and b[i] == "1" ) :
                res += "0"
            saved_bit = "1"

            if (a[i] == "0" and b[i] == "0" ) :
                res += "1"
                saved_bit = "0"

            if (a[i] == "1" and b[i] == "1" ) :
                res += "1"
                saved_bit = "1"
            
                   

    return res[::-1]




a = "1110100101"
b = "111"

#res = BinSub("11001111100000000000010110000011","10111010101110111","")
#print("res   " + str(res))


#FloorDevAndMod = FloorDevAndMod(a,b,"")
#print("FloorDevAndMod" , FloorDevAndMod , len(FloorDevAndMod))

#addBin_val  = addBin ("1001" ,"11")
#print("addBin_val" , addBin_val , len(addBin_val))



'''

    this section is to start testing and tweking the original ESDCA algorithm

'''



import json
file = open("./data_test2.json","r")
fp_dt = json.loads(file.read())
the_data = fp_dt["the_data"]
privkey = fp_dt["privkey"]
pubkey = fp_dt["pubkey"]
p = the_data[0]["p"]

b = "101"
old_value = "0"
for j in range(0,7) :
    old_value = addBin(old_value,b)
    print(old_value, "old_value")
# note 9*p to add one level 10
'''
for i in range(0,len(the_data)) :
    item = the_data[i]
    bool_itm =( item["value"] == "kk")
    # fileter all add operation to pub key
    all_possible_ry_before_mod = []
    if (bool_itm) :
        ry = item["ry"]
        ry_before_mod = item["ry_before_mod"]
        max_length_of_m = 155 #m is between 152-155
        max_length_ry_before_mod = 233 #ry before mod p  is between 227-233

        number_of_p_required_to_reach_max_range_ry = (max_length_ry_before_mod-len(str(ry)))*9*p 
        minimum_value_rp_before_mod = (227-len(str(p)))*(9*p) + ry
        print(len(str((10*p*1010))) , len(str(p)))
        all_possible_ry_before_mod.append(minimum_value_rp_before_mod)
        #print(ry ,'  |||||||||  ', minimum_value_rp_before_mod , '  |||||||||  '   )
        print(len(str(ry_before_mod)) ,'  |||||||||  ', len(str(minimum_value_rp_before_mod)) , '  |||||||||  '   )
        for j in range(0,(233-227)*9) :
            minimum_value_rp_before_mod+= p
            all_possible_ry_before_mod.append(minimum_value_rp_before_mod)
        print(ry_before_mod in all_possible_ry_before_mod , len(str(ry_before_mod)))
        print("\n")
        print("\n")
        break


'''

