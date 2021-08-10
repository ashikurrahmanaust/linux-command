# file maker
import  sys

class Maker:
    def __init__(self, file_name, current_directory):
        self.file_name = file_name
        self.curr_dir = current_directory
        
    def run(self):
        if (self.file_name.endswith('.cpp')):
            copy_file("")
        else:
            print("anything")
    def dis(self):
        print(self.file_name + ' ' + self.curr_dir)
def main():
    if (len(sys.argv) < 3):
        exit(0)
    file_name = str(sys.argv[1])
    curr_dir = str(sys.argv[2])
    maker = Maker(file_name, curr_dir)
    # maker.run()
    maker.dis()

if (__name__ == "__main__"):
    main()