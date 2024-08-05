itemsIncart = 0

# if itemsIncart != 2:
#        raise Exception("the product count is not matching")

# if itemsIncart != 2:
#        pass
# assert(itemsIncart==2)

try:
       with open('filelog.txt','r') as reader:
              reder.read()
# except:
#        print("the file is not present in the directory")
except Exception as e:
       print(e)
finally:
       print("cleaning up the resources")