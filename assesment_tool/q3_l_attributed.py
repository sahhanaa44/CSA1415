import tkinter as tk
from tkinter import messagebox

# ============================================================
# L-ATTRIBUTED DEFINITION — "ATTRIBUTE LAB"
# A deliberately different visual design:
# dark laboratory / timeline / circular data-flow interface.
# Pure Python + Tkinter.
# ============================================================

BG = "#0b1020"
SURFACE = "#11182b"
SURFACE_2 = "#17213a"
BORDER = "#263452"
TEXT = "#f4f7ff"
MUTED = "#8f9bb5"

CYAN = "#39d9ff"
VIOLET = "#a78bfa"
PINK = "#fb7185"
LIME = "#a3e635"
GOLD = "#fbbf24"

class AttributeLab:
    def __init__(self, root):
        self.root = root
        self.root.title("Attribute Lab — L-Attributed Definition")
        self.root.geometry("1280x780")
        self.root.minsize(1050, 680)
        self.root.configure(bg=BG)

        self.step = 0
        self.auto = False
        self.timer = None

        self.a = tk.StringVar(value="2")
        self.b = tk.StringVar(value="3")
        self.c = tk.StringVar(value="4")

        self.build()
        self.render()

    # --------------------------------------------------------
    # UI
    # --------------------------------------------------------
    def build(self):
        top = tk.Frame(self.root, bg=BG, height=82)
        top.pack(fill="x", padx=26, pady=(20, 0))
        top.pack_propagate(False)

        left = tk.Frame(top, bg=BG)
        left.pack(side="left", fill="y")

        tk.Label(
            left, text="ATTRIBUTE LAB",
            font=("Segoe UI", 9, "bold"),
            fg=CYAN, bg=BG
        ).pack(anchor="w")

        tk.Label(
            left, text="L-attributed expression evaluator",
            font=("Segoe UI", 22, "bold"),
            fg=TEXT, bg=BG
        ).pack(anchor="w", pady=(2, 0))

        tk.Label(
            left, text="Watch information travel through the grammar.",
            font=("Segoe UI", 10),
            fg=MUTED, bg=BG
        ).pack(anchor="w")

        # Expression badge
        expr = tk.Frame(
            top, bg=SURFACE_2,
            highlightbackground=BORDER,
            highlightthickness=1
        )
        expr.pack(side="right", pady=10)

        tk.Label(
            expr, text="EXPRESSION",
            font=("Segoe UI", 8, "bold"),
            fg=MUTED, bg=SURFACE_2
        ).pack(side="left", padx=(14, 8))

        tk.Label(
            expr, text="a + b × c",
            font=("Consolas", 15, "bold"),
            fg=TEXT, bg=SURFACE_2
        ).pack(side="left", padx=(0, 14))

        # Main canvas
        self.canvas = tk.Canvas(
            self.root, bg=BG, highlightthickness=0
        )
        self.canvas.pack(fill="both", expand=True, padx=26, pady=8)
        self.canvas.bind("<Configure>", lambda e: self.render())

        # Bottom control strip
        bottom = tk.Frame(
            self.root, bg=SURFACE,
            highlightbackground=BORDER,
            highlightthickness=1,
            height=104
        )
        bottom.pack(fill="x", padx=26, pady=(4, 22))
        bottom.pack_propagate(False)

        # Inputs
        inputs = tk.Frame(bottom, bg=SURFACE)
        inputs.pack(side="left", padx=18, pady=16)

        self.make_input(inputs, "a", self.a)
        self.make_input(inputs, "b", self.b)
        self.make_input(inputs, "c", self.c)

        # Controls
        controls = tk.Frame(bottom, bg=SURFACE)
        controls.pack(side="left", padx=25)

        self.button(
            controls, "RUN", self.start,
            bg=VIOLET, fg="#100d1b"
        ).pack(side="left", padx=4)

        self.button(
            controls, "‹", self.prev,
            bg=SURFACE_2, fg=TEXT
        ).pack(side="left", padx=3)

        self.button(
            controls, "›", self.next,
            bg=SURFACE_2, fg=TEXT
        ).pack(side="left", padx=3)

        self.button(
            controls, "AUTO", self.auto_run,
            bg=CYAN, fg="#071019"
        ).pack(side="left", padx=8)

        self.button(
            controls, "RESET", self.reset,
            bg=SURFACE_2, fg=MUTED
        ).pack(side="left", padx=3)

        # Step indicator
        self.status = tk.Frame(bottom, bg=SURFACE)
        self.status.pack(side="right", padx=22)

        self.step_text = tk.Label(
            self.status,
            text="READY",
            font=("Consolas", 10, "bold"),
            fg=CYAN, bg=SURFACE
        )
        self.step_text.pack(anchor="e")

        self.desc = tk.Label(
            self.status,
            text="Press RUN to begin",
            font=("Segoe UI", 9),
            fg=MUTED, bg=SURFACE
        )
        self.desc.pack(anchor="e", pady=(3, 0))

    def make_input(self, parent, name, variable):
        box = tk.Frame(parent, bg=SURFACE_2)
        box.pack(side="left", padx=5)

        tk.Label(
            box, text=name.upper(),
            font=("Segoe UI", 8, "bold"),
            fg=MUTED, bg=SURFACE_2
        ).pack(side="left", padx=(8, 2))

        tk.Entry(
            box, textvariable=variable,
            width=4,
            font=("Consolas", 11, "bold"),
            fg=TEXT, bg=SURFACE_2,
            insertbackground=TEXT,
            relief="flat",
            justify="center"
        ).pack(side="left", padx=(0, 8), ipady=5)

    def button(self, parent, text, command, bg, fg):
        return tk.Button(
            parent, text=text, command=command,
            font=("Segoe UI", 9, "bold"),
            bg=bg, fg=fg,
            activebackground=bg,
            activeforeground=fg,
            relief="flat", bd=0,
            padx=12, pady=8,
            cursor="hand2"
        )

    # --------------------------------------------------------
    # Drawing
    # --------------------------------------------------------
    def render(self):
        self.canvas.delete("all")

        w = max(self.canvas.winfo_width(), 850)
        h = max(self.canvas.winfo_height(), 480)

        # subtle grid
        for x in range(0, w, 50):
            self.canvas.create_line(
                x, 0, x, h,
                fill="#10182b"
            )
        for y in range(0, h, 50):
            self.canvas.create_line(
                0, y, w, y,
                fill="#10182b"
            )

        # top explanatory labels
        self.canvas.create_text(
            22, 25,
            text="ATTRIBUTE FLOW",
            anchor="w",
            font=("Segoe UI", 9, "bold"),
            fill=MUTED
        )

        self.canvas.create_text(
            w - 22, 25,
            text=f"FRAME {max(self.step, 0):02d} / 06",
            anchor="e",
            font=("Consolas", 9, "bold"),
            fill=MUTED
        )

        # Flow layout: unlike the reference, this is horizontal,
        # circular, and timeline-driven rather than a tree/sidebar.
        y = h * 0.49

        x1 = w * 0.12
        x2 = w * 0.31
        x3 = w * 0.50
        x4 = w * 0.69
        x5 = w * 0.88

        # Timeline
        self.draw_flow_line(x1, y, x5, y)

        # Nodes
        self.draw_circle_node(x1, y, "ENV", "{a,b,c}", CYAN,
                              active=self.step in (1, 2))
        self.draw_circle_node(x2, y, "a", self.a.get(), VIOLET,
                              active=self.step == 4)
        self.draw_circle_node(x3, y, "*", "b × c", GOLD,
                              active=self.step == 3)
        self.draw_circle_node(x4, y, "VALUE", self.mult_value(), PINK,
                              active=self.step == 5)
        self.draw_circle_node(x5, y, "+", self.final_value(), LIME,
                              active=self.step == 6)

        # Attribute arrows above/below the timeline
        self.draw_attribute_arrow(
            x1, y - 105, x2, y - 105,
            "inherited environment", CYAN,
            active=self.step in (1, 2)
        )

        self.draw_attribute_arrow(
            x2, y + 105, x5, y + 105,
            "synthesized value", LIME,
            active=self.step >= 4
        )

        # Direction markers
        self.draw_direction_tag(
            x1 + 20, y - 155,
            "TOP-DOWN", CYAN
        )
        self.draw_direction_tag(
            x4 + 20, y + 155,
            "BOTTOM-UP", LIME
        )

        # Center operation explanation
        explanation = self.step_description()
        self.canvas.create_text(
            w / 2, h - 55,
            text=explanation,
            font=("Segoe UI", 11),
            fill=TEXT
        )

        # Mini legend in canvas
        self.legend_dot(22, h - 20, CYAN, "Inherited")
        self.legend_dot(125, h - 20, GOLD, "Evaluating")
        self.legend_dot(235, h - 20, LIME, "Synthesized")

    def draw_flow_line(self, x1, y, x2, color=None):
        self.canvas.create_line(
            x1, y, x2, y,
            fill=BORDER, width=5
        )

        # small ticks
        for x in [x1, (x1+x2)/4, (x1+x2)/2,
                  (x1+x2)*0.75, x2]:
            self.canvas.create_oval(
                x-3, y-3, x+3, y+3,
                fill=BORDER, outline=""
            )

    def draw_circle_node(self, x, y, title, value, color, active=False):
        r = 58 if active else 52

        # glow rings
        if active:
            for extra, alpha_color in [
                (16, "#1b2940"),
                (10, "#223454")
            ]:
                self.canvas.create_oval(
                    x-r-extra, y-r-extra,
                    x+r+extra, y+r+extra,
                    outline=alpha_color,
                    width=2
                )

        self.canvas.create_oval(
            x-r, y-r, x+r, y+r,
            fill=SURFACE,
            outline=color if active else BORDER,
            width=4 if active else 2
        )

        self.canvas.create_oval(
            x-r+9, y-r+9,
            x+r-9, y+r-9,
            outline="#1f2b44",
            width=1
        )

        self.canvas.create_text(
            x, y-10,
            text=title,
            font=("Segoe UI", 13, "bold"),
            fill=color
        )

        self.canvas.create_text(
            x, y+15,
            text=str(value),
            font=("Consolas", 11, "bold"),
            fill=TEXT
        )

        if active:
            self.canvas.create_text(
                x, y+r+20,
                text="ACTIVE",
                font=("Consolas", 8, "bold"),
                fill=color
            )

    def draw_attribute_arrow(self, x1, y1, x2, y2, text, color, active):
        line_color = color if active else BORDER
        width = 3 if active else 1

        self.canvas.create_line(
            x1, y1, x2, y2,
            fill=line_color,
            width=width,
            arrow=tk.LAST
        )

        self.canvas.create_text(
            (x1+x2)/2,
            y1-13,
            text=text,
            font=("Consolas", 9, "bold"),
            fill=line_color
        )

    def draw_direction_tag(self, x, y, text, color):
        self.canvas.create_rectangle(
            x, y-11, x+88, y+11,
            fill="#10182b",
            outline=color
        )
        self.canvas.create_text(
            x+44, y,
            text=text,
            font=("Consolas", 8, "bold"),
            fill=color
        )

    def legend_dot(self, x, y, color, text):
        self.canvas.create_oval(
            x, y-5, x+10, y+5,
            fill=color, outline=""
        )
        self.canvas.create_text(
            x+17, y,
            text=text,
            anchor="w",
            font=("Segoe UI", 8),
            fill=MUTED
        )

    # --------------------------------------------------------
    # Values
    # --------------------------------------------------------
    def nums(self):
        try:
            return float(self.a.get()), float(self.b.get()), float(self.c.get())
        except ValueError:
            return None

    def fmt(self, n):
        if isinstance(n, str):
            return n
        return str(int(n)) if float(n).is_integer() else f"{n:.2f}"

    def mult_value(self):
        n = self.nums()
        if not n:
            return "?"
        return self.fmt(n[1] * n[2])

    def final_value(self):
        n = self.nums()
        if not n:
            return "?"
        return self.fmt(n[0] + n[1] * n[2])

    # --------------------------------------------------------
    # Steps
    # --------------------------------------------------------
    def step_description(self):
        descriptions = {
            0: "Ready — enter values and press RUN.",
            1: "The variable environment is created at the root.",
            2: "Inherited information travels from the environment to identifiers.",
            3: "b and c are evaluated; their synthesized value becomes b × c.",
            4: "The value of a is available to the left side of the expression.",
            5: "The multiplication result is synthesized toward the parent.",
            6: "The root combines a + (b × c). Evaluation complete."
        }
        return descriptions[self.step]

    def update(self):
        self.step_text.config(
            text="READY" if self.step == 0
            else f"STEP {self.step}  /  06"
        )
        self.desc.config(text=self.step_description())
        self.render()

    def start(self):
        if not self.nums():
            messagebox.showerror(
                "Invalid input",
                "Please enter numeric values for a, b and c."
            )
            return

        self.stop()
        self.step = 1
        self.update()

    def next(self):
        if self.step < 6:
            self.step += 1
            self.update()

    def prev(self):
        if self.step > 1:
            self.step -= 1
            self.update()

    def reset(self):
        self.stop()
        self.step = 0
        self.update()

    def auto_run(self):
        self.stop()
        if self.step < 1:
            self.step = 1
        self.auto = True
        self.auto_tick()

    def auto_tick(self):
        if not self.auto:
            return

        self.update()

        if self.step < 6:
            self.step += 1
            self.timer = self.root.after(1000, self.auto_tick)
        else:
            self.auto = False

    def stop(self):
        self.auto = False
        if self.timer is not None:
            try:
                self.root.after_cancel(self.timer)
            except Exception:
                pass
            self.timer = None


if __name__ == "__main__":
    root = tk.Tk()
    AttributeLab(root)
    root.mainloop()