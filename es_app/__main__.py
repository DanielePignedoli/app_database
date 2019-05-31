from plumbum import cli, local, colors

class MyApp(cli.Application):
    """add, delete, modify your notes
    """
    PROGNAME = "App for notes"
    VERSION = "0.1"
    
    def main(self):
        #path="/home/daniele/Scrivania/APPLIED/Software/es_app/"
        #path=self.make_database()
        if not self.nested_command:           # will be ``None`` if no sub-command follows
            print("No command given")
            return 1   # error exit code
    
    def new_path():
        #path = "/home/daniele/Scrivania/APPLIED/Software/es_app/"
        path= local["pwd"]()[:-1]+'/'
        if "Database" in local['ls'](path):
            pass
        else:
            local["mkdir"](path+"Database")
        return path + "Database"

    path=new_path()
        
    
@MyApp.subcommand("add")
class MyAppAddnotes(MyApp):
    "add notes"
    def main(self, text=None, text_file=None):
        if text==None:
            pass
        if text_file==None:
            text_file=self.if_already_exist("new_note")
        else:
            text_file = self.if_already_exist(text_file)
        with open(text_file,'w') as outfile:
            print(text, file=outfile)
            self.add_to_database(text_file, self.path)
    
    def if_already_exist(self, name):
        if name[-3:]=="txt":
            name = name[:-4]
        ls= local["ls"](self.path)
        if name in ls:
            i = 1
            while name + f"({i}).txt" in ls:
                i+=1
            return name+f"({i}).txt"
        else:
            return name
            
    def add_to_database(self, file, direc):
        local["mv"](file,direc)
    
@MyApp.subcommand("list")
class MyAppList(MyApp):
    "list all your notes"
    def main(self):
        print(local["ls"](self.path))
        
@MyApp.subcommand("remove")
class MyAppRemove(MyApp):
    "remove motes"
    def main(self, note=None):
        if note==None:
            note =self.chose_one()
        local["rm"](self.path +'/' + note)
    
    def chose_one(self):
        from itertools import count
        print("type 'Yes' if you have chosen, 'return' for the next")
        ls = local["ls"](self.path)
        ls = ls.split()
        i=0
        for j in range(len(ls)):
            if j==i%len(ls):
                print(colors.green & colors.bold | ls[j])
            else:
                    print(ls[j])
        for i in count(1):
            if not str(input())=='yes':
                for j in range(len(ls)):
                    if j==i%len(ls):
                        print(colors.green & colors.bold | ls[j])
                    else:
                        print(ls[j])
            else:
                break
        return ls[j]
                    
        
        
        
if __name__ == "__main__":
    MyApp.run()