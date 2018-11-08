checklist = list()
# checklist.append('blue')
# print(checklist)
# checklist.append('orange')
# print(checklist)

def create(item):
    checklist.append(item)

def read(index):
    return checklist[index]

# checklist = ['blue', 'orange']
# checklist[1] = 'cats'
# print(checklist)

def update (index, item):
    checklist[index] = item

# checklist = ['blue', 'cats']
# checklist.pop(1)
# print(checklist)

def destory(index):
    checklist.pop(index)
    
def test():
    create("purple socks")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destory(1)

    print(read(0))
    print(read(1))

test()