import sqlite3
from sqlite3 import Error
import pprint


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    global conn
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

# this is to parse a string in the insert into command for the database query
def parsing_string(thestring) : return "'" + thestring+"'"

# this is to parse all items for a long insert into command
def the_values_to_insert(the_values_of_items) :
    # the_values_of_items is an array
    theFinalString  ="("
    for elem in the_values_of_items :
        theFinalString += parsing_string(elem) + ","
    theFinalString = list(theFinalString)
    theFinalString[len(theFinalString)-1] = ")"
    theFinalString = "".join(theFinalString)

    return theFinalString

# this function is to create a the addition table
def CreateAdditiontable(conn) :
   
    j = 0
    bits_string =""
    for i in range(0,(256)) :
        bits_string +=  "  ,the" +str(j*256+i)+"  TEXT  "

    cursor = conn.cursor()
        # create a table
    create_table_command = """CREATE TABLE addition"""+ str(j) +"""
                            (status TEXT, reason TEXT, idxofnext TEXT
                            """ +bits_string+"""
                            )
                            """

    cursor.execute(create_table_command)
    conn.commit()


    return 0

# this function is to create a the addition table
def CreateModDivTable(conn) :
   
    j = 0
    bits_string =""
    for i in range(0,len("1110100010101011")) :
        bits_string +=  "  ,the" +str(j*256+i)+"  TEXT  "

    cursor = conn.cursor()
        # create a table
    create_table_command = """CREATE TABLE moddiv"""+ str(j) +"""
                           (
                            theid INTEGER PRIMARY KEY,
							subvalidx TEXT, 
                            borowedidx TEXT
                            """ +bits_string+""" ,
                            status bool

                            )
                            """

    cursor.execute(create_table_command)
    conn.commit()


    return 0

# this function is to select any item or items from a particular table
def select_from_table(conn , table_name , item_name_to_select):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT "+ str(item_name_to_select) +" FROM "+str(table_name))
    rows = cur.fetchall()

    return rows


# this function is to select any item or items from a particular table
def select_from_table_withCond(conn , table_name , item_name_to_select , condition):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    command = "SELECT "+ str(item_name_to_select) +" FROM "+str(table_name) + " WHERE  "+str(condition)
    #print(command)
    cur.execute( command )
    
    rows = cur.fetchall()

    return rows


# this function is to insert item into a table
def inset_items_in_table(conn , table_name , items_names , the_values_of_items) :

    cur = conn.cursor()
    insert_command = "INSERT INTO  "+ str(table_name)+"  " +str(items_names)+"  VALUES  " +str(the_values_of_items)

    cur.execute(insert_command)
   
    conn.commit()


    return 0

# this function is to update the table items with a condition
def update_table(conn , table_name , items_to_update , condition_for_update) :

    cur = conn.cursor()
   
    update_command = "UPDATE   "+ str(table_name)+" SET  " +items_to_update +"  WHERE  " +condition_for_update


    print(update_command)

    cur.execute(update_command)
   
    conn.commit()


    return 0

# this function is to find the positions of a particular bit in a Binary number
def findPositionsOfbitInAnumber(NumberInBits , toSearchBit):
    array = []
    for i  in range(0,len(NumberInBits)) :
        bit = NumberInBits[i]
        if (bit == toSearchBit) :
            array.append(str(i))

    return array

