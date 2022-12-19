%Model covariance (MCF) computation -----> selected model C(tao) = A.*exp(-B*tao)
%Amod = ECF(2,2) + ((ECF(2,2)-ECF(3,2))/(ECF(3,1)-ECF(2,1))) * (ECF(2,1)-ECF(1,1));
Amod = 9.5;				%expected signal power
tao_halving = 7;		%ECF tao closer to the expected correlation length
%id_halving = 6;			%ECF id closer to the expected correlation length
%Bmod = 1/tao_halving*(log(Amod)-log(ECF(id_halving,2)));	%invert model for B determination
Bmod = log(2)/tao_halving;

tao_mod = [0:0.1:ECF(end,1)];
mcf = Amod.*exp(-Bmod*tao_mod);

hold on,
plot(tao_mod,mcf,'-b')

%Noise estimate
Var_noise = ECF(1,2)-mcf(1)

%True covariance
mcf_orig = A.*exp(-B*tao_mod);
hold on,
plot(tao_mod,mcf_orig,'-r')