import frida
import sys

package_name = "com.ethan.v2x.wvpn"


def on_message(message, data):
    print("asdadasd")
    print(data)


hook_script = ""
with open("../js_code/wvpn_hook.js") as f:
    hook_script = f.read()
    f.close()
process = frida.get_remote_device().attach(package_name)
print(process)
script = process.create_script(hook_script)
script.on('message', on_message)
print('[*] Running wvpn_hook')
script.load()
sys.stdin.read()
