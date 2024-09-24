import os as sistema
import time as tempo

a = ['/p','Sistem','Drag','Time','/f','Time of date','shutdown','Version','Windows','Lua','C#']

match str(input('Sim ou Não?\n')).capitalize():
    case 'Sim':
        print('Sim :>')
    case 'Não':
        print('Morra >:c')
        tempo.sleep(1)
        sistema.system(f'{a[6]} {a[0]} {a[4]}')
