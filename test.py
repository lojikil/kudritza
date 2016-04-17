import kudritza
r = kudritza.read
tests = [
"'{1 2 3 4}",
"{define-variable x '{1 2 3 4}}",
"{define-variable x :y}"]

for test in tests:
    print "test is: {0} with length: {1}".format(test, len(test))
    print r(test)
