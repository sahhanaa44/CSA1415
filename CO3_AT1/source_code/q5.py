import tkinter as tk
from tkinter import ttk, messagebox

BG="#0b1220"; PANEL="#121c2e"; PANEL2="#17243a"
TEXT="#eef5ff"; MUTED="#8fa1bb"; LINE="#2b3a55"
BLUE="#5ee7ff"; PURPLE="#b79cff"; ORANGE="#ffb86b"
GREEN="#73e6a2"

RANK={"char":1,"int":2,"float":3,"double":4}
COL={"char":ORANGE,"int":BLUE,"float":PURPLE,"double":GREEN}

class SemanticWorkbench:
    def __init__(self, root):
        self.root=root
        root.title("Semantic Workbench — Type Compatibility")
        root.geometry("1250x780"); root.minsize(1050,700); root.configure(bg=BG)
        self.a=tk.StringVar(value="int"); self.op=tk.StringVar(value="+"); self.b=tk.StringVar(value="char")
        self.step=0; self.timer=None; self.running=False
        self.build(); self.refresh()

    def build(self):
        head=tk.Frame(self.root,bg=BG); head.pack(fill="x",padx=28,pady=(20,8))
        tk.Label(head,text="SEMANTIC WORKBENCH",font=("Segoe UI",9,"bold"),fg=BLUE,bg=BG).pack(anchor="w")
        tk.Label(head,text="Type Compatibility & Implicit Conversion",font=("Segoe UI",22,"bold"),fg=TEXT,bg=BG).pack(anchor="w")
        tk.Label(head,text="Watch semantic analysis resolve mixed operand types.",font=("Segoe UI",10),fg=MUTED,bg=BG).pack(anchor="w")

        body=tk.Frame(self.root,bg=BG); body.pack(fill="both",expand=True,padx=28)
        self.build_left(body); self.build_center(body); self.build_right(body)
        self.build_bottom()

    def build_left(self,parent):
        f=tk.Frame(parent,bg=PANEL,width=240,highlightbackground=LINE,highlightthickness=1)
        f.pack(side="left",fill="y",padx=(0,12)); f.pack_propagate(False)
        tk.Label(f,text="EXPRESSION BUILDER",font=("Segoe UI",9,"bold"),fg=MUTED,bg=PANEL).pack(anchor="w",padx=18,pady=(18,14))
        self.combo(f,"LEFT OPERAND",self.a,["char","int","float","double"])
        self.combo(f,"OPERATOR",self.op,["+","-","*","/"])
        self.combo(f,"RIGHT OPERAND",self.b,["char","int","float","double"])
        tk.Button(f,text="▶  ANALYZE",command=self.start,font=("Segoe UI",9,"bold"),bg=PURPLE,fg="#0c0a16",relief="flat",bd=0,pady=10).pack(fill="x",padx=18,pady=(18,6))
        tk.Button(f,text="RESET",command=self.reset,font=("Segoe UI",9,"bold"),bg=PANEL2,fg=MUTED,relief="flat",bd=0,pady=8).pack(fill="x",padx=18)
        r=tk.Frame(f,bg=PANEL2,highlightbackground=LINE,highlightthickness=1); r.pack(fill="x",padx=18,pady=25)
        tk.Label(r,text="CONVERSION LADDER",font=("Segoe UI",8,"bold"),fg=ORANGE,bg=PANEL2).pack(anchor="w",padx=12,pady=(12,5))
        tk.Label(r,text="char  <  int  <  float  <  double",font=("Consolas",9,"bold"),fg=TEXT,bg=PANEL2).pack(anchor="w",padx=12)
        tk.Label(r,text="The narrower type is promoted to the wider type.",font=("Segoe UI",8),fg=MUTED,bg=PANEL2,wraplength=190,justify="left").pack(anchor="w",padx=12,pady=(5,12))

    def combo(self,parent,label,var,values):
        tk.Label(parent,text=label,font=("Segoe UI",8,"bold"),fg=MUTED,bg=PANEL).pack(anchor="w",padx=18,pady=(5,4))
        c=ttk.Combobox(parent,textvariable=var,values=values,state="readonly",font=("Segoe UI",10))
        c.pack(fill="x",padx=18,pady=(0,10),ipady=4)

    def build_center(self,parent):
        f=tk.Frame(parent,bg=BG); f.pack(side="left",fill="both",expand=True)
        self.canvas=tk.Canvas(f,bg=BG,highlightthickness=0); self.canvas.pack(fill="both",expand=True)
        self.canvas.bind("<Configure>",lambda e:self.draw())

    def build_right(self,parent):
        f=tk.Frame(parent,bg=PANEL,width=255,highlightbackground=LINE,highlightthickness=1)
        f.pack(side="right",fill="y",padx=(12,0)); f.pack_propagate(False)
        tk.Label(f,text="SEMANTIC TRACE",font=("Segoe UI",9,"bold"),fg=MUTED,bg=PANEL).pack(anchor="w",padx=16,pady=(18,10))
        self.log=tk.Text(f,bg=PANEL,fg=TEXT,relief="flat",bd=0,font=("Consolas",9),wrap="word",state="disabled")
        self.log.pack(fill="both",expand=True,padx=12,pady=8)
        self.log.tag_config("tag",foreground=BLUE,font=("Consolas",8,"bold"))

    def build_bottom(self):
        f=tk.Frame(self.root,bg=PANEL,height=70,highlightbackground=LINE,highlightthickness=1)
        f.pack(fill="x",padx=28,pady=(10,20)); f.pack_propagate(False)
        tk.Label(f,text="EXECUTION",font=("Segoe UI",8,"bold"),fg=MUTED,bg=PANEL).pack(side="left",padx=(18,10))
        for text,cmd in [("‹ PREV",self.prev),("NEXT ›",self.next),("AUTO PLAY",self.auto_run)]:
            tk.Button(f,text=text,command=cmd,font=("Segoe UI",8,"bold"),bg=PANEL2,fg=TEXT,relief="flat",bd=0,padx=11,pady=8).pack(side="left",padx=3)
        self.status=tk.Label(f,text="IDLE",font=("Consolas",10,"bold"),fg=BLUE,bg=PANEL); self.status.pack(side="right",padx=18)

    def draw(self):
        if not hasattr(self,"canvas"): return
        c=self.canvas; c.delete("all"); w=max(c.winfo_width(),500); h=max(c.winfo_height(),500)
        for x in range(0,w,42): c.create_line(x,0,x,h,fill="#0f192a")
        for y in range(0,h,42): c.create_line(0,y,w,y,fill="#0f192a")
        a,b,op=self.a.get(),self.b.get(),self.op.get(); result=self.result()
        c.create_text(22,22,text="SEMANTIC RESOLUTION",anchor="w",font=("Segoe UI",9,"bold"),fill=MUTED)
        c.create_text(w/2,h*.08,text=f"{a}   {op}   {b}",font=("Consolas",15,"bold"),fill=TEXT)
        y=h*.30
        self.card(w*.19,y,"OPERAND A",a,f"rank {RANK[a]}",COL[a],self.step>=1)
        self.card(w*.50,y,"OPERATOR",op,"binary operation",ORANGE,self.step>=2)
        self.card(w*.81,y,"OPERAND B",b,f"rank {RANK[b]}",COL[b],self.step>=1)
        if self.step>=2:
            self.arrow(w*.19,y+55,w*.38,h*.55,COL[a]); self.arrow(w*.81,y+55,w*.62,h*.55,COL[b])
        ry=h*.63
        c.create_text(w/2,ry-68,text="CONVERSION LADDER",font=("Segoe UI",8,"bold"),fill=MUTED)
        x0,x1=w*.18,w*.82; c.create_line(x0,ry,x1,ry,fill=LINE,width=4)
        for i,t in enumerate(["char","int","float","double"]):
            x=x0+(x1-x0)*i/3
            active=self.step>=2 and RANK[t]==RANK[result]
            c.create_oval(x-25,ry-25,x+25,ry+25,fill=COL[t] if active else PANEL,outline=COL[t],width=2)
            c.create_text(x,ry,text=t,font=("Consolas",8,"bold"),fill="#071019" if active else COL[t])
            c.create_text(x,ry+38,text=str(RANK[t]),font=("Consolas",8),fill=MUTED)
        if self.step>=3 and a!=b:
            lower=a if RANK[a]<RANK[b] else b
            c.create_text(w/2,ry+55,text=f"PROMOTE   {lower}  →  {result}",font=("Consolas",10,"bold"),fill=ORANGE)
        if self.step>=4:
            c.create_rectangle(w/2-125,h*.86-20,w/2+125,h*.86+20,fill="#102a22",outline=GREEN,width=2)
            c.create_text(w/2,h*.86,text=f"✓  RESULT TYPE = {result}",font=("Consolas",10,"bold"),fill=GREEN)

    def card(self,x,y,title,value,sub,color,active):
        c=self.canvas; W,H=105,90
        c.create_rectangle(x-W/2,y-H/2,x+W/2,y+H/2,fill=PANEL,outline=color if active else LINE,width=3 if active else 1)
        c.create_text(x,y-H/2+15,text=title,font=("Segoe UI",7,"bold"),fill=MUTED)
        c.create_text(x,y-3,text=value,font=("Consolas",16,"bold"),fill=color)
        c.create_text(x,y+27,text=sub,font=("Consolas",7),fill=MUTED)

    def arrow(self,x1,y1,x2,y2,color):
        self.canvas.create_line(x1,y1,x2,y2,fill=color,width=2,arrow=tk.LAST)

    def result(self):
        return self.a.get() if RANK[self.a.get()]>=RANK[self.b.get()] else self.b.get()

    def refresh(self):
        self.draw(); self.update_log()
        names=["IDLE","READ OPERANDS","RANK TYPES","PROMOTE","FINAL RESULT"]
        self.status.config(text=names[min(self.step,4)])

    def update_log(self):
        self.log.config(state="normal"); self.log.delete("1.0","end")
        a,b=self.a.get(),self.b.get(); result=self.result(); items=[]
        if self.step>=1: items.append(("READ",f"Expression = {a} {self.op.get()} {b}"))
        if self.step>=2:
            items += [("RANK",f"{a} → rank {RANK[a]}"),("RANK",f"{b} → rank {RANK[b]}")]
        if self.step>=3:
            if a==b: items.append(("PROMOTE","No conversion required; types already match."))
            else:
                low=a if RANK[a]<RANK[b] else b
                items.append(("PROMOTE",f"{low} is promoted to {result}."))
        if self.step>=4: items.append(("RESULT",f"Expression is valid; result type = {result}."))
        if not items: items=[("WAIT","Press ANALYZE to begin.")]
        for tag,msg in items:
            self.log.insert("end",f"[{tag}]\n","tag"); self.log.insert("end",msg+"\n\n")
        self.log.config(state="disabled")

    def start(self): self.stop(); self.step=1; self.refresh()
    def next(self):
        if self.step<4: self.step+=1; self.refresh()
    def prev(self):
        if self.step>1: self.step-=1; self.refresh()
    def reset(self): self.stop(); self.step=0; self.refresh()
    def auto_run(self):
        self.stop(); self.step=1; self.running=True; self.tick()
    def tick(self):
        if not self.running: return
        self.refresh()
        if self.step<4:
            self.step+=1; self.timer=self.root.after(900,self.tick)
        else: self.running=False
    def stop(self):
        self.running=False
        if self.timer:
            try:self.root.after_cancel(self.timer)
            except:pass
        self.timer=None

if __name__=="__main__":
    root=tk.Tk()
    SemanticWorkbench(root)
    root.mainloop()