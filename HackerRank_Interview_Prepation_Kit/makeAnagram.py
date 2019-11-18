def makeAnagram(a, b):
    dicta = {}
    dictb = {}

    for i in a:
        if(i in dicta):
            dicta[i] += 1
        else: 
            dicta[i] = 1
    for i in b:
        if(i in dictb):
            dictb[i] += 1
        else: 
            dictb[i] = 1

    delete = 0
    
    for key in dicta:
        if key in dictb:
            # compare and delete
            delete_char = dicta[key] - dictb[key]
            if (delete_char < 0):
                delete_char = delete_char*(-1)            
            delete += delete_char

        else:
            delete += dicta[key]
    
    for key in dictb:
        if key not in dicta:
            delete += dictb[key]


    return delete