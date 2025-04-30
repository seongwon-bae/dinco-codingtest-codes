shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

def binary_search(array, element):
    start = 0
    last = len(array)
    for i in range(start, last):
        now = (start+last)//2
        if array[now] > element:
            last = now
        elif array[now] < element:
            start = now
        else:
            return True
    else:
        return False

def is_available_to_order(menus, orders):
    menus.sort()
    result = False
    for i in orders:
        result = binary_search(menus,i)
    return result
result = is_available_to_order(shop_menus, shop_orders)
print(result)