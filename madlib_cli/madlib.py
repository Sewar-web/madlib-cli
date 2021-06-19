import re


def read_template(path):
    try:
        with open(path) as file:
            return  file.read()
    except FileNotFoundError:
        raise FileNotFoundError('The file not found')
    except Exception as e:
        return "Something's Going Wrong : "+ e



def parse_template(text):
    parse= re.findall(r'\{(.*?)\}', text)
    for item in parse:    
        text=text.replace((item),'',1)
    return text, tuple(parse)




def merge(text,parse):
 
    newtxt=text.format(*parse)

    with open('text/text.text','w') as output:
        output.write(newtxt)
    return newtxt


