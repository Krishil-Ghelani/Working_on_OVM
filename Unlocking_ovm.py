import virtualbox
import pyvbox
virtualbox.import_vboxapi()

try:
    vbox = virtualbox.VirtualBox()
    session = virtualbox.Session()
    vm = vbox.find_machine("Kali 2020 x64 Customized by zSecurity v1.3")
    progress = vm.launch_vm_process(session, 'gui', '')
    h, w, _, _, _, _ = session.console.display.get_screen_resolution(0)
    png = session.console.display.take_screen_shot_to_array(0, h, w, virtualbox.library.BitmapFormat.png)
    with open('screenshot.png', 'wb') as f:
        f.write(png)
    print(session.state)
    session.state
    SessionState(2)
    session.state >= 2
    True
    session.console.power_down()
except ModuleNotFoundError as e:
    
    vbox = virtualbox.VirtualBox()
    session = virtualbox.Session()
    vm = vbox.find_machine("Kali 2020 x64 Customized by zSecurity v1.3")
    progress = vm.launch_vm_process(session, 'gui', '')
    h, w, _, _, _, _ = session.console.display.get_screen_resolution(0)
    png = session.console.display.take_screen_shot_to_array(0, h, w, virtualbox.library.BitmapFormat.png)
    with open('screenshot.png', 'wb') as f:
        f.write(png)
    print(session.state)
    session.state
    SessionState(2)
    session.state >= 2
    True
    session.console.power_down()
    # except ModuleNotFoundError as k:
    #     pass
