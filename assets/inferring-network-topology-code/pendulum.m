%pendulum.m
% this is just a model of coupled pendulums, of my own creation
% rudimentary tests show that it exhibits pretty rich dynamics
% briefly, it never phase locks, it never syncrhonises, but there is a global attractor
% last edit @ 14:02 on Wednesday the 10th 
% for details on the model, see a Mathematica notebook called pendulum.nb
% this can now be run by oneshot variant
function[theta phi] = pendulum(J,k,b,tend,dt)
%debug OFF
%clear all
nsteps = floor(tend/dt);
n = length(J);

theta = NaN(n,nsteps); % theta and phi are the 2 dimensions of this system
phi = NaN(n,nsteps);    % which is a hack because phi = diff(theta)
% generate ics
theta(:,1) = rand(1,n)*2*pi*0.001; % we don’t want pendulums swirling all over the place
phi(:,1) = rand(1,n)*0.001; % i guess these are small velocities
% simulate~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for i = 2:1:nsteps
    for j = 1:1:n
        % convention : J(:,j)  specififes indegree
        theta(j,i) = theta(j,i-1) + phi(j,i-1)*dt;
        para = -k*(sin(theta(j,i-1))) + sum(J(:,j).*(sin(theta(:,i-1)  -theta(j,i-1)))) - b*phi(j,i-1);
        phi(j,i) = phi(j,i-1) + dt*para;
    end
end