import sys, os, re, io, time, pyperclip

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} file")
    sys.exit(1)

def waitForNewPaste(timeout=0):
    current = pyperclip.paste()
    start = time.monotonic()
    while True:
        time.sleep(0.1)
        text = pyperclip.paste()
        if text != current:
            return text
        if timeout > 0 and time.monotonic() - start > timeout:
            raise pyperclip.PyperclipTimeoutException(
                f"waitForPaste() timed out after {timeout} seconds.")

def waitForNewPasteLines():
    ret = waitForNewPaste().replace("\r\n", "\n").split("\n")
    while ret and not ret[-1]:
        ret.pop()
    return ret

file = sys.argv[1]
num = 1
while True:
    print("prompt?")
    p = waitForNewPasteLines()
    print("response?")
    r = waitForNewPasteLines()
    with io.StringIO() as sio:
        if os.path.exists(file):
            print(file=sio)
        print("##", num, file=sio)
        num += 1
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