# this is to tell each possibility of a MOD divison 
def ReverseMod(mod_res,mod_by , lenght_of_origin) :
    i =0
    table_name = 'moddiv0'
    while i < lenght_of_origin :
        if (i < len(mod_res) ) :
            bit = mod_res[i]

            zeros_idx = findPositionsOfbitInAnumber(mod_by , "0")
            ones_idx = findPositionsOfbitInAnumber(mod_by , "1")

            if (bit == "0") :
                inset_items_in_table(conn ,table_name ,"(the"+str(i)+",subvalidx ,borowedidx"+")" , the_values_to_insert(["0", "null","null"  ]) )

                inset_items_in_table(conn ,table_name ,"(the"+str(i)+",subvalidx"+")" , the_values_to_insert(["0",   '/'.join(zeros_idx)   ]) )
                inset_items_in_table(conn ,table_name ,"(the"+str(i)+",subvalidx"+")" , the_values_to_insert(["1",    '/'.join(ones_idx)  ]) )
                inset_items_in_table(conn ,table_name ,"(the"+str(i)+",subvalidx ,borowedidx"+")" , the_values_to_insert(["0",  '/'.join(ones_idx)     ,str(i)]) )

            if (bit == "1") :
                inset_items_in_table(conn ,table_name ,"(the"+str(i)+",subvalidx ,borowedidx"+")" , the_values_to_insert(["1", "null","null"  ]) )

                inset_items_in_table(conn ,table_name ,"(the"+str(i)+",subvalidx"+")" , the_values_to_insert(["0",    '/'.join(zeros_idx)  ]) )
                inset_items_in_table(conn ,table_name,"(the"+str(i)+",subvalidx ,borowedidx"+")" , the_values_to_insert(["1",  '/'.join(ones_idx)     ,str(i)]) )

        else :

            zeros_idx = findPositionsOfbitInAnumber(mod_by , "0")
            ones_idx = findPositionsOfbitInAnumber(mod_by , "1")

            bit = "0"
            if (bit == "0") :
                inset_items_in_table(conn ,table_name ,"(the"+str(i)+",subvalidx"+")" , the_values_to_insert(["0",   '/'.join(zeros_idx)   ]) )
                inset_items_in_table(conn , table_name ,"(the"+str(i)+",subvalidx"+")" , the_values_to_insert(["1",    '/'.join(ones_idx)  ]) )
                inset_items_in_table(conn , table_name ,"(the"+str(i)+",subvalidx ,borowedidx"+")" , the_values_to_insert(["0",  '/'.join(ones_idx)     ,str(i)]) )
            
            bit = "1"
            if (bit == "1") :
                inset_items_in_table(conn , table_name ,"(the"+str(i)+",subvalidx"+")" , the_values_to_insert(["0",    '/'.join(zeros_idx)  ]) )
                inset_items_in_table(conn , table_name ,"(the"+str(i)+",subvalidx ,borowedidx"+")" , the_values_to_insert(["1",  '/'.join(ones_idx)     ,str(i)]) )
        
        i+=1

    return 0


def ModPossibilities(mod_res , mod_by , lenght_of_origin , table_name) :
    i = lenght_of_origin -1
    table_name = 'moddiv0'
    all_posibilities = []
    while i > 0 :
        
        theid_and_thebit = select_from_table_withCond(conn , table_name , " theid "+" , the"+str(i) +" ,subvalidx , borowedidx , status",  "the"+str(i)+" == 0 OR the"+str(i)+" == 1")
        for idbit in theid_and_thebit :
            theid = idbit[0]
            thebit = idbit[1]


            subvalidx = idbit[2]
            borowedidx = idbit[3]
            status = idbit[4]


            if len(all_posibilities) == 0  or i == lenght_of_origin -1:
                all_posibilities.append(
                    [
                        {
                        "delete_position":0 ,
                        "borrow_position" :""
                        } ,
                        
                        theid
                 ])
            else :
                for possibility in all_posibilities :
                    dict_of_data = possibility[0]
                    delete_position = dict_of_data["delete_position"]

                    
                    final_id = possibility[len(possibility)-1]
                    old_id_details = select_from_table_withCond(conn , table_name , " theid "+" , the"+str(i) +" ,subvalidx , borowedidx , status",  "theid == "+str(final_id))
                    old_bit = old_id_details[0][1]
                    if (old_bit == None) :
                        pass
                    elif old_bit == "0" :
                        pass
                    elif old_bit == "1":
                        pass
                    else :
                        print("bit is introuvable >>>  "+str(old_bit))

                    if (delete_position == len(mod_by)) :
                        delete_position = -1
                    else :
                        possibility[0]["delete_position"] =  delete_position + 1

                    print(possibility ,final_id , old_id_details , old_bit )
                    print("\n")

                pass
            #print(theid , thebit )

        print("\n")
        print("\n")
        i-=1 


    return 0
# this is where the magic happens
def main():
    conn = create_connection('ecctest.db')
    #CreateModDivTable(conn)
    #data_selected  = select_from_table(conn , "addition0" , "status ")
    #the_values_of_items = the_values_to_insert(["go"])
    #the_values_of_items  = "('go')"
    
    #the_values_of_items = the_values_to_insert(["go"])
    #inset_items_in_table(conn ,'moddiv0' ,"(status)" , the_values_of_items)
    
    #update_table(conn , 'addition0' , "the0= '125' , the3='0225'" , "status = 'go'")
    
    #pprint.pprint(data_selected)
    
    a = "1110100010101011"
    b = "101"
    mod_res = "011"
    #ReverseMod(mod_res,b , len(a))
    table_name = 'moddiv0'
    ModPossibilities(mod_res,b , len(a), table_name)


if __name__ == '__main__':
    main()
