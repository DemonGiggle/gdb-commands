gdb-commands
============

Some useful gdb command

How to install

$ mkdir ~/gdb_commands; cd gdb_commands

$ git clone git@github.com:DemonGiggle/gdb-commands.git 

$ echo "source ~/gdb_commands/stack.py" > ~/.gdbinit 

.... you could add more python file via this way ....

In gdb, you could type the command as

gdb > btf boost

, which will filter out the call stack with the name boost in it. 

Note that the filtering string could be regular expression.

