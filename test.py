import pyprosail

LIDFa, LIDFb = pyprosail.Planophile

res = pyprosail.run(
    n=1.5,
    cab=40,
    car=8,
    cbrown=0,
    cw=0.01,
    cm=0.009,
    psoil=1,
    lai=3,
    hspot=0.01,
    tts=30,
    tto=0,
    psi=10,
    typelidf=1,
    lidfa=LIDFa,
    lidfb=LIDFb
)

# import matplotlib.pyplot as plt
# plt.plot(res[:,0], res[:,1])
# plt.show()
