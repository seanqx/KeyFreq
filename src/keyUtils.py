def translateKey(key):

    if str(key) == "\'\\x01\'":
        return "a"
    if str(key) == "\'\\x02\'":
        return "b"
    if str(key) == "\'\\x03\'":
        return "c"
    if str(key) == "\'\\x04\'":
        return "d"
    if str(key) == "\'\\x05\'":
        return "e"  
    if str(key) == "\'\\x06\'":
        return "f"  
    if str(key) == "\'\\x07\'":
        return "g" 
    if str(key) == "\'\\x08\'":
        return "h" 
    if str(key) == "\'\\x09\'":
        return "i" 
    if str(key) == "\'\\x0a\'":
        return "j" 
    if str(key) == "\'\\x0b\'":
        return "k" 
    if str(key) == "\'\\x0c\'":
        return "l" 
    if str(key) == "\'\\x0d\'":
        return "m" 
    if str(key) == "\'\\x0e\'":
        return "n" 
    if str(key) == "\'\\x0f\'":
        return "o"
    if str(key) == "\'\\x10\'":
        return "p"
    if str(key) == "\'\\x11\'":
        return "q"
    if str(key) == "\'\\x12\'":
        return "r"
    if str(key) == "\'\\x13\'":
        return "s"
    if str(key) == "\'\\x14\'":
        return "t"
    if str(key) == "\'\\x15\'":
        return "u"
    if str(key) == "\'\\x16\'":
        return "v"
    if str(key) == "\'\\x17\'":
        return "w"   
    if str(key) == "\'\\x18\'":
        return "x"
    if str(key) == "\'\\x19\'":
        return "y"
    if str(key) == "\'\\x1a\'":
        return "z"
    if str(key) == "\'\\x1b\'":
        return "["    
    if str(key) == "\'\\x1c\'":
        return "\\"     
    if str(key) == "\'\\x1d\'":
        return "]" 
    if str(key) == "\'\\x1e\'":
        return "^" 
    if str(key) == "\'\\x1f\'":
        return "_"
    if str(key) == "\'\\x7f\'":
        return "?"   
 
    if str(key) == "\'\\n\'":
        return "j" 
    if str(key) == "\'\\t\'":
        return "i"   
    if str(key) == "\'\\r\'":
        return "m"  
    if str(key) == "<186>":
        return ";"  
    if str(key) == "<189>":
        return "-"  
    if str(key) == "<190>":
        return "."  
    if str(key) == "<191>":
        return "/"  
    if str(key) == "<220>":
        return "|"  
    if str(key) == "<222>":
        return "'"  
    else:
        return str(key).lower()
    
    