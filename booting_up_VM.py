import virtualbox
class Virtual:
    def __init__(self):
        try:
            vbox = virtualbox.VirtualBox()
            [m.name for m in vbox.machines]
            session = virtualbox.Session()
            machine = vbox.find_machine("Kali 2020 x64 Customized by zSecurity v1.3")
            # progress = machine.launch_vm_process(session, "gui", "")
            # For virtualbox API 6_1 and above (VirtualBox 6.1.2+), use the following:
            progress = machine.launch_vm_process(session, "gui", [])
            progress.wait_for_completion()
        except ModuleNotFoundError as e:
            try:
                vbox = virtualbox.VirtualBox()
                [m.name for m in vbox.machines]
                session = virtualbox.Session()
                machine = vbox.find_machine("Kali 2020 x64 Customized by zSecurity v1.3")
                # progress = machine.launch_vm_process(session, "gui", "")
                # For virtualbox API 6_1 and above (VirtualBox 6.1.2+), use the following:
                progress = machine.launch_vm_process(session, "gui", [])
                progress.wait_for_completion()
            except ModuleNotFoundError as f:
                pass
