# Test Output

## Test 1: 1200 to 1450 (250 units)

```
PS C:\Users\saive> python -u "c:\Users\saive\OneDrive\Desktop\bill.py"
Tariff slabs:
first 100 units 1.50
next 100 units 2.50
above 200 units 4.00
previous reading:1200
current reading:1450
previous: 1200.0, current: 1450.0
consumtion 250.0kWh
slab1: 100 unit * 1.50 = 150.0
left: 150.0
slab2: 100 unit * 2.50 = 250.0
left: 50.0
slab3 50.0 unit * 4.00 = 200.0
total electricity bill: 600.0
```

## Test 2: 1000 to 1150 (150 units)

```
PS C:\Users\saive> python -u "c:\Users\saive\OneDrive\Desktop\bill.py"
Tariff slabs:
first 100 units 1.50
next 100 units 2.50
above 200 units 4.00
previous reading:1000
current reading:1150
previous: 1000.0, current: 1150.0
consumtion 150.0kWh
slab1: 100 unit * 1.50 = 150.0
left: 50.0
slab2: 50.0 unit * 2.50 = 125.0
left: 0.0
slab3 0.0 unit * 4.00 = 0.0
total electricity bill: 275.0
```

## Test 3: 1000 to 1100 (100 units)

```
PS C:\Users\saive> python -u "c:\Users\saive\OneDrive\Desktop\bill.py"
Tariff slabs:
first 100 units 1.50
next 100 units 2.50
above 200 units 4.00
previous reading:1000
current reading:1100
previous: 1000.0, current: 1100.0
consumtion 100.0kWh
slab1: 100.0 unit * 1.50 = 150.0
left: 0.0
slab2: 0.0 unit * 2.50 = 0.0
left: 0.0
slab3 0.0 unit * 4.00 = 0.0
total electricity bill: 150.0
```

## Test 4: 500 to 500 (0 units)

```
PS C:\Users\saive> python -u "c:\Users\saive\OneDrive\Desktop\bill.py"
Tariff slabs:
first 100 units 1.50
next 100 units 2.50
above 200 units 4.00
previous reading:500
current reading:500
previous: 500.0, current: 500.0
consumtion 0.0kWh
slab1: 0.0 unit * 1.50 = 0.0
left: 0.0
slab2: 0.0 unit * 2.50 = 0.0
left: 0.0
slab3 0.0 unit * 4.00 = 0.0
total electricity bill: 0.0
```
