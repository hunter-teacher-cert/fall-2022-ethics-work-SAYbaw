# A Better Algorithm for Plane Seating
### By Steve Sabaugh

I thought the best way to solve this problem for this particular plane, was a simple implementation. Simply add a new method called seat_economy_pair(), which would be similar to seat_economy_block, however, the third formal parameter would be 2 or a pair. This way, you could guarantee that at least one passenger requiring assistance could sit with at least one person, or at least have a better chance, at the same price as economy. I will run it in the simulation at the same time as economy plus and seat_econonmy_block() and depending on the distribution I get between pairs, trios and economy plus, I may tweak windows to only be sold to individual economy plus passengers.

## Or so I thought...

