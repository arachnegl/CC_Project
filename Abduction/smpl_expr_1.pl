abducible(dflt_expl(_)).
abducible(exp_a(_)).

obs_a(X) :- exp_a(X).

ic :- exp_a(X),obs_z(X).