# xXxDankScavengerxXx
Dark times have come. Article 13 has been passed almost 2 years ago. Memes are illegal. People use USB sticks to store and sell them for caps. Every meme is identified by a size, given in MiB, and its market price. xXxDankScavengerxXx sells memes as his way of earning a living.

## Problem
Given set of memes, each with a name, size and price in caps, determine these to include in a collection so that the total space used is less or equal to given usb-drive capacity and the total value is as large as possible. In other words, maximise total value using given usb drive.

## Solution
Solution is base on dynamic programming algorithm, that uses divide and conquer principle. Running time of this algorithm is pseudo-polynomial - O(nW), where:
- n - number of memes
- W - total capacity of usb drive in the smallest unit, in our case MiB

##Code
Code has been written in Python 3.7.1, without external modules. 
__init__.py file as been included, so in order to use calculate() function, simply import it 


