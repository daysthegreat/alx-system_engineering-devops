Ex 0: su betty Script that changes user ID to betty

Ex 1: id -un Script that prints the effective username of the current user

Ex 2: id -Gn Script that prints all the groups the current user is part of

Ex 3: chown betty hello Script that changes owner of file hello to betty

Ex 4: touch hello Script that creates an empty file called hello

Ex 5: chmod u+x hello Script that adds execution permission to the file hello

Ex 6: chmod ug+x,o+r hello Add execute permission to user & group owner, and read permission to others for file hello

Ex 7: chmod ugo+x hello Script adds execution permission to all

Ex 8: chmod 007 hello Script sets command for file hello so neither owner nor group have any permissions while other users have read, write and execute permissions 

Ex 9: chmod 753 hello Script set permission so owner has all permissions, group has read & execute permission, others have write and execute permissions

Ex 10: chmod --reference=olleh hello Script the mode of file hello the same as file olleh's mode

Ex 11: chmod -R +X . Script adds execute permission to all subdirectories of thecurrent directory for everyone. Regular files remain unchanged

Ex 12: mkdir -m 751 my_dir Script creates a directory called my_dir with permissions 751 in the working directory. User has read, write, execute permissions. Groups has read & execute permissions & others have have only execute permission

Ex 13: 
