def printing(val):
    print(val)
    
    
def resendchangedvalue(val):
    if isinstance(val, str):
        return val+"1"
    else:
        return val+1


if __name__=='__main__':
    print("working")