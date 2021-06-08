import re

files=" "

word=[]
def read_template():
    
    try:
        with open('text/template.txt') as file:
            files=file.read()
            # print(files)
            parse_template(files) 
    except FileNotFoundError:
            print('the path is invalid') 

      





def parse_template(files):
    
    regex = r"\{(.*?)\}"
    reg=re.findall(regex, files)
    print(reg)
    # print(len(reg))
     
    input_fun(reg ,files)





def input_fun(reg ,files):
    
    for w in range(len(reg)):
        inp=input('please insert  '+ reg[w] + ' ')
        word.append(inp)
        # print(word)
    merg(reg ,files)
    



def merg(reg ,files):
    print(len(reg))
    print(len(word))
    for i in range(len(word)):
        files = files.replace( "{" + reg[i] + "}" , word[i] )
    print (files)



read_template()




