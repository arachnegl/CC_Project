% A low is defined as a 8 hour period where consumption is at a minimum.

% Theory

fluctuations(I) :- inhabited_by(I).
day_low(I) :- day_worker(I).
day_low(I) :- day_sleep(I).
night_low(I) :- night_worker(I).
night_low(I) :- night_sleep(I).

morning_spike(I) :- prepare_food_morn(I).
midday_spike(I) :- prepare_food_midday(I).
evening_spike(I) :- prepare_food_dinner(I).

lunch(I) :- stay_at_home(I).

% Integrity Constraints

ic :- night_worker(I),\+ day_sleep(I).
ic :- day_worker(I),\+ night_sleep(I).
ic :- day_worker(I), night_worker(I).
ic :- night_worker(I),\+ stay_at_home(I).
ic :- night_worker(I),breakfast(I),dinner(I),\+ day_sleep(I).


% Abducibles

abducible(inhabited_by(_)).
abducible(day_worker(_)).
abducible(night_worker(_)).
adbucible(stay_at_home(_)).

% adbucible(day_sleep(I)).   % I don't care when they sleep in results. inBetween abducible.
