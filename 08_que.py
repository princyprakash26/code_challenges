#/give the discount:


def Discount(price,discount):
    discount_amount = (discount/100) * price
    total = price - discount_amount
    return total

result = Discount(100, 20)
print(result)
    