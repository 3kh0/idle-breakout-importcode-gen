import base64
import crayons
import time

#test


# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 2, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()



print("{}".format(crayons.blue('\nWelcome to the interactive \nIdle Breakout import code generator by 3kh0!\n\nPlease enter numbers for the questions.\n')))
time.sleep(0.2)
print("{}".format(crayons.cyan('------------------------------------------\nWhat level you want to be on?')))
level = input()

print("{}".format(crayons.green('------------------------------------------\nHow much money do you want?')))
money = input()

print("{}".format(crayons.yellow('------------------------------------------\nHow much gold do you want?')))

gold = input()

print("{}".format(crayons.black('------------------------------------------\nHow many Black Boxes do you want?')))
bb = input()

print("------------------------------------------\nHow many skillpoints do you want?")
sp = input()

encode = f"{level},{money},{gold},3,0,0,0,0,0,0,0,1,1,0,43595.78,999999,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,{bb},0,0,0,1,{sp},1,0,0"
finalCode = encode.encode("UTF-8")
result = base64.b64encode(finalCode)

print("\nGenerating....")
# A List of Items
items = list(range(0, 57))
l = len(items)

# Initial call to print 0% progress
printProgressBar(0, 1, prefix = 'Progress:', suffix = '', length = 50)
for i, item in enumerate(items):
    # Do stuff...
    time.sleep(0.1)
    # Update Progress Bar
    printProgressBar(i + 1, l, prefix = 'Progress:', suffix = '', length = 50)
print("{}".format(crayons.green('Complete!')))

print("\n------------------------------------------\nHere is your code:\n")
print(result)

print("{}".format(crayons.red('\nCopy whats INSIDE the single quotes!\n')))
print("------------------------------------------")
print("Idle Breakout import code generator by 3kh0.")
time.sleep(0.2)
