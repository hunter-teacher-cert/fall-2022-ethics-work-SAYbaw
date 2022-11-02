# Plane Seating Algorithm

My algorithm will work the same as the current algoritm, but I would add one more function, seat_economy_pair. This would randomly look for two adjacent
seats and add +1 to the economy seat adjacent.

This algoritm would improve equity of families who can't afford the upgrade, but need to ensure at leat one adult is seated next to a child. If there are more than one child per adult, then they must try for the economy block, or pay for the economy plus upgrade. This also allows the airline to maximize its profits.

This algorithm could be improved by eliminating random window seating for economy plus, and prioritizing single passengers the right to only buy window seats, thus allowing for the higher probability of more "pairs" of open seats available for passengers with children or others who require care. If you want a window (say mom), then dad has to take the chance of sitting with liitle daughter in another row. This would no doubt cause an issue for those who want a window AND want to sit together, but it would also lesson the chances of travellers needing a companion, at least one, to sit by themselves.

In theory, at least as the code in concerned, this is an easy implementation. You just need to add another method that searches for two empty seats randomly, and picks the +1 adjacent. As far as making it more likely that pairs will be available, then it gets more complicated because you need to eliminate some features of the code (e.g., randomized windows for economy plus for blocks). Also, IRL, this may outrage the customers who want to pay more to get more.
