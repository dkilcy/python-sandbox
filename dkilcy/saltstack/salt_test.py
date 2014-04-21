'''
Created on Apr 17, 2014

@author: dkilcy
'''

#import os
#import salt.config

"""
master_opts = salt.config.master_config(
    os.environ.get('SALT_MASTER_CONFIG', '/etc/salt/master'))

minion_opts = salt.config.minion_config(
    os.environ.get('SALT_MINION_CONFIG', '/etc/salt/minion'))
"""

import salt.client
import salt.client.ssh

class SaltTest1(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.id = 1
    
    def execute(self, cfg):
        
        try:
            #username = profile['user']
            #key = profile['file_contents']
            
            minion_id = cfg['minion_id']
            module = cfg['module']
            commands = cfg['commands']
            
            #client = cfg['client']
            print minion_id
            
        except KeyError, e:
            self.code = -1
            self.content = 'Profile field not defined :%s' % str(e)
            return

        self.code = 0
        
        #client = salt.client.LocalClient();
        client = salt.client.SSHClient();
        
        # synchronously execute a command on a targeted minion
        print client.cmd(minion_id, module, commands)
         
    def finish(self):
        pass

if __name__ == '__main__':
    
    cfg={
        ##"client":"salt.client.SSHClient()",
        "minion_id":"*",
        "module":"cmd.run", "commands":[ "yum install salt-minion" ],          
        #"module":"test.ping","commands":[],
        #"module":"test.fib","commands":[10],
    }  
        
    saltTest1 = SaltTest1()
    saltTest1.execute(cfg)
    
    #salt-ssh '*' cmd.run "yum install salt-minion"
    
    #chkconfig salt-minion on
    #service salt-minion start
    
    #http://intothesaltmine.org/pages/salt-minion-install-guide.html
    #"wget -O - http://bootstrap.saltstack.org | sh"
    #"curl -L http://bootstrap.saltstack.org | sh"
    #"fetch -o - http://bootstrap.saltstack.org | sh"
    
    