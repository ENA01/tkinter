from tkinter import *
root = Tk()


def fun1():
    print("new project")


def fun2():
    print("new")


def fun3():
    print("new scratch")


def fun4():
    print("open")


def fun5():
    print("save")


def fun6():
    print("undo")


def fun7():
    print("redo")


def fun8():
    print("cut")


def fun9():
    print("copy")


def fun10():
    print("paste")


def fun11():
    print("delte")


def fun12():
    print("tool ")


def fun13():
    print("apperance")


def fun14():
    print("recent file")


def fun15():
    print("recent location")


def fun16():
    print("content info")


def fun17():
    print("info")


def fun18():
    print("back")


def fun19():
    print("forward")


def fun20():
    print("search")


def fun21():
    print("class")


def fun22():
    print("search in")


def fun23():
    print("bookmark")


def fun24():
    print("generate")


def fun25():
    print("coding")


def fun26():
    print("reformat file")


def fun27():
    print("folding")


def fun28():
    print("reformat saving")


def fun29():
    print("update")


main_menu = Menu(root)
root.config(menu=main_menu)
sub_menu = Menu(main_menu)

main_menu.add_cascade(label="file",menu=sub_menu)
sub_menu.add_command(label="new project",command=fun1)
sub_menu.add_command(label="new",command=fun2)
sub_menu.add_separator()
sub_menu.add_command(label="new scratch",command=fun3)
sub_menu.add_command(label="open",command=fun4)
sub_menu.add_separator()
sub_menu.add_command(label="save as",command=fun5)
sub_menu.add_command(label="quit",command=root.quit)

sub1_menu = Menu(main_menu)

main_menu.add_cascade(label="edit",menu=sub1_menu)
sub1_menu.add_command(label="undo",command=fun6)
sub1_menu.add_command(label="redo",command=fun7)
sub1_menu.add_separator()
sub1_menu.add_command(label="cut",command=fun8)
sub1_menu.add_command(label="copy",command=fun9)
sub1_menu.add_separator()
sub1_menu.add_command(label="paste",command=fun10)
sub1_menu.add_command(label="delete",command=fun11)

sub2_menu = Menu(main_menu)

main_menu.add_cascade(label="view",menu=sub2_menu)
sub2_menu.add_command(label="tool",command=fun12)
sub2_menu.add_command(label="apperance",command=fun13)
sub2_menu.add_separator()
sub2_menu.add_command(label="recent file",command=fun14)
sub2_menu.add_command(label="recent location",command=fun15)
sub2_menu.add_separator()
sub2_menu.add_command(label="context info",command=fun16)
sub2_menu.add_command(label="info",command=fun17)

sub3_menu = Menu(main_menu)

main_menu.add_cascade(label="navigate",menu=sub3_menu)
sub3_menu.add_command(label="back",command=fun18)
sub3_menu.add_command(label="forward",command=fun19)
sub3_menu.add_separator()
sub3_menu.add_command(label="search",command=fun20)
sub3_menu.add_command(label="class",command=fun21)
sub3_menu.add_separator()
sub3_menu.add_command(label="serach in",command=fun22)
sub3_menu.add_command(label="bookmark",command=fun23)

sub4_menu = Menu(main_menu)

main_menu.add_cascade(label="code",menu=sub4_menu)
sub4_menu.add_command(label="generate",command=fun24)
sub4_menu.add_command(label="coding",command=fun25)
sub4_menu.add_separator()
sub4_menu.add_command(label="reformat file",command=fun26)
sub4_menu.add_command(label="folding",command=fun27)
sub4_menu.add_separator()
sub4_menu.add_command(label="reformat saving",command=fun28)
sub4_menu.add_command(label="update",command=fun29)

root.mainloop()
