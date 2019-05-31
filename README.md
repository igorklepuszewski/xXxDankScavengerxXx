# xXxDankScavengerxXx
Dark times have come. Article 13 has been passed almost 2 years ago. Memes are illegal. People use USB sticks to store and sell them for caps. Every meme is identified by a size, given in MiB, and its market price. xXxDankScavengerxXx sells memes as his way of earning a living.

## Problem
Given set of memes, each with a name, size and price in caps, determine these to include in a collection so that the total space used is less or equal to given usb-drive capacity and the total value is as large as possible. In other words, maximise total value using given usb drive.

## Solving
Solution is base on dynamic programming algorithm, that uses divide and conquer principle. Running time of this algorithm is pseudo-polynomial - O(nW), where:
- n - number of memes
- W - total capacity of usb drive
