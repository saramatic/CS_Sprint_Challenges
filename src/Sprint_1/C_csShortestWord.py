"""
def csShortestWord(input_str):
    # check if input_str contains a space 
    if " " in input_str:
    # if space then 
        txt = input_str.split(" ")   
    elif "\t" in input_str:    
        txt = input_str.split("\t") 
    else:
        # return length of input_str 
        return len(input_str)
      
    shortest_len = 99999
    
    for x in txt:
    
        if len(x) < shortest_len:
            shortest_len = len(x) 
              
    return shortest_len

"""