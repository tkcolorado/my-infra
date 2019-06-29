# my-infra

### server1, server2
- fix the setting  
`PasswordAuthentication no` => `yes`;  
`sudo service ssh restart`

### fabric
```
vagrant@main:/srv/ops/fab_project$ sudo su -
root@main:~# pip3 install paramiko==2.1.2
vagrant@main:/srv/ops/fab_project$ fab -H root@172.16.200.101 host_type
[root@172.16.200.101] Executing task 'host_type'
[root@172.16.200.101] run: uname -s
[root@172.16.200.101] Login password for 'root':
[root@172.16.200.101] out: Linux
[root@172.16.200.101] out:
Done.
Disconnecting from root@172.16.200.101... done.
````

### error-fix
- error: `Ansible provisioning ERROR! Using a SSH password instead of a key is not possible`

`export ANSIBLE_HOST_KEY_CHECKING=False`