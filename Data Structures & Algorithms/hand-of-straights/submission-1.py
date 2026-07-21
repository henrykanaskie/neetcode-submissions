class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        mp = {}
        for card in hand:
            if card in mp:
                mp[card] += 1
            else:
                mp[card] = 1
        hand.sort()

        for i in range(len(hand)):
            if mp[hand[i]]:
                for j in range(hand[i], hand[i] + groupSize):
                    if j not in mp or not mp[j]:
                        return False
                    mp[j] -= 1
        return True



