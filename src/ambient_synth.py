# Generates public/assets/audio/ambient.mp3: an original 64-second seamless ambient loop (no third-party samples).
# Run: python3 src/ambient_synth.py && ffmpeg -i ambient.wav -c:a libmp3lame -b:a 112k public/assets/audio/ambient.mp3
import numpy as np, wave
SR=44100; CH=8.0; prog=[[38,[54,57,61,64]],[35,[50,54,57,61]],[31,[50,54,57,59]],[33,[50,52,54,59]],
                        [38,[54,57,61,66]],[35,[50,54,59,61]],[31,[47,54,57,59]],[33,[49,52,57,59]]]
L=CH*len(prog); N=int(L*SR); rng=np.random.default_rng(7)
f=lambda m:440*2**((m-69)/12)
out=np.zeros((2,N))
def add(sig,start,ch_gain):
    idx=(int(start*SR)+np.arange(len(sig)))%N
    for c in range(2): np.add.at(out[c],idx,sig*ch_gain[c])
def env_pad(n,att,rel):
    t=np.arange(n)/SR; e=np.ones(n); a=int(att*SR); r=int(rel*SR)
    e[:a]=0.5-0.5*np.cos(np.pi*np.arange(a)/a); e[-r:]=0.5+0.5*np.cos(np.pi*np.arange(r)/r); return e
for i,(bass,notes) in enumerate(prog):
    start=i*CH-1.5; dur=CH+4.0; n=int(dur*SR); t=np.arange(n)/SR; e=env_pad(n,3.0,4.0)
    for k,m in enumerate(notes):
        fr=f(m); s=np.zeros(n)
        for d in (-0.07,0,0.07):
            ph=rng.uniform(0,2*np.pi)
            s+=np.sin(2*np.pi*fr*(1+d/100*12)*t+ph)+0.18*np.sin(2*np.pi*2*fr*t+ph)
        s*=e*(0.9+0.1*np.sin(2*np.pi*0.13*t+k))*0.045
        pan=0.3+0.4*(k/len(notes)); add(s,start,(1-pan,pan))
    fr=f(bass); s=(np.sin(2*np.pi*fr*t)+0.25*np.sin(2*np.pi*2*fr*t))*e*0.10; add(s,start,(0.5,0.5))
penta=[66,69,71,73,76,78,81]; t0=1.0
while t0<L-0.5:
    m=rng.choice(penta); n=int(5*SR); t=np.arange(n)/SR; fr=f(m)
    s=(np.sin(2*np.pi*fr*t)+0.25*np.sin(2*np.pi*2.76*fr*t)*np.exp(-t*3))*np.exp(-t*0.9)*np.minimum(1,t/0.01)*0.035
    p=rng.uniform(0.2,0.8); add(s,t0,(1-p,p)); t0+=rng.uniform(2.5,5.5)
noise=rng.standard_normal((2,N)); 
for c in range(2):
    y=np.fft.rfft(noise[c]); fq=np.fft.rfftfreq(N,1/SR); y*=1/(1+(fq/600)**2); noise[c]=np.fft.irfft(y,N)
noise/=np.abs(noise).max(); tt=np.arange(N)/SR
out+=noise*0.012*(0.7+0.3*np.sin(2*np.pi*tt/L*4))
# circular reverb
rt=3.2; n=int(rt*SR)
for c in range(2):
    ir=rng.standard_normal(n)*np.exp(-np.arange(n)/SR*(6.9/rt)); ir/=np.sqrt((ir**2).sum())
    irf=np.zeros(N); irf[:n]=ir
    wet=np.fft.irfft(np.fft.rfft(out[c])*np.fft.rfft(irf),N)
    out[c]=0.6*out[c]+0.55*wet
out/=np.abs(out).max(); out*=0.6
pcm=(out.T*32767).astype(np.int16)
w=wave.open('ambient.wav','wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes()); w.close()
print('ok',L)
