%
% 
%
% Typical usage:
%
% 	% yap
%
%	?- consult('abduction.pl')
%	?- load_theory('day_night_worker_cc.pl')
%
%	?- query([fluctuations(p)],(As,_,Ns)).   % Observed: fluctuations by p, What can be abduced?
%		[facilities_used(p)]             % equiv to household lived in
%
%	?- query([fluctuations(P)],(As,_,_)).    % Oberved: fluctuations by Someone
%		series of facilities_used answers: person can be p, or not p, or greg
%
%	?- query([day_low(p)...
%		[facilities_used(p),day_sleep(p)]
%
%	?- query([day_low(P)...                  % Identifies different possibilities (living arrangements)
%		[facilities_used(p),day_sleep(P),facilities_used(P),night_worker(P)],=/=(P,p);
%		[facilities_used(p),day_sleep(P)]
%
%	?- query([day_sleep(p)],(As,_,Ns)).
%		[facilities_used(p),day_sleep(p)]
%
%	?- query([night_low(p)],(As,_,Ns)).
%		[night_sleep(p),facilities_used(p),day_worker(p)]
%
%
%	(Ctrl-d to exit)


 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Theory (Background Knowledge) consists of rules and facts:   %
 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% A) Rules:    ( Observations :- hypotheses/explanations)
fluctuations(I) :- facilities_used(I).
day_low(I) :- night_worker(I).
day_low(I) :- day_sleep(I).
night_low(I) :- day_worker(I).
night_low(I) :- night_sleep(I).
%morning_spike(I) :- breakfast(I).
%midday_spike(I) :- lunch(I).
%evening_spike(I) :- dinner(I).
lunch(I) :- day_worker(I).

% B) Facts:  (these are 'pruned' by disaggregation)

lunch(p).
fluctuations(greg).
%night_low(p).
%fluctations(angela).

 %%%%%%%%%%%%%%%%%%%%%%%%%
% Integrity Constraints   %
 %%%%%%%%%%%%%%%%%%%%%%%%%

ic :- night_worker(I), \+ facilities_used(I).
ic :- day_worker(I), \+ facilities_used(I).
ic :- lunch(I), \+ facilities_used(I).

ic :- night_worker(I),lunch(I).
ic :- day_worker(I),\+ lunch(I).
ic :- night_worker(I),\+ day_sleep(I).   % a night worker has to sleep during the day
ic :- day_worker(I),\+ night_sleep(I).   % a day worker has to sleep during the night
ic :- day_worker(I), night_worker(I).    % can't be both day and night worker
ic :- day_low(I), night_low(I).

%%%%%%%%%%%%%%
% Abducibles %
%%%%%%%%%%%%%%

abducible(facilities_used(_)).
abducible(day_worker(_)).
abducible(night_worker(_)).
abducible(night_sleep(_)).
abducible(day_sleep(_)).
%adbucible(stay_at_home(_)).

