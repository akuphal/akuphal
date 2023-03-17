select * from myTeam JOIN types on myTeam.Type_1 = types.Attacking
union
select * from myTeam JOIN types on myTeam.Type_2 = types.Attacking
