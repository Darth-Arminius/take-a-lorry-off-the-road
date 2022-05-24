import json


def getBoxes():
    boxesFile = open("boxes.json")
    boxesData = json.load(boxesFile)
    boxesFile.close()

    return boxesData


def getBoxVolumeCm3(boxData):
    dimensions = boxData["dimensions"]
    volumeMm3 = dimensions["widthMm"] * dimensions["heightMm"] * dimensions["depthMm"]

    return volumeMm3 / 1000


def getOrders():
    ordersFile = open("orders.json")
    ordersData = json.load(ordersFile)
    ordersFile.close()

    return ordersData


def getOrderVolume(order):
    ingredients = order["ingredients"]

    orderVolume = 0
    for ingredient in ingredients:
        orderVolume += ingredient["volumeCm3"]

    return orderVolume


def selectBestBox(boxes, order):
    orderVolume = getOrderVolume(order)
    volumeDifference = 9999
    selectedBoxId = ""

    for box in boxes:
        boxVolume = getBoxVolumeCm3(box)
        difference = boxVolume - orderVolume

        if difference > 0 and difference < volumeDifference:
            volumeDifference = difference
            selectedBoxId = box["id"]

    return selectedBoxId


def getMaxCo2(boxes):
    co2 = 0

    for box in boxes:
        if box["co2FootprintKg"] > co2:
            co2 = box["co2FootprintKg"]

    return co2


boxes = getBoxes()
orders = getOrders()
intelligentCo2 = 0

for order in orders:
    selectedBoxId = selectBestBox(boxes, order)
    selectedBox = next((x for x in boxes if x["id"] == selectedBoxId), None)
    intelligentCo2 += selectedBox["co2FootprintKg"]
    orderId = order["id"]
    print(f"Order ID: {orderId}, Box ID: {selectedBoxId}")

maxCo2 = getMaxCo2(boxes)
totalCo2Footprint = len(orders) * maxCo2
print(f"Sum of CO2 footprint without Intelligent Packaging: {totalCo2Footprint}")
print(f"Sum of CO2 footprint with Intelligent Packaging: {intelligentCo2}")

co2Difference = totalCo2Footprint - intelligentCo2
if co2Difference >= 1000:
    print("We have successfully removed a lorry from the road!")
else:
    print("We have sadly not removed a lorry from the road :(")
