from controllers import controller as ctr

def interacao():
    listapaises: list = []
    while True:
        entrada: str = input()
        instrs: list = entrada.split(" ")
        instr: str = instrs[0].upper()
        if instr == "RPI":
            pais = instrs[1]
            ctr.rpi(listapaises, pais)
            ctr.impressao()
        elif instr == "RPF":
            pais = instrs[1]
            ctr.rpf(listapaises, pais)
            ctr.impressao()
        elif instr == "RPDE":
            paisnovo = instrs[1]
            paisregistado = instr[2]
            ctr.rpde(listapaises, paisnovo, paisregistado)
            ctr.impressao()
        elif instr == "RPAE":
            paisnovo = instrs[1]
            paisregistado = instrs[2]
            ctr.rpae(listapaises, paisnovo, paisregistado)
            ctr.impressao()
        elif instr == "RPII":
            paisnovo = instrs[1]
            indice: int = instrs[2]
            ctr.rpii(listapaises, int(indice), paisnovo)
            ctr.impressao()
        elif instr == "VNE":
            print(f'O número de elementos são {ctr.vne()}')
        elif instr == "VP":
            pais = instrs[1]
            if ctr.vp(pais) == True:
                print(f'O país {pais} encontra-se na lista')
            if ctr.vp(pais) == False:
                print(f'O país {pais} não se encontra na lista')
        elif instr == "EPE":
            print(listapaises)
            ctr.epe(listapaises)
            print(f'O país {pais} foi eliminado da lista')
        elif instr == "EUE":
            ctr.eue(listapaises)
            print(f'O país {pais} foi eliminado da lista')
        elif instr == "EP":
            pais = instrs[1]
            if ctr.ep(listapaises, pais) == False:
                print(f'O país {pais} não se encontra na lista')
            elif ctr.ep(listapaises, pais) == True:
                print(f'O país {pais} foi eliminado da lista')