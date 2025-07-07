from modules.poisoning.cp import scan_cp
from modules.deception.cd import scan_cd
#from modules.poisoning.cp_dos import scan_cp_dos

def scan(url, protocol, headers_dict, body, method, cookie, mode, thread, silent):
        if mode == "cp":
            scan_cp(url, protocol, headers_dict, body, method, cookie, mode, thread, silent)

        elif mode == "cd":
             scan_cd(url, protocol, headers_dict, body, method, cookie, mode, thread, silent)

        # More test cases will be added soon.

        # elif mode == "cp-dos":
        #     scan_cp_dos(url, protocol, headers_dict, body, method, cookie, mode, thread, silent)

        # elif mode == "cp-dos2":
        #     scan_cp_dos(url, protocol, headers_dict, body, method, cookie, mode, thread, silent)

        #These three should be merged into one