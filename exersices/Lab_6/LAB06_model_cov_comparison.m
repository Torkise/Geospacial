figure
plot(ECF(:,1),ECF(:,2),'*b'),grid on

%Model covariance (MCF) computation -----> selected model C(tao) = A.*exp(-B*tao) -----> Exponential function 
%Amod = ECF(2,2) + ((ECF(2,2)-ECF(3,2))/(ECF(3,1)-ECF(2,1))) * (ECF(2,1)-ECF(1,1));
Amod = 9.5;				%expected signal power
tao_halving = 7;		%ECF tao closer to the expected correlation length
id_halving = 5;			%ECF id closer to the expected correlation length
%Bmod = 1/tao_halving*(log(Amod)-log(ECF(id_halving,2)));	%invert model for B determination
Bmod = log(2)/tao_halving;

tao_mod = [0:0.1:ECF(end,1)];
mcf1 = Amod.*exp(-Bmod*tao_mod);

hold on,
plot(tao_mod,mcf1,'-b')

%Model covariance (MCF) computation -----> selected model C(tao) = A.*exp(-B*tao.^2) -----> Normal function 
%Amod = ECF(2,2) + ((ECF(2,2)-ECF(3,2))/(ECF(3,1)-ECF(2,1))) * (ECF(2,1)-ECF(1,1));
Amod = 9.5;				%expected signal power
tao_halving = 7;		%ECF tao closer to the expected correlation length
id_halving = 5;			%ECF id closer to the expected correlation length
%Bmod = 1/(tao_halving^2)*(log(Amod)-log(ECF(id_halving,2)));	%invert model for B determination
Bmod = log(2)/(tao_halving^2);

tao_mod = [0:0.1:ECF(end,1)];
mcf2 = Amod.*exp(-Bmod*tao_mod.^2);

hold on,
plot(tao_mod,mcf2,'-g')

%True covariance
mcf_orig = A.*exp(-B*tao_mod);
hold on,
plot(tao_mod,mcf_orig,'-r')