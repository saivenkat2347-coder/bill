
print("Tariff slabs:")
print("first 100 units 1.50")
print("next 100 units 2.50")
print("above 200 units 4.00")

previous = float(input("previous reading:"))
current = float(input("current reading:"))

units = current - previous

if current < previous:
    print("Error: current reading lower than previous reading")
else:
    print(f"previous: {previous}, current: {current}")
    print(f"consumtion {units}kWh")

    left = units

    slab1 = min(left, 100)
    charge1 = slab1 * 1.50
    left = left - slab1
    print(f"slab1: {slab1} unit * 1.50 = {charge1}")
    print(f"left: {left}")

    slab2 = min(left, 100)
    charge2 = slab2 * 2.50
    left = left - slab2
    print(f"slab2: {slab2} unit * 2.50 = {charge2}")
    print(f"left: {left}")

    slab3 = left
    charge3 = slab3 * 4.00
    left = left - slab3
    print(f"slab3 {slab3} unit * 4.00 = {charge3}")

    total = charge1 + charge2 + charge3
    print(f"total electricity bill: {total}")