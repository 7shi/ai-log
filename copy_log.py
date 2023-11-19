import sys, os, re, io, pyperclip

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} file")
    sys.exit(1)

def waitForNewPaste():
    ret = pyperclip.waitForNewPaste().replace("\r\n", "\n").split("\n")
    while ret and not ret[-1]:
        ret.pop()
    return ret

file = sys.argv[1]
while True:
    print("prompt?")
    p = waitForNewPaste()
    print("response?")
    r = waitForNewPaste()
    with io.StringIO() as sio:
        if os.path.exists(file):
            print(file=sio)
        print("##", file=sio)
        print(file=sio)
        for line in p:
            print("    " + line, file=sio)
        print(file=sio)
        code = False
        for line in r:
            if line.startswith("```"):
                code = not code
            if not code and (m := re.match(r"#+(.*)", line)):
                print("**", m.group(1).strip(), "**" ,sep="", file=sio)
            else:
                print(line, file=sio)
        with open(file, "ab") as f:
            f.write(sio.getvalue().encode("utf_8"))
