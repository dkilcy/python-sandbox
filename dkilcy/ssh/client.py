
import paramiko
from StringIO import StringIO

address = '127.0.0.1'
username = 'dkilcy'

#pub_key = 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC1mMsaCkN/Uwj6bOewB57rZl8fivTcDrqTgDYN99K0TXUTdKIOhzmM6l/ORtFypA9al0OmUOjEsSNN2tJvy6OfJWWmuOdYbnflS78eTG+KB/4BrB6K3fgRaeGKrDlZ+LYKmNmPJ9E2HMdHY+EhuZ/hND2y5owINqCwVrXlL/23sRd8wauUAD7lq6dqIe4EJ86GKl2TP+nP6E1OboeDTGeTyBVms+t+woNryFJ26tcY9l0aLPUUWKI2sB8tbRhnYO57OP+/RiuMumeQNmMidTDuCs/GwQsfme1q9pSJrXtkBz4G022PZHSJRXGXcORs10zhuOAGAiE35On3n14LUghN'
pri_key = '-----BEGIN RSA PRIVATE KEY-----\r\nMIIEpQIBAAKCAQEAtZjLGgpDf1MI+mznsAee62ZfH4r03A66k4A2DffStE11E3SiDoc5jOpfzkbRcqQPWpdDplDoxLEjTdrSb8ujnyVlprjnWG535Uu/Hkxvigf+Aaweit34EWnhiqw5Wfi2CpjZjyfRNhzHR2PhIbmf4TQ9suaMCDagsFa15S/9t7EXfMGrlAA+5aunaiHuBCfOhipdkz/pz+hNTm6Hg0xnk8gVZrPrfsKDa8hSdurXGPZdGiz1FFiiNrAfLW0YZ2Duezj/v0YrjLpnkDZjInUw7grPxsELH5ntavaUia17ZAc+BtNtj2R0iUVxl3DkbNdM4bjgBgIhN+Tp959eC1IITQIDAQABAoIBAQCtsm5ig/q36Nanok+iYkex5gOKikFX04bG21XY2njiGUyoxWDVAKcdkHj/N2HTg/Vjs1fz12Qt7zlTmMC8Sk5BRWYLqMUwIsnvuxodgwMVRjvBob69GT/UeDBRkhZxZqHJVRaUBYPpfHFoabLHrWOt52g0nKzIlmfxA5+MjvDiJ5dUwuGxRHeMt3Hv8CxqOyIaxz/IZUqA5d6H3VMEsaNcCbispG1J3VrZNiKavZrFosBhz/mkzx262bw8aSZnOJGOG7vdNto8YIvtGMasEcsmaZEYM//awOR+L3g4VzmWgRO3P3BMGRd9o2UN7cX9+EDkiDnTLJLi99TXILr/cK/JAoGBANfAiX/uw+TEeNAyo27gNwPGUUgZl77PK9XdAV1ZcjTeusLCNLXLKsP3x4V4H16VtzRN84BkaJJ0JTlbi1Z9g2F9nbWnAODFhjBSGKwr74MUMSmNgJ40zV9UcPDY3kz28Y2ErMiiM3LBkA08qDHMi12XoNnmphZtlc5j6JHxDbCPAoGBANd5IyUebWVOcYywaH/l+WIOaFGEc0EFry4ZKKRvC92X0MGoB25LVnPRZ6QUafE7+jUnNgkoCEr76A3TGfKoJOq4Z5aKYOrgUQFzoL/8HXqW9kdyWPgZiim19rYX3xvQI8k49rW8zvrgHCnLhwWLriwWJqJsAv9qH5KRdiZD269jAoGBANFua8rM+klaUrA/R5h8e8rlOseTWFL3heS++PElv5AE2SPvIv2Jb0T1hC9ScJj/Gezi8kkirsPjjLLF41cc1WjQaEQKDfcipmTHfH281G3YLvTYEA8C0I0GSe/xhLEPUWF/db34fZqavHus8tQMawh6BMEgfP7ud2n2X68zYIePAoGAWhy/JfbjqUp1EnF0QojbErcTyYOq77aA3LaI2LvYKoQjOdobwXSgYy9gOK6Q3+JFcZVEc+/aCAHxulZes6y+Q6t7JuoYPiIxvnms8J1vdqVLufWIX7nOnkMLOnwhQnB5ht3bz4V2ylSPcqs7fIY+ARICdkrVthubuKA82SPn7CECgYEAo8t/mxINMnIHiYhyYiOfxlz91ScC1vQZwfIWO1UteHD/+2jGgnH/z/EaK4t3Z8vf+eb730vqm2oszh9qG5E6/U7y0VDT12chRUK9Hx8TE7QPNk9acrPugSqAeEWIDiobkDeVweXHomlWl22yv/TmDzq4XwssiSE/JFJ0S/BzPKI=\r\n-----END RSA PRIVATE KEY-----'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
key = StringIO(pri_key)
key = paramiko.RSAKey.from_private_key(file_obj=key)
#key = paramiko.RSAKey(data="ssh-rsa " + key)
client.connect(hostname=address, username=username, pkey=key)

channel = client.invoke_shell()
channel.send('hostname\n')

channel.shutdown_write()
            
while True:
    data = channel.recv(1024)
    if len(data) == 0:
        break
    print data
       
            