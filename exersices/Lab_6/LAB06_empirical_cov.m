clear all
close all

%load SIMUDATA
load INPUT_LAB06

t_obs = t;
obs = signal+noise;
obs_nomean = obs-mean(obs);

%Compute obs lag matrix
[t1,t2] = meshgrid(t_obs,t_obs);
TAO = abs(t1-t2);
TAO = triu(TAO,1);

%Compute correspondent obs cov matrix
[p1,p2] = meshgrid(obs_nomean,obs_nomean);
C = p1.*p2;
C = triu(C,1);

%Reshape lag and cov into arrays 
tao = TAO(:);
c = C(:);

%Consider single combinations only
c(tao==0)=[];
tao(tao==0)=[];

%Empirical covariance (ECF) computation
delta_tao_ecf = 2;										%ECF sampling interval
max_tao_ecf = 50;										%farther ECF sample
tao_ecf = [0:delta_tao_ecf:max_tao_ecf];				%ECF tao bin edges
tao_inbin = discretize(tao,tao_ecf);					%ECF tao binning

for bin = 1:length(tao_ecf)-1							%ECF tao binning
	c_inbin = c(tao_inbin==bin);
	ECF(bin,1) = tao_ecf(bin)+ delta_tao_ecf/2;
	ECF(bin,2) = mean(c_inbin);
end
ECF = [[0 var(obs_nomean)]; ECF];						%add C(0) to ECF

figure
plot(ECF(:,1),ECF(:,2),'*b'),grid on