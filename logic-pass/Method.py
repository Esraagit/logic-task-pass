class rem:
    def remov(str1,ch):
        str_to_list=list(str1)
        for i in range(len(str_to_list)-1):
            if str_to_list[i]==ch:
                str_to_list.remove(ch)
        x=''
        print("New string is: ",x.join(str_to_list))
        pass
given_str=input("Enter String: ")
given_ch=input("Enter character: ")
rem.remov(given_str,given_ch)
        
        
