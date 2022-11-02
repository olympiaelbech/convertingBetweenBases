import sys

for line in sys.stdin:
    line = line.strip()

    if line.find('>') != -1:

        x = int(line[:line.find('>')])
        y = int(line[line.find('>') + 1:])

    else:
        z = 0
        base = 1

        for convertBase in line:
            if not convertBase.isdigit():
                convertBase = ord(convertBase) - 87
            z += x ** (len(line) - base) * int(convertBase)
            base += 1

        convertNumber = ''

        if z == 0:
            convertNumber = 0

        else:
            while z > 0:
                if z % y >= 10:
                    convertNumber = chr(z % y + 87) + convertNumber
                else:
                    convertNumber = str(z % y) + convertNumber
                z //= y

        print(convertNumber)