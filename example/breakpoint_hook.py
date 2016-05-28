# Add commands to the last breakpoint
# (gdb) comm
# info locals
# info args
# end
# (gdb) c

# Do the same with python script
# (gdb) so breakpoint_hook.py

# Before
import gdb


last_breakpoint_num = gdb.breakpoints()[-1].number

def commands(event):
    if last_breakpoint_num in (bp.number for bp in event.breakpoints):
        gdb.execute('info locals')
        gdb.execute('info args')

gdb.events.stop.connect(commands)

# After
