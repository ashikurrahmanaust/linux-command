# file maker
import  sys, os

# defines or constants
TEMPLATE_PATH = '/home/akash/git_workspace/linux-filemaker'

class Maker:
    def __init__(self, file_name, current_directory, template_path):
        self.file_name = file_name
        self.curr_dir = current_directory
        self.template_path = template_path
        
    def run(self):
        if (self.file_name.endswith('.cpp')):
            self.copy_file(self.template_path + "/template.cpp", self.curr_dir + "/" + self.file_name)
        else:
            os.system("touch " + self.file_name)
    
    def copy_file(self, file_from, file_to):
        try:
            in_file = open(file_from, 'r')
            data = in_file.read()
            self.cpp_header(data)
        except:
            pass
            
    def cpp_header(self, data):
        cmd = "echo \"/***\" > " + self.curr_dir + "/" + self.file_name
        os.system(cmd)
        cmd = "echo \"*   author:   5-head\" >> " + self.curr_dir + "/" + self.file_name
        os.system(cmd)
        cmd = "echo -n \"*   created:  \" >> " + self.curr_dir + "/" + self.file_name
        os.system(cmd)
        cmd = "date \"+%d.%m.%Y %H:%M:%S\" >> " + self.curr_dir + "/" + self.file_name
        os.system(cmd)
        cmd = "echo \"***/\" >> " + self.curr_dir + "/" + self.file_name
        os.system(cmd)
        cmd = "echo \"\" >> " + self.curr_dir + "/" + self.file_name
        os.system(cmd)
        cmd = "echo \"" + str(data) + "\" >> " +  self.curr_dir + "/" + self.file_name
        os.system(cmd)
        
def main():
    if (len(sys.argv) < 3):
        exit(0)
    file_name = str(sys.argv[1])
    curr_dir = str(sys.argv[2])
    maker = Maker(file_name, curr_dir, TEMPLATE_PATH)
    maker.run()

if (__name__ == '__main__'):
    main()