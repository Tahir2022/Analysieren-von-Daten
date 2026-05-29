import math, random

# ---- Inputs ----
S0, K, r, sigma, T = 100.0, 100.0, 0.03, 0.2, 1.0
N = 200_000  # simulations

disc = math.exp(-r*T)
mu = (r - 0.5*sigma*sigma)*T
sigT = sigma*math.sqrt(T)

pay_sum = 0.0
cv_sum = 0.0  # control variate: use S_T with known E[S_T] = S0*e^{rT}

for _ in range(N//2):  # antithetic variates
    z = random.gauss(0.0, 1.0)
    for z_use in (z, -z):
        ST = S0 * math.exp(mu + sigT*z_use)
        payoff = max(ST - K, 0.0)
        pay_sum += payoff
        cv_sum += ST

# raw estimator
call_hat = disc * (pay_sum / N)

# ---- Control variate adjustment (optional, cheap) ----
# payoff vs ST correlation helps reduce variance
E_ST = S0 * math.exp(r*T)
# estimate beta* via sample covariance/C(ST) variance; use a simple plug-in:
# compute both means first (one pass above), then a second quick loop for cov/var:

# For simplicity (and speed without storing arrays), reuse a smaller batch:
M = 10_000
pay_mean = 0.0; st_mean = 0.0
ps = []; sts = []
for _ in range(M):
    z = random.gauss(0.0, 1.0)
    ST = S0 * math.exp(mu + sigT*z)
    p = max(ST - K, 0.0)
    ps.append(p); sts.append(ST)
    pay_mean += p; st_mean += ST
pay_mean /= M; st_mean /= M

cov = sum((p-pay_mean)*(s-st_mean) for p,s in zip(ps,sts)) / (M-1)
var = sum((s-st_mean)**2 for s in sts) / (M-1)
beta = 0.0 if var == 0 else cov/var

cv_adjusted = call_hat - disc*beta*((cv_sum/N) - E_ST)

print(f"Call (raw MC):        {call_hat:.6f}")
print(f"Call (control variate): {cv_adjusted:.6f}")
