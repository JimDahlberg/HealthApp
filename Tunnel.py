"""Start ssh connection to server, press enter to disconnect.
Open sshtunnel required for online functionality
"""

import sshtunnel

if __name__ == "__main__":
    SSH_USER = '' #ACRONYM
    SSH_PASS = "" #CANVAS_PASS
        
    MYSQL_USER =  SSH_USER #ACRONYM
    MYSQL_PASS =  '' #MYSQL_PASS
    MYSQL_DATABASE = SSH_USER #ACRONYM

    server =  sshtunnel.SSHTunnelForwarder(
                ('ssh.student.bth.se', 22),
                ssh_username=SSH_USER,
                ssh_password=SSH_PASS,
                remote_bind_address=('blu-ray.student.bth.se', 3306)
    ) 
    server.start()
    
    f = open("port.txt", "w")
    f.write(str(server.local_bind_port))
    f.close()
    
    continue_loop = True
    while continue_loop:
        print(server.local_bind_port)
        continue_loop = input("end?")
    
    server.stop()