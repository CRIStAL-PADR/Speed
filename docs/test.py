import fallerlib
fallerlib.init("172.17.217.217")

IP_master = "172.17.217.217"
IP_slave = "172.17.217.60"
fallerlib.startM(IP_master, 1 , 1)
allerlib.stopM(IP_master,1)

