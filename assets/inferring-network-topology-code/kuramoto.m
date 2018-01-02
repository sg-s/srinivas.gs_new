%kuramoto.m
% this is just the kuramoto model
% last edit @ 20:22 on Tuesday the 09th 
% this can now be run by oneshot
function[phi] = kuramoto(J,ic)
%debug OFF
%clear all
tend = 500; % seconds
dt = 1e-3; % also seconds
w = 24; %Hz, this is the intrinsic frequency 
w = w*2*pi; % this is the phase correction
nsteps = floor(tend/dt);
n = length(J);

xi = NaN(n,nsteps);
% create inital conditions
%ic =  ones(1,n)*(1/n)*2*pi; % since this is the Kuramoto model, with near global 
%ic = [0:(2*pi/n):2*pi - (2*pi/n)];
%ic(1) = ic(1) + 0.1;
% debug
xi(:,1) = ic;
% simulate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
autohalt = nsteps;
for i = 2:1:autohalt
    if i == autohalt
        break
    end
    for j = 1:1:n
        % convention : J(:,j)  specififes indegree
        s = J(:,j).*(sin(xi(:,i-1)  -xi(j,i-1)));
        para = w + sum(s);
        xi(j,i) = xi(j,i-1) + dt*para;
        % check if system has phase locked

    end
        chkhalt= sum(abs((xi(:,i) - xi(1,i)) - (xi(:,i-1) - xi(1,i-1))));
        if autohalt == nsteps && chkhalt==0 && i > 10 % now an extra condition to make sure it runs at least 100 points

            autohalt = i+100; % so now it stops a 100 steps AFTER it phase locks
            %AUG = autohalt; % this stores the point till simulated for later reference
        end
end
phi = NaN(n-1,autohalt-1);
for i = 1:n
    phi(i,:) = xi(i,1:autohalt-1);
end
