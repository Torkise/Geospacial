N = length(obs_nomean);
t_pred = t_obs;							%filtering application


%Compute obs lag matrix
[t1,t2] = meshgrid(t_obs,t_obs);
TAO = abs(t1-t2);

%Compute obs cov matrix
Css = Amod.*exp(-Bmod*TAO);

%Compute noise cov matrix
Cvv = eye(N)*Var_noise;

%Compute obs-est lag matrix
[t1,t2] = meshgrid(t_pred,t_obs);
TAO = abs(t1-t2);

%Compute obs-est cov matrix
Csp = Amod.*exp(-Bmod*TAO);

%Get the prediction
pred = Csp' * inv(Css+Cvv) * obs_nomean;


figure,plot(t_obs,obs_nomean,'b')
hold on,plot(t_pred,pred,'r')
hold on,plot(t_obs,obs,'g')

%Get the prediction (recovering the original mean)
pred_unbiased = pred + mean(obs);

err = obs-pred_unbiased;
[mean(err) std(err) rms(err)]
[mean(noise) std(noise) rms(noise)] 