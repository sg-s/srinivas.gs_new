% osp.m
% osp is based on one shot, but it tries to reconstruct a network
% on which a 2D oscillator system operates
% this is realised in pendulum.m, which returns a matrix of theta and phi,
% the two dynamic variables. 
% Initial conditions are chosen by the network function. 
function [] = osp(n)

%% make system parameters
dilution = 0.5; % determines sparseness of graph
dt = (1e-3); % also seconds
b = 0.1; % damping constant
k = 1; % pendulum cosntant
tend = 10*log(n);
J = rand(n);
J = J - J.*eye(n);
J(rand(n)<dilution) = 0; 
%% run system, get phis back. 
[theta phi] = pendulum(J,k,b,tend,dt);
sd = size(phi);
nsteps = sd(2)-1; % this is the time to which the simulation was run. 
% the -1 is because when you differentiate a vector, the length shrinks
%% analysis
% compute phidot
phidot = NaN(n,nsteps);
thetadot = NaN(n,nsteps);
for i = 1:n
    phidot(i,:) = diff(phi(i,:))/dt;
end
% pick  random time steps  % testing!
% resort the first x fraction of transient
xf = round(nsteps/2); % xf is the number of points used for solving
if n>nsteps/20
    error('Transient too short')
end
ts = randperm(xf); % just for fun
% J has to be reconstructed row by row. 
Jcap = zeros(n);
% begin reconstruction
for i = 1:n
    % assemble LHS
    LHS = phidot(i,ts) + k*sin(theta(i,ts)) + b*phi(i,ts);
    % assemble RHS
    RHS = NaN(n-1,xf);
    ticker = setdiff([1:n],i);
    for j = 1:xf
        deltas = theta(ticker,ts(j)) - theta(i,ts(j));
        RHS(:,j) = sin(deltas);
    end
    Jcap(i,ticker) = LHS/RHS;
end
Jcap = Jcap'; % again, IÕve screwed up somewhere
if n < 10
    Jcap 
    J
    disp('Total relative error is:')
    disp(sum(sum(abs(Jcap-J)))/(n*n))
else
    disp('Total relative error is:')
    disp(sum(sum(abs(Jcap-J)))/(n*n));
end
