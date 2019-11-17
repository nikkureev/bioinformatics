# функция проверяет тип коллекции и возвращает элемент
def search(collection, a):
    if type(collection) == dict:
        print(collection.get(a))
    else:
        print(collection[a])
