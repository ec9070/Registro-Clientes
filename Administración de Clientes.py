import util.connection as db
from forms.menu import Menu

def main():
    db.initialize()
    Menu()

if __name__ == '__main__':
    main()