# README

This solution creates a 2D array and iterates through each row to find the first available seat given some
number of tickets. It uses a check to first see how many seats are available per row before 
searching for a seat. If the number of available seats is at least as large as the number of 
sought seats, it will traverse through that specific row, else return an empty list. 

If given an invalid input (ie: purchasing > 20 seats), the solution will return that that is an invalid 
transaction. Assume characters will not be passed in as input. 


## Input/Output
Some input.txt file in the same directory structure. Input file should have a list of reservations and 
desired number of tickets. 

Returns an output.txt file with the row and seat number assigned per reservation.