def count_ch(str1,ch):
    str_to_list=list(str1)
    count=0
    for i in range(len(str_to_list)):
        if str_to_list[i]==ch:
            count+=1
    print("The character  ",ch, " is repeated  ",count," times.")
    pass

given_str=input("Enter String: ")
given_ch=input("Enter character: ")
count_ch(given_str,given_ch)
    
