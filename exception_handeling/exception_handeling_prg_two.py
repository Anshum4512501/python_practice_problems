try:
    file = open("debug.log", 'w')
    print(file.wri)

except FileNotFoundError:
    print("file could be found out")
except Exception as e:
    print(e)

else:
    print("Everything is fine")

finally:
    print("I m finally")
    file.close()
