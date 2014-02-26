import os
target = "C:/Vim" 
# target = "C:/Users/escher9/.vim/bundle/vdebug" 
ext_ruleoutset = ['.pyc','.bak','out','files']
nameonly_ruleoutset = ['tags']
print 
print '+---------+'
print '| Caution |'
print '+---------+'
print 
print 'from ' + target
print 'removing recusively'
print ext_ruleoutset
a = raw_input("Are you sure?(y/n) ")
if a == "y":

    for root, dir, files in os.walk(target):
        for f in files:
            name, ext = os.path.splitext(f) 
            fullname = os.path.join(root,f) 
            if ext in ext_ruleoutset or f in nameonly_ruleoutset:
                os.remove(fullname)
                print 'removed '+f+ ' in '+root

else:
    print 'bye~'
