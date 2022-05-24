import json


def getBoxes():
    """
    Opens the boxes.json file, reads the content, closes the file
    Returns the content
    """
    boxesFile = open("boxes.json")
    boxesData = json.load(boxesFile)
    boxesFile.close()

    return boxesData


def getBoxVolumeCm3(boxData):
    """
    Takes in a box object
    Gets the dimensions object of the provided box and multiplies the width, height, and depth to get the volume
    Each value (width, height, and depth) is in mm so must be divided by 1000 to get the volume in cm3
    Returns the volume in cm3
    """
    dimensions = boxData["dimensions"]
    volumeMm3 = dimensions["widthMm"] * dimensions["heightMm"] * dimensions["depthMm"]

    return volumeMm3 / 1000


def getOrders():
    """
    Opens the orders.json file, reads the content, closes the file
    Returns the content
    """
    ordersFile = open("orders.json")
    ordersData = json.load(ordersFile)
    ordersFile.close()

    return ordersData


def getOrderVolume(order):
    """
    Takes in an order object
    Gets the ingredients array of the provided order, then adds the volume of each ingredient together to get the total volume of the order
    Returns the total order volume
    """
    ingredients = order["ingredients"]

    orderVolume = 0
    for ingredient in ingredients:
        orderVolume += ingredient["volumeCm3"]

    return orderVolume


def selectBestBox(boxes, order):
    """
    Takes in all boxes and an order object
    Gets the total volume of the provided order then checks the difference between it and the volumes of each box
    If the difference is greater than 0 (all ingredients can fit) but less than any previous checks (less wasted space) then that box is selected
    Repeats until all boxes have been checked
    Returns the ID of the best box for the order
    """
    orderVolume = getOrderVolume(order)
    volumeDifference = 9999  # High number for initial comparison
    selectedBoxId = ""

    for box in boxes:
        boxVolume = getBoxVolumeCm3(box)
        difference = boxVolume - orderVolume

        if difference > 0 and difference < volumeDifference:
            volumeDifference = difference
            selectedBoxId = box["id"]

    return selectedBoxId


def getMaxCo2PerBox(boxes):
    """
    Takes in all boxes
    Iterates through all the boxes to find the highest value of CO2
    Returns the highest CO2 Footprint of all the boxes
    """
    co2 = 0

    for box in boxes:
        if box["co2FootprintKg"] > co2:
            co2 = box["co2FootprintKg"]

    return co2


def intelligentPackaging():
    """
    Gets all the boxes and orders provided from the boxes.json and orders.json files
    Calculates which box is the best fitting for each order so that all ingredients fit but with minimal wasted space
    Prints the ID of each Order along with the ID of the best selected Box for said Order
    Calculates the total maximum CO2 if the largest (highest CO2 value) box was used for every order and prints this value
    Calculates the total CO2 for every box used by every order and prints this value
    Calculates if a lorry was removed from the road by checking if the difference between the Max CO2 and CO2 from Intelligent Packaging is greater than or equal to 1000 and prints accordingly
    """
    boxes = getBoxes()
    orders = getOrders()
    totalIntelligentCo2 = 0

    for order in orders:
        selectedBoxId = selectBestBox(boxes, order)
        selectedBox = next(
            (box for box in boxes if box["id"] == selectedBoxId), None
        )  # Finds the first box that matches the id of the selectedBox
        totalIntelligentCo2 += selectedBox["co2FootprintKg"]
        orderId = order["id"]
        print(f"Order ID: {orderId}, Box ID: {selectedBoxId}")

    maxCo2PerBox = getMaxCo2PerBox(boxes)
    totalCo2 = (
        len(orders) * maxCo2PerBox
    )  # Uses the highest CO2 value multiplied by the number of orders to get the highest CO2 Footprint

    print(f"Sum of CO2 footprint without Intelligent Packaging: {totalCo2}")
    print(f"Sum of CO2 footprint with Intelligent Packaging: {totalIntelligentCo2}")

    co2Difference = totalCo2 - totalIntelligentCo2
    if co2Difference >= 1000:
        print("We have successfully removed a lorry from the road!")
    else:
        print("We have sadly not removed a lorry from the road :(")


intelligentPackaging()
