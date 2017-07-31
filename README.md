# loot
Calculate loot split for pathfinder 

This file is a python file used for splitting/sharing party loot in Pathfinder

============

How it works

First the application asks you how much of each denomination you have and uses the pathfinder rule book to convert all currency
Into the smallest denomination which is copper.
After which the application will then try to add it back up and divide it into the smallest parts it can 

Example: 
Say you have 5 platinum pieces 98 gold pieces 45 silver pieces and 106 copper pieces and you need to split it between a group of 4
first the code will convert all pieces one by one into the equivalent copper value so for this example 
5 platinum is 5000cp 98 gold is 9800cp 45 silver is 450cp with 106cp left over. That adds up to 15356cp .
	
The program then divides it into the required portions so
	
15356cp / 1000 is 15pp
15356cp / 100 is 153gp and subtracting the platinum leaves us with 3gp
15356cp /10 is 1535sp subtract the gold and platinum leaves us with 5sp
15356cp /10 if you count the remainder is the amount of copper pieces left which is 6cp
This gives us a total of 6 cp, 5 sp, 3 gp, 15 pp
Now we divide it between 4 people, so using the total copper value and dividing by 4 we get 3839cp and using the same method as
Before we devide it into the biggest coin available and print the result 9 cp, 3 sp, 8 gp, 3 pp
		
Weight:
As an added functionality the application also prints out the total coin weight of the newly sorted currency
by assuming each coin ways .02lbs it adds the total amount of the coins and divides it by 50

==========

Known issues

. Client is unable to accept string values and crashes program
    
    
