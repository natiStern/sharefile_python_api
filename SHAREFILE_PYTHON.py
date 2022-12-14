import requests

class sharefile():
    """
    this class implements sharefile's API
    methods:
     
    > auth -  get autenticating token 
    > items - Get Root Items
     
    """
    def dl(self,env:str,item_id,token,filepath:str):
        headers = {
            'Authorization': f'Bearer {token}',
        }

        response = requests.get(f'https://{env}.sf-api.com/sf/v3/Items({item_id})/Download', headers=headers, verify=False)

        with open(filepath, 'wb') as f:
            f.write(response.content)
        return response.json()

    def uploader(self,env:str,item_id,token,filepath:str):
        headers = {
                    'Authorization': f'Bearer {token}',
                    }   

        res = requests.get(f'https://{env}.sf-api.com/sf/v3/Items({item_id})/Upload', headers=headers, verify=False)
        f=dict(File1=open(file=filepath, 'rb'))
        

        files = {
            'File1': open(file=filepath, 'rb')
        }

        resp = requests.post(res, files=f, verify=False)
        return resp.json()
    def items(self,env:str,token):
        
        headers = {
                    'Authorization': f'Bearer {token}',
                    }   
        res = requests.get(f'https://{env}.sf-api.com/sf/v3/Items', headers=headers, verify=False)
        return res.json()
    def index(self,env:str,creds=None,comm=None):
      

        res = requests.get(f'https://{env}.sf-api.com/sf/v3')

        print(res)
        return res.json()
    def auth(self,env:str,creds={"USERNAME":"my@user.name","PASSWORD":'mypassword',"CLIENT_ID":"myclient-id","myclient-SECRET":"myclient-secret"},comm="Shares"):
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f'grant_type=password&client_id={creds["CLIENT_ID"]}&client_secret=creds["myclient-SECRET"]&username=creds["USERNAME"]&password=creds["PASSWORD"]'

        T = requests.post(f'https://{env}.sharefile.com/oauth/token', headers=headers, data=data)

        return T.json()

print(sharefile.index("weankor"))
print(sharefile.auth("weankor",creds={"USERNAME":"my@user.name","PASSWORD":'mypassword',"CLIENT_ID":"myclient-id","myclient-SECRET":"myclient-secret"}))

