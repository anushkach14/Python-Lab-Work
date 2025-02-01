str='''    indentation
            indentation
                indentation'''

for line in str.splitlines():
    print(line.lstrip())