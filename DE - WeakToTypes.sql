select sum(Normal) as Normal, sum(Fire) as Fire, sum(Water) as Water, sum(Grass) as Grass, sum(Ice) as Ice, sum(Fighting) as Fighting,
sum(Poison) as Poison, sum(Ground) as Ground, sum(Flying) as Flying, sum(Psychic) as Psychic, sum(Bug) as Bug, sum(Rock) as Rock,
sum(Ghost) as Ghost, sum(Dragon) as Dragon, sum(Dark) as Dark, sum(Steel) as Steel, sum(Fairy) as Fairy
from myTeam LEFT JOIN types on myTeam.Type_1 = types.Attacking
