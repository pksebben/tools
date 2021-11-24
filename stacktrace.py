def trace_calls(frame, event, arg):
    """
    Trace calls
    This is meant to provide deep debugging capabilities and code inspection given a large codebase that
    does weird shit.
    USAGE
    there are four major lists that are relevant to configuring output:
    - funcname_whitelist
    - filename_whitelist
    - callfunc_blacklist
    - callfile_blacklist
    
    If the whitelists are left empty, they are not used.  Whitelists exclude everything that doesn't match.
    Blacklists simply turn off output for matching patterns.
    """
    # only output if the function name is in this list
    funcname_whitelist = []
    # do not output if the function name is in this list
    funcname_blacklist = ['module', 'lambda']
    # only output if one of these is in 'path'.  Can be upper level directories
    filename_whitelist = ['/code/FexTools/ItkBackend']
    # do not output if one of these is in 'path'.  Can be upper level directories
    filename_blacklist = ['lib', 'frozen']
    
    if event != 'call':
        return
    co = frame.f_code
    func_filename = co.co_filename
    func_name = co.co_name
    if any(x in func_filename for x in filename_blacklist):
        return
    if any(x in func_name for x in funcname_blacklist):
        return
    if funcname_whitelist != []:
        if not any(x in func_name for x in funcname_whitelist) or funcname_whitelist:
            return
    if filename_whitelist != []:
        if not any(x in func_filename for x in filename_whitelist):
            return
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    func_line_no = frame.f_lineno
    caller = frame.f_back
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename
    print('Call to %s on line %s of %s from line %s of %s' % \
        (func_name, func_line_no, func_filename,
         caller_line_no, caller_filename))
    return

def trace_calls(frame, event, arg):
    """
    Trace calls
    This is meant to provide deep debugging capabilities and code inspection given a large codebase that
    does weird shit.
    USAGE
    there are four major lists that are relevant to configuring output:
    - funcname_whitelist
    - filename_whitelist
    - callfunc_blacklist
    - callfile_blacklist
    
    If the whitelists are left empty, they are not used.  Whitelists exclude everything that doesn't match.
    Blacklists simply turn off output for matching patterns.
    """
    # only output if the function name is in this list
    funcname_whitelist = []
    # do not output if the function name is in this list
    funcname_blacklist = ['module', 'lambda', 'autoreload']
    # only output if one of these is in 'path'.  Can be upper level directories
    filename_whitelist = ['ItkBackend', 'django']
    # do not output if one of these is in 'path'.  Can be upper level directories
    filename_blacklist = ['frozen', 'autoreload']
    
    if event != 'call':
        return
    co = frame.f_code
    func_filename = co.co_filename
    func_name = co.co_name
    if any(x in func_filename for x in filename_blacklist):
        return
    if any(x in func_name for x in funcname_blacklist):
        return
    if funcname_whitelist != []:
        if not any(x in func_name for x in funcname_whitelist) or funcname_whitelist:
            return
    if filename_whitelist != []:
        if not any(x in func_filename for x in filename_whitelist):
            return
    if func_name == 'write':
        # Ignore write() calls from print statements
        return
    func_line_no = frame.f_lineno
    caller = frame.f_back
    caller_line_no = caller.f_lineno
    caller_filename = caller.f_code.co_filename
    # print('Call to %s on line %s of %s from line %s of %s' % \
        # (func_name, func_line_no, func_filename,
         # caller_line_no, caller_filename))
    print(f"{func_filename}:{func_line_no} :: {func_name}")
    return

