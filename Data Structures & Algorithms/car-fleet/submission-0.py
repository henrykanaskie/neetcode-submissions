class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combine = zip(position, speed)
        sortt = reversed(sorted(combine))
        lsortt = list(sortt)
        fleets = 1
        prevtime = (target - lsortt[0][0]) / lsortt[0][1]
        for car in lsortt[1:]:
            position, speed = car
            time = (target - position) / speed
            if time > prevtime:
                fleets += 1
                prevtime = time

        return fleets

