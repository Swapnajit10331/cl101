import dropbox
class Transferdata:
    def __init__(self,accesstoken) :
        self.accesstoken=accesstoken
    
    def upload_file(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        f=open(filefrom,"rb")
        dbx.filesupload(f.read(),fileto)

def main():
    accesstoken="sl.BLd_CNySzlaXGz3h40eS7QTpak83vBnzHiQAAIX_aJ6kwiZ4NwcPUcrz-wtDfDHh1vgGmES66rJDdirQy7XuVxnGoqWnSNN-Q-vFSBD-CcO5NerWC3KS2Zytee3kQUXE2DCpNM4"
    transferdata=Transferdata(accesstoken)
    
    filefrom=input("enter the file path to transfer")
    fileto=input("enter the path to upload the dropbox")
    transferdata.upload_file(filefrom,fileto)
    print("file has been moved")

main()

        
