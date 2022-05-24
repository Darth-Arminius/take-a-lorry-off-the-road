import unittest

from intelligent_packaging import (
    getBoxVolumeCm3,
    getBoxes,
    getMaxCo2PerBox,
    getOrderVolume,
    getOrders,
    selectBestBox,
)

expectedBoxData = [
    {
        "id": "PK-MED-01",
        "name": "Medium",
        "dimensions": {"widthMm": 30, "heightMm": 50, "depthMm": 60},
        "co2FootprintKg": 200,
    },
    {
        "id": "PK-SML-02",
        "name": "Small",
        "dimensions": {"widthMm": 20, "heightMm": 80, "depthMm": 50},
        "co2FootprintKg": 100,
    },
    {
        "id": "PK-LRG-03",
        "name": "Large",
        "dimensions": {"widthMm": 20, "heightMm": 100, "depthMm": 50},
        "co2FootprintKg": 300,
    },
]

expectedOrdersData = [
    {
        "id": "1",
        "ingredients": [
            {"name": "radishes", "volumeCm3": 9},
            {"name": "aubergine", "volumeCm3": 18},
            {"name": "super pasta", "volumeCm3": 27},
            {"name": "honey", "volumeCm3": 7.2},
            {"name": "duck", "volumeCm3": 23},
        ],
    },
    {
        "id": "2",
        "ingredients": [
            {"name": "artichokes", "volumeCm3": 20},
            {"name": "haricots", "volumeCm3": 6.7},
            {"name": "noodles", "volumeCm3": 18},
            {"name": "broccoli", "volumeCm3": 27.9},
            {"name": "mayonnaise", "volumeCm3": 3},
        ],
    },
    {
        "id": "3",
        "ingredients": [
            {"name": "lemon", "volumeCm3": 5},
            {"name": "garlic", "volumeCm3": 5},
            {"name": "ginger", "volumeCm3": 12.5},
            {"name": "soy", "volumeCm3": 5},
            {"name": "chicken thigh", "volumeCm3": 35},
            {"name": "pita bread", "volumeCm3": 18},
        ],
    },
    {
        "id": "4",
        "ingredients": [
            {"name": "brown onion", "volumeCm3": 7.5},
            {"name": "soy sauce", "volumeCm3": 5},
            {"name": "ginger", "volumeCm3": 9},
            {"name": "cod", "volumeCm3": 25},
            {"name": "brown rice", "volumeCm3": 26},
            {"name": "carrots", "volumeCm3": 20},
        ],
    },
    {
        "id": "5",
        "ingredients": [
            {"name": "yoghurt", "volumeCm3": 3},
            {"name": "black beans", "volumeCm3": 12.2},
            {"name": "ginger", "volumeCm3": 0.2},
            {"name": "spaghetti", "volumeCm3": 8.1},
            {"name": "peas", "volumeCm3": 3},
        ],
    },
    {
        "id": "6",
        "ingredients": [
            {"name": "parsnip", "volumeCm3": 4.7},
            {"name": "lamb", "volumeCm3": 7},
            {"name": "white rice", "volumeCm3": 6},
            {"name": "chicken", "volumeCm3": 5.6},
        ],
    },
    {
        "id": "7",
        "ingredients": [
            {"name": "lasagne sheets", "volumeCm3": 14.7},
            {"name": "cauliflower", "volumeCm3": 46},
            {"name": "white wine", "volumeCm3": 3},
            {"name": "lentils", "volumeCm3": 15},
            {"name": "breadcrumbs", "volumeCm3": 8.8},
        ],
    },
    {
        "id": "8",
        "ingredients": [
            {"name": "potato", "volumeCm3": 3},
            {"name": "parsnip", "volumeCm3": 2},
            {"name": "carrot", "volumeCm3": 2},
            {"name": "minced beef", "volumeCm3": 19},
        ],
    },
    {
        "id": "9",
        "ingredients": [
            {"name": "basa fillet", "volumeCm3": 18},
            {"name": "corn flour", "volumeCm3": 8.9},
            {"name": "potatoes", "volumeCm3": 35},
            {"name": "red onion", "volumeCm3": 5},
            {"name": "red pepper", "volumeCm3": 12.3},
        ],
    },
    {
        "id": "10",
        "ingredients": [
            {"name": "beans", "volumeCm3": 28},
            {"name": "chicken breast", "volumeCm3": 39},
            {"name": "rice", "volumeCm3": 13.9},
            {"name": "lemon", "volumeCm3": 5},
            {"name": "tomatoes", "volumeCm3": 12.1},
        ],
    },
]


class TestIntelligentPackaging(unittest.TestCase):
    def test_getBoxes(self):
        """
        Test that it can read and return boxes.json data
        """
        actualBoxData = getBoxes()
        self.assertEqual(actualBoxData, expectedBoxData)

    def test_getOrders(self):
        """
        Test that it can read and return orders.json data
        """
        actualOrdersData = getOrders()
        self.assertEqual(actualOrdersData, expectedOrdersData)

    def test_getBoxVolumeCm3(self):
        """
        Test that it can return the correct volume in cm3 from the provided boxData
        """
        expectedVolume = 90
        actualVolume = getBoxVolumeCm3(expectedBoxData[0])
        self.assertEqual(actualVolume, expectedVolume)

    def test_getOrderVolume(self):
        """
        Test that it can return the correct total volume of the provided order
        """
        expectedVolume = 84.2
        actualVolume = getOrderVolume(expectedOrdersData[0])
        self.assertEqual(actualVolume, expectedVolume)

    def test_getMaxCo2PerBox(self):
        """
        Test that it can return the correct highest CO2 value from the boxes array provided
        """
        expectedMaxCo2 = 300
        actualMaxCo2 = getMaxCo2PerBox(expectedBoxData)
        self.assertEqual(actualMaxCo2, expectedMaxCo2)

    def test_selectBestBox(self):
        """
        Test that it can return the ID of the best suited box based on the order and boxes array provided
        """
        expectedBoxId = "PK-MED-01"
        actualBoxId = selectBestBox(expectedBoxData, expectedOrdersData[0])
        self.assertEqual(actualBoxId, expectedBoxId)


if __name__ == "__main__":
    unittest.main()
