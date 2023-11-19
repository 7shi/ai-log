import sys, os, io, pyperclip

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} file")
    sys.exit(1)

file = sys.argv[1]
while True:
    print("prompt?")
    p = pyperclip.waitForNewPaste().replace("\r\n", "\n").split("\n")
    while p and not p[-1]:
        p.pop()
    print("response?")
    r = pyperclip.waitForNewPaste().replace("\r\n", "\n")
    r.removesuffix("\n")
    with io.StringIO() as sio:
        if os.path.exists(file):
            print(file=sio)
            print("----", file=sio)
            print(file=sio)
        for line in p:
            print("    " + line, file=sio)
        print(file=sio)
        print(r, file=sio)
        with open(file, "ab") as f:
            f.write(sio.getvalue().encode("utf_8"))
