x_dict = {"Mahin":1,"hasan":2,"Mehedi":4}
print(x_dict)

del x_dict["Mehedi"]

print("After del: "+str(x_dict))
print("ID OF MAHIN: "+str(x_dict["Mahin"]))

print("Lenth: "+str(len(x_dict)))

print("Values in dict: "+str(x_dict.values()))