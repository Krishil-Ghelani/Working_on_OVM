import pyvbox
import virtualbox

virtualbox.import_vboxapi()
try:
    vbox = virtualbox.VirtualBox()
    print("VM(s):\n + %s" % "\n + ".join([vm.name for vm in vbox.machines]))
except ModuleNotFoundError as e:
    try:
        vbox = virtualbox.VirtualBox()
        print("VM(s):\n + %s" % "\n + ".join([vm.name for vm in vbox.machines]))
    except ModuleNotFoundError as e:
        pass
