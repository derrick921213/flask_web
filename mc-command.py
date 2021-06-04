from mcrcon import MCRcon
mcr = MCRcon('192.168.2.195', 'minecraft')
mcr.connect()
resp = mcr.command("/whitelist add derrick921213")
mcr.disconnect()
