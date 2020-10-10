#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) because the output will increase in equal relation to the input size

b) O(n log n) because the outer for loop will increase slower as n gets bigger
than the inner while loop which doubles each time.

c) O(n) because the output will increase in equal relation to the input size

## Exercise II

Start by finding the middle floor of n.  If an egg gets broken from this middle
floor, you won't have to go higher this now becomes the top floor.
Find the middle floor again of the new n.  If an egg gets broken from this middle
floor, you won't have to go higher and this is now the top floor.
If an egg doesn't break, you won't have to go lower and now this becomes the 
bottom floor.
Repeat this sequence of halving n until you only have 1 floor left and the egg
doesn't break.

The runtime complexity should be O(log n)
