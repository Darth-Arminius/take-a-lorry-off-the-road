# Gousto Code Kata - Take a Lorry off the Road With Some Code!

Code kata/tech test repo [here](https://github.com/Gousto/take-a-lorry-off-the-road)

My solution to this kata was:

- Read and store the box data from the `boxes.json` file
- Read and store the order data from the `orders.json` file
- For each order calculate the total volume of the order
- For each box calculate and convert the volume in cm3 from the dimensions
- Calculate the difference between the order volume and the box volume for each one
- If the difference is negative then the order won't fit in the box
- If the difference is smaller than any other then this box is currently the best fitting
- Once all the boxes have been checked the ID of the best fitting is printed along with the ID of the order
- The CO2 of that particular box is added to the total running CO2 amount of all the orders so far
- This CO2 value is then compared with the total max CO2 if all the orders went with the largest box
- If the difference between the CO2 values is greater than or equal to 1000 then we have successfully removed a lorry from the road

Improvements/What to do differently:

- Smarter best box selection by starting with the smallest box and breaking out of the loop once a non-negative value is found, this would require certainty in box sizes and identifiers for that
- Storing box volumes so that iterating through them isn't needed for every order, this would mean box volumes can only be calculated once at the start and not be dynamic
- Adding integration testing especially for the the main `intelligentPackaging` function
