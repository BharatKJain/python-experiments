#Please run this code in WSL or Linux environment
from subprocess import check_output

def print_contents_of_cmd():
    return check_output(['pwd'])
if __name__ == "__main__":
    print_contents_of_cmd()