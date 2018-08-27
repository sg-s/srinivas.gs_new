% oneshot.m
% this is a test of the totally awesome theory of one-shot reconstruction
% the theory : start the system from some IC. observe the dynamical route towards
% the attractor. If you know the dynamical route, and if you know the coupling 
% funciton, then you can exactly determine J. itÕs that simple. 
%% ~~~~~~~~ONE SHOT DEVELOPMENT ROADMAP~~~~~~~~~
% 1. DONE reduce ts to n-1, pick points better, sans while loop
% 2. DONE implement over determined solutions
% 2.1 DONE new J to make it sparser
% 3. average over different ICs
function [J, Jcap] = oneshot(n)


%% make system parameters
dilution = 0.5;
J = rand(n);
J = J - J.*eye(n);
J(rand(n)>dilution) = 0; 
ic = rand(1,n)*2*pi;
dt = 1e-3;
w0 = 24*2*pi; % currently, this needs to be known
%% run system, get phis back. 
phi = kuramoto(J,ic);
sd = size(phi);
nsteps = sd(2)-1; % this is the time to which the simulation was run. 
%% analysis
% compute phidot
phidot = NaN(n,nsteps);
for i = 1:n
    phidot(i,:) = diff(phi(i,:))/dt;
end
% pick  random time steps  % testing!
% resort the first x fraction of transient
xf = round(nsteps/3);
if n>nsteps/2
    error('Transient too short')
end
ts = randperm(xf); % just for fun
% J has to be reconstructed row by row. 
Jcap = zeros(n);
% begin reconstruction
for i = 1:n
    % assemble LHS
    LHS = [phidot(i,ts)] - w0;
    % assemble RHS
    RHS = NaN(n-1,xf);
    ticker = setdiff([1:n],i);
    for j = 1:xf
        deltas = phi(ticker,ts(j)) - phi(i,ts(j));
        RHS(:,j) = sin(deltas);
    end
    Jcap(i,ticker) = LHS/RHS;
end
Jcap = Jcap'; % again, IÕve screwed up somewhere
if n < 10
    Jcap 
    J    
end
disp('Total relative error is:')
disp(sum(sum(abs(Jcap-J)))/(n*n));

%% plot
figure
subplot(1,3,1);
image(J*255), title('J')
axis image
subplot(1,3,2), image(Jcap*255), title('Jcap')
axis image
subplot(1,3,3), image(abs(Jcap-J)*1e6), title('Differences * 10^6')
axis image
colorbar