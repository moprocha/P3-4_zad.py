def countdown(wishes = True):
    print("Trzy..")
    print("Dwa..")
    print("Jeden..")
    if not wishes:
        return
    print("Szczęśliwego Nowego Roku!")

countdown()
print()
countdown(wishes=False)
print()
countdown(0)
print()
countdown(None)
#