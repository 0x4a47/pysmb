from smb.SMBConnection import SMBConnection

#Establish a connection to the server in the Winsearch initialization.
class WinSearch:
    def __init__(self, server_hostname, server_ip, user_id, user_password, client_machine_name):
        print("+[Creating WinSearch Object]")
        self._SMBConnection = SMBConnection(user_id, user_password, client_machine_name, server_hostname, use_ntlm_v2 = False)
        self._SMBConnected = self._SMBConnection.connect(server_ip, 139) #do the connection. Should make this asynchronous imo
        if(self._SMBConnected == True):
            print("+[Successfully created SMB Connection]")
        else:
            print("-[Failed to create SMB Connection]")
            self._SMBConnected = False
    

    def getSMBConnection(self):
        return self._SMBConnection

