import os
import onedrivesdk

api_base_url='https://api.onedrive.com/v1.0/'

class onedrive(object):
    def __init__(self,token,client_id):
        self.token = token
        scopes = ['wl.signin', 'wl.offline_access', 'onedrive.readwrite']
        http_provider = onedrivesdk.HttpProvider()
        auth_provider = onedrivesdk.AuthProvider(
            http_provider=http_provider,
            client_id=client_id,
            scopes=scopes)
        self.client = onedrivesdk.OneDriveClient(api_base_url, auth_provider, http_provider)

    def uploadfile(self,filename):
        a=1

    def downloadfile(self,filename,dfilename):
        a=1