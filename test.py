import pyprosail

LIDFa, LIDFb = pyprosail.Planophile

res = pyprosail.run(
    N=1.5,
    Cab=40,
    Car=8,
    Cbrown=0,
    Cw=0.01,
    Cm=0.009,
    psoil=1,
    LAI=3,
    hspot=0.01,
    tts=30,
    tto=0,
    psi=10,
    TypeLidf=1,
    LIDFa=LIDFa, 
    LIDFb=LIDFb
)

# import matplotlib.pyplot as plt
# plt.plot(res[:,0], res[:,1])
# plt.show()