-- Inner Join
-- Description
-- Consider a table named 'home' storing Arsenal football club's performance in the league at home in 2003-04 season, while the table 'away' stores Arsenal's performance away in the same season.
-- home: |opponent|goals_scored|goals_conceded|
-- away: |opponent|goals_scored|goals_conceded|
-- Note that a team is awarded three points for a win, one for a draw and zero for a loss. Write a query to determine the number of teams against whom Arsenal won all the available six points.
use upgrad;

select count(*)
from home inner join away on home.opponent = away.opponent
where home.goals_scored > home.goals_conceded and away.goals_scored > away.goals_conceded;