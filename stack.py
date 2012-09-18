import gdb
import re

""" 
    Reference:
    http://sourceware.org/gdb/current/onlinedocs/gdb/Python-API.html#Python-API 
"""

class StackFilterCommand(gdb.Command):
    def __init__(self):
        gdb.Command.__init__(self, 'btf', gdb.COMMAND_STACK)

    def invoke(self, filter_string, from_tty):
        '''
            The filter_string is a regular expression string.
            And we will only display those strings meet the 
            requirement.
        '''
        backtrace = []
        frame = gdb.selected_frame()

        while frame:
            backtrace.append(frame)
            frame = frame.older()

        # print for debugging
        number = 0
        for frame in backtrace:
            info = frame.find_sal()

            if info.symtab:
                # start filtering
                concate_string = info.symtab.filename + " " + frame.function().name
                if not re.search(filter_string, concate_string):
                    print "(", number, ")", info.symtab.filename, ":", info.line, "\t\t", frame.function().name

            number += 1


StackFilterCommand()     
