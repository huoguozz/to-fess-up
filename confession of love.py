import tkinter as tk, random, time, sys, math
h, a= [],[]
t = ['..','','','']
c = ['pink', 'lightblue','lightgreen','skyblue','lemonchiffon','hotpink']

def g(n,w,h):
    p=[]
    for i in range(n):
        th = i/n*2*math.pi
        x = 16*math.sin(th)**3;y=13*math.cos(th)-5*math.cos(2*th)-2*math.cos(3*th)-math.cos(4*th)
        sx = int(w/2+x*20-50);sy=int(h/2-y*20-80)
        p.append((max(0,min(sx,w-150)),max(0,min(sy,h-40))))
    return p

def cw(x,y,tip=None,is_h=True):
    w=tk.Toplevel()
    w.geometry(f"150x40+{x}+{y}");w.title('point');w.attributes('-topmost',1)
    tk.Label(w,text=tip or random.choice(t),bg=random.choice(c),font=('微软雅黑',16),width=20,height=0).pack()
    w.bind('<space>',lambda e:[_.destroy() for _ in h+a or sys.exit()])
    return w

def q():
    r=tk.Tk();r.withdraw();sw,sh=r.winfo_screenwidth(),r.winfo_screenheight();n=100

    for i,(x,y) in enumerate(g(n,sw,sh)):
        w=cw(x,y,"Finally"if i==n-1 else None);h.append(w);r.update();time.sleep(0.01)

    time.sleep(1);[_.destroy() for _ in h if isinstance(_,tk.Toplevel) and _.winfo_exists()]

    #注意修改循环次数以防宕机
    for _ in range(sw//150*sh//40+50):
        x,y=random.randint(0,sw-150),random.randint(0,sh-40)
        w=cw(x,y,is_h=False);a.append(w);r.update();time.sleep(0.005)
    r.mainloop()

if __name__=="__main__":q()
