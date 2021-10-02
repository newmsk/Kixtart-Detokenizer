operators = {0x00: ' and ',
             0x01: 'BEEP ',
             0x02: 'big ',
             0x04: 'Call ',
             0x07: 'cls',
             0x08: 'color ',
             0x0D: 'DIM ',
             0x0F: 'do ',
             0x15: 'exit ',
             0x16: 'file ',
             0x19: 'For ',
             0x1B: 'get ',
             0x1F: 'gosub ',
             0x25: 'list ',
             0x26: 'loop',
             0x2B: 'Not ',
             0x2C: ' or ',
             0x2F: 'play ',
             0x33: 'return ',
             0x35: 'Run ',
             0x38: 'setl ',
             0x3B: 'shell',
             0x3C: 'sleep',
             0x3D: 'little',
             0x40: ' To ',
             0x41: 'until ',
             0x42: 'use ',
             0xD1: ' = ',
             0xC6: ' + ',
             0xCC: ',',
             0xCD: '(',
             0xCE: ') ',
             0x21: 'if ',
             0x13: 'endselect',
             0x14: 'else',
             0x03: 'break ',
             0xC5: ' / ',
             0xCF: '[',
             0xD0: ']',
             0x2A: 'Next',
             0xE4: '? ',
             0x11: 'endif',
             0xD7: ' <> ',
             0x10: 'each ',
             0x22: ' in ',
             0x36: 'select',
             0x05: 'case ',
             0x43: 'while ',
             0xD4: '<=',
             0xD5: '>='}

functions = {0x00:" abs",
            0x01:" asc",
            0x02:" ascan",
            0x03:" addkey",
            0x04:" addprinterconnection",
            0x05:" addprogramgroup",
            0x06:" addprogramitem",
            0x07:" at",
            0x08:" backupeventlog",
            0x09:" box",
            0x0b:" chr",
            0x0c:" cint",
            0x0d:" cleareventlog",
            0x0e:" close",
            0x0f:" comparefiletimes",
            0x10:" cstr",
            0x11:" dectohex",
            0x12:" delkey",
            0x13:" delprogramgroup",
            0x14:" delprogramitem",
            0x15:" deltree",
            0x16:" delvalue",
            0x17:" delprinterconnection",
            0x18:" dir",
            0x19:" enumgroup",
            0x1a:" enumipinfo",
            0x1b:" enumkey",
            0x1c:" enumlocalgroup",
            0x1d:" enumvalue",
            0x1e:" execute",
            0x1f:" existkey",
            0x20:" exist",
            0x21:" expandenvironmentvars",
            0x22:" fix",
            0x23:" formatnumber",
            0x24:" freefilehandle",
            0x25:" getdiskspace",
            0x26:" getfileattr",
            0x27:" getfilesize",
            0x28:" getfiletime",
            0x29:" getfileversion",
            0x2a:" getobject",
            0x2b:" iif",
            0x2c:" ingroup",
            0x2d:" instr",
            0x2e:" instrrev",
            0x2f:" int",
            0x30:" isdeclared",
            0x31:" join",
            0x32:" kbhit",
            0x33:" keyexist",
            0x34:" lcase",
            0x35:" left",
            0x36:" len",
            0x37:" loadkey",
            0x38:" loadhive",
            0x39:" logevent",
            0x3a:" logoff",
            0x3b:" ltrim",
            0x3c:" makearray",
            0x3d:" memorysize",
            0x3e:" messagebox",
            0x3f:" createobject",
            0x40:" open",
            0x41:" readprofilestring",
            0x42:" readline",
            0x43:" readtype",
            0x44:" readvalue",
            0x45:" redirectoutput",
            0x46:" right",
            0x47:" rnd",
            0x48:" round",
            0x49:" rtrim",
            0x4a:" savekey",
            0x4b:" sendkeys",
            0x4c:" sendmessage",
            0x4d:" setascii",
            0x4e:" setconsole",
            0x4f:" setdefaultprinter",
            0x50:" setfocus",
            0x51:" setfileattr",
            0x52:" setoption",
            0x53:" setsystemstate",
            0x54:" settitle",
            0x55:" setwallpaper",
            0x56:" showprogramgroup",
            0x57:" shutdown",
            0x58:" sidtoname",
            0x59:" substr",
            0x5a:" srnd",
            0x5b:" split",
            0x5c:" trim",
            0x5d:" ubound",
            0x5e:" ucase",
            0x5f:" unloadhive",
            0x60:" val",
            0x61:" vartype",
            0x62:" vartypename",
            0x63:" writeline",
            0x64:" writeprofilestring",
            0x65:" writevalue",
            0x66:" getcommandline"}

macros = {0x01: 'address',
         0x02: 'build',
         0x04: 'comment',
         0x05: 'cpu',
         0x07: 'csd',
         0x08: 'curdir',
         0x09: 'date',
         0x0a: 'day',
         0x0B: 'domain',
         0x0C: 'dos',
         0x0D: 'error',
         0x0E: 'serror',
         0x0F: 'fullname',
         0x10: 'homedir',
         0x11: 'homedrive',
         0x12: 'homeshr',
         0x14: 'im',
         0x15: 'IpAddress0',
         0x16: 'IpAddress1',
         0x17: 'IpAddress2',
         0x18: 'IpAddress3',
         0x19: 'inwin',
         0x1A: 'kix',
         0x1B: 'kq',
         0x1C: 'lanroot',
         0x1D: 'ldomain',
         0x1E: 'ldrive',
         0x1F: 'lm',
         0x20: 'logonmode',
         0x21: 'longhomedir',
         0x22: 'lserver',
         0x23: 'm0',
         0x24: 'monthno',
         0x25: 'maxpwage',
         0x26: 'msecs',
         0x29: 'primarygroup',
         0x2A: 'priv',
         0x2B: 'productsuite',
         0x2C: 'producttype',
         0x2D: 'pwage',
         0x2E: 'ras',
         0x30: 'rserver',
         0x31: 'scriptdir',
         0x33: 'scriptname',
         0x34: 'sid',
         0x35: 'site',
         0x36: 'startdir',
         0x37: 'syslang',
         0x39: 'time',
         0x3B: 'userid',
         0x3C: 'userlang',
         0x3D: 'wdayno',
         0x3E: 'wksta',
         0x3F: 'wuserid',
         0x40: 'xt',
         0x41: 'ydayno',
         0x42: 'year',
         0xFF: '???'}
