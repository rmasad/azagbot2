import os

#class  plugins:
def main(name,msg,user,advice,channel,irc): 
    plugins =  os.listdir("plugins")


    #para que se incluyan solo una vez los modulos
    included = False
    if included == False:
        for element in plugins:
            if element != "__init__.py":
                if element[len(element)-3:] == ".py":
                    exec("from plugins import "+ element[:-3])
    included = True 


    for element in plugins:
        if element != "__init__.py":
            if element[len(element)-3:]  == ".py":
                exec(element[:-3] + ".main(msg,channel,irc,name)")
