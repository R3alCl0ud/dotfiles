from simple_term_menu import TerminalMenu
import audioconfig.audioconfig as ac

def main():
    copy: bool = (ask_symlink_or_copy() == 0)
    print("Final configs will be copied to destination" if copy else "Final configs will be symlinked to destination")
    status = ac.main(copy=copy)
    if status is Exception:
        print(status)

def ask_symlink_or_copy():
    menu = TerminalMenu(['Copy Files', 'Symlink Files'], title='Copy or Symlink Files')
    return menu.show()


if __name__ == "__main__":
    main()


