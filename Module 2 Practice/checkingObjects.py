# Author Jibran Gill
# Checking python object
# Concept of Name Binding


def check_hex_id(obj):
    obj_id = hex((id(obj)))
    print('Address of object created in memory for ',obj, 'is', obj_id)
    return obj_id

def compare_memory_address(obj1, obj2):
    if obj1 == obj2:
        print("The memory address is same for objects i.e.  ", obj1,' and ', obj2)
    else:
        print("The memory address is different for objects i.e ", obj1,' and ', obj2)

def main():
    x = 4
    y = 10
    z = 12
    memory_address1 = check_hex_id(x)
    memory_address2 = check_hex_id(y)
    memory_address3 = check_hex_id(z)
    compare_memory_address(memory_address1, memory_address2)
    compare_memory_address(memory_address1,memory_address3)
    compare_memory_address(memory_address2,memory_address3)
if __name__ == "__main__":
    main()