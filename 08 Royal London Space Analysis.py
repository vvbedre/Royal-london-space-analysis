import tkinter as tk
from tkinter import ttk, messagebox

class RoyalLondonAnalysisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Royal London Space Analysis")
        self.root.geometry("1000x800")
        
        # Set style
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        self.style.configure('TButton', font=('Arial', 10))
        self.style.configure('Header.TLabel', font=('Arial', 12, 'bold'))
        self.style.configure('Result.TLabel', font=('Arial', 10, 'bold'), foreground='blue')
        self.style.configure('TNotebook', background='#f0f0f0')
        self.style.configure('TNotebook.Tab', font=('Arial', 10))
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Notebook for tabs
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create tabs
        self.create_input_tab()
        self.create_info_tab()
        
    def create_input_tab(self):
        # Input tab
        input_tab = ttk.Frame(self.notebook)
        self.notebook.add(input_tab, text="Analysis Calculator")
        
        # Header
        header_frame = ttk.Frame(input_tab)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Label(header_frame, text="Royal London Space Analysis", style='Header.TLabel').pack()
        ttk.Label(header_frame, text="Calculate space requirements for orthodontic treatment planning").pack()
        
        # Create canvas with scrollbar
        canvas = tk.Canvas(input_tab)
        scrollbar = ttk.Scrollbar(input_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Input frame
        input_frame = ttk.LabelFrame(scrollable_frame, text="Tooth Measurements (in mm)", padding="15")
        input_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        # Ideal values (average mesiodistal widths)
        ideal_values = {
            "upper_molar": 10.5, "lower_molar": 11.0,
            "upper_premolar": 7.0, "lower_premolar": 7.0,
            "upper_canine": 7.6, "lower_canine": 6.5,
            "upper_incisor": 8.5, "lower_incisor": 5.0
        }
        
        # Create measurement variables
        self.upper_right_molar = tk.DoubleVar(value=ideal_values["upper_molar"])
        self.upper_left_molar = tk.DoubleVar(value=ideal_values["upper_molar"])
        self.lower_right_molar = tk.DoubleVar(value=ideal_values["lower_molar"])
        self.lower_left_molar = tk.DoubleVar(value=ideal_values["lower_molar"])
        
        self.upper_right_premolar = tk.DoubleVar(value=ideal_values["upper_premolar"])
        self.upper_left_premolar = tk.DoubleVar(value=ideal_values["upper_premolar"])
        self.lower_right_premolar = tk.DoubleVar(value=ideal_values["lower_premolar"])
        self.lower_left_premolar = tk.DoubleVar(value=ideal_values["lower_premolar"])
        
        self.upper_right_canine = tk.DoubleVar(value=ideal_values["upper_canine"])
        self.upper_left_canine = tk.DoubleVar(value=ideal_values["upper_canine"])
        self.lower_right_canine = tk.DoubleVar(value=ideal_values["lower_canine"])
        self.lower_left_canine = tk.DoubleVar(value=ideal_values["lower_canine"])
        
        self.upper_right_incisor = tk.DoubleVar(value=ideal_values["upper_incisor"])
        self.upper_left_incisor = tk.DoubleVar(value=ideal_values["upper_incisor"])
        self.lower_right_incisor = tk.DoubleVar(value=ideal_values["lower_incisor"])
        self.lower_left_incisor = tk.DoubleVar(value=ideal_values["lower_incisor"])
        
        # Create input fields in a grid
        measurements = [
            ("Upper Right Molar (16)", self.upper_right_molar),
            ("Upper Left Molar (26)", self.upper_left_molar),
            ("Lower Right Molar (46)", self.lower_right_molar),
            ("Lower Left Molar (36)", self.lower_left_molar),
            ("Upper Right Premolar (14)", self.upper_right_premolar),
            ("Upper Left Premolar (24)", self.upper_left_premolar),
            ("Lower Right Premolar (44)", self.lower_right_premolar),
            ("Lower Left Premolar (34)", self.lower_left_premolar),
            ("Upper Right Canine (13)", self.upper_right_canine),
            ("Upper Left Canine (23)", self.upper_left_canine),
            ("Lower Right Canine (43)", self.lower_right_canine),
            ("Lower Left Canine (33)", self.lower_left_canine),
            ("Upper Right Incisor (11)", self.upper_right_incisor),
            ("Upper Left Incisor (21)", self.upper_left_incisor),
            ("Lower Right Incisor (41)", self.lower_right_incisor),
            ("Lower Left Incisor (31)", self.lower_left_incisor)
        ]
        
        for i, (label, var) in enumerate(measurements):
            row = i % 8
            col = i // 8 * 2
            ttk.Label(input_frame, text=label).grid(row=row, column=col, sticky=tk.W, padx=5, pady=2)
            ttk.Entry(input_frame, textvariable=var, width=8).grid(row=row, column=col+1, sticky=tk.W, padx=5, pady=2)
        
        # Buttons
        button_frame = ttk.Frame(scrollable_frame)
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        ttk.Button(button_frame, text="Calculate Space Requirements", command=self.calculate).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="Reset", command=self.reset).pack(side=tk.LEFT, padx=5)
        
        # Results frame
        results_frame = ttk.LabelFrame(scrollable_frame, text="Analysis Results", padding="15")
        results_frame.pack(fill=tk.BOTH, expand=True)
        
        self.results_text = tk.Text(results_frame, height=8, wrap=tk.WORD, font=('Arial', 10))
        self.results_text.pack(fill=tk.BOTH, expand=True)
        
    def create_info_tab(self):
        # Information tab
        info_tab = ttk.Frame(self.notebook)
        self.notebook.add(info_tab, text="Information")
        
        # Text widget with scrollbar
        text_frame = ttk.Frame(info_tab)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        text_scroll = ttk.Scrollbar(text_frame)
        text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        info_text = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=text_scroll.set, 
                          font=('Arial', 10), padx=10, pady=10)
        info_text.pack(fill=tk.BOTH, expand=True)
        
        text_scroll.config(command=info_text.yview)
        
        # Add information content
        info_content = """ROYAL LONDON SPACE ANALYSIS INFORMATION

Measurement Instructions:
1. Measure the mesiodistal width of each tooth at its greatest contour
2. Use a digital caliper or Boley gauge for accurate measurements
3. Record to the nearest 0.1 mm
4. Measure both left and right teeth (analysis divides by 2 automatically)

Parameters:
- Upper arch: Teeth 16-13, 12-22, 23-26 (FDI numbering)
- Lower arch: Teeth 46-43, 42-32, 33-36 (FDI numbering)
- Space Requirements = (Sum of tooth widths) / 2

Ideal Values (average mesiodistal widths in mm):
- Upper Molars (16,26): 10.5 mm
- Lower Molars (36,46): 11.0 mm
- Upper Premolars (14,15,24,25): 7.0 mm
- Lower Premolars (34,35,44,45): 7.0 mm
- Upper Canines (13,23): 7.6 mm
- Lower Canines (33,43): 6.5 mm
- Upper Incisors (11,12,21,22): 8.5 mm (central), 6.5 mm (lateral)
- Lower Incisors (31,32,41,42): 5.0 mm (central), 5.5 mm (lateral)

Interpretation Guidelines:
- Compare space requirements with available arch length
- Discrepancy = Space Required - Space Available
  - Positive: Space deficiency (crowding)
  - Negative: Space excess (spacing)
- Typical treatment thresholds:
  - 0-4mm: Mild crowding/spacing
  - 4-8mm: Moderate
  - >8mm: Severe

Clinical Significance:
- Helps determine:
  - Need for extractions
  - Amount of interproximal reduction (IPR) required
  - Arch expansion potential
  - Anchorage requirements
- Particularly valuable for:
  - Comprehensive treatment planning
  - Borderline extraction cases
  - Space management decisions

Treatment Planning Considerations:
For Crowding:
1. 0-4mm: Often manageable with IPR or slight proclination
2. 4-8mm: May require IPR + arch expansion or single extraction
3. >8mm: Typically requires bilateral extractions

For Spacing:
1. 0-4mm: Can often be closed with mechanics
2. 4-8mm: May require restorations or accept some spacing
3. >8mm: Significant restorative or prosthetic solutions needed

Common Findings:
- Upper arch often shows greater variability
- Lower incisor crowding is most common
- Asymmetrical discrepancies frequent
- Mixed dentition requires different analysis methods
"""
        info_text.insert(tk.END, info_content)
        info_text.config(state=tk.DISABLED)
    
    def calculate(self):
        try:
            # Calculate upper arch requirements
            upper_sum = (
                self.upper_right_molar.get() + self.upper_left_molar.get() +
                self.upper_right_premolar.get() + self.upper_left_premolar.get() +
                self.upper_right_canine.get() + self.upper_left_canine.get() +
                self.upper_right_incisor.get() + self.upper_left_incisor.get()
            )
            upper_requirement = upper_sum / 2
            
            # Calculate lower arch requirements
            lower_sum = (
                self.lower_right_molar.get() + self.lower_left_molar.get() +
                self.lower_right_premolar.get() + self.lower_left_premolar.get() +
                self.lower_right_canine.get() + self.lower_left_canine.get() +
                self.lower_right_incisor.get() + self.lower_left_incisor.get()
            )
            lower_requirement = lower_sum / 2
            
            # Generate results
            result_text = f"""ROYAL LONDON SPACE ANALYSIS RESULTS

Upper Arch:
- Total tooth material: {upper_sum:.1f} mm
- Space requirement (per side): {upper_requirement:.1f} mm

Lower Arch:
- Total tooth material: {lower_sum:.1f} mm
- Space requirement (per side): {lower_requirement:.1f} mm

CLINICAL INTERPRETATION:
These values represent the space needed to properly align the teeth.
Compare with available arch length to determine:
- Crowding (if space required > space available)
- Spacing (if space available > space required)

TYPICAL ARCH LENGTHS:
- Maxillary arch: ~32-36mm (canine to first molar)
- Mandibular arch: ~28-32mm (canine to first molar)
"""
            self.results_text.config(state=tk.NORMAL)
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, result_text)
            self.results_text.config(state=tk.DISABLED)
            
        except tk.TclError:
            messagebox.showerror("Error", "Please enter valid numbers for all fields")
    
    def reset(self):
        # Reset to ideal values
        ideal_values = {
            "upper_molar": 10.5, "lower_molar": 11.0,
            "upper_premolar": 7.0, "lower_premolar": 7.0,
            "upper_canine": 7.6, "lower_canine": 6.5,
            "upper_incisor": 8.5, "lower_incisor": 5.0
        }
        
        self.upper_right_molar.set(ideal_values["upper_molar"])
        self.upper_left_molar.set(ideal_values["upper_molar"])
        self.lower_right_molar.set(ideal_values["lower_molar"])
        self.lower_left_molar.set(ideal_values["lower_molar"])
        
        self.upper_right_premolar.set(ideal_values["upper_premolar"])
        self.upper_left_premolar.set(ideal_values["upper_premolar"])
        self.lower_right_premolar.set(ideal_values["lower_premolar"])
        self.lower_left_premolar.set(ideal_values["lower_premolar"])
        
        self.upper_right_canine.set(ideal_values["upper_canine"])
        self.upper_left_canine.set(ideal_values["upper_canine"])
        self.lower_right_canine.set(ideal_values["lower_canine"])
        self.lower_left_canine.set(ideal_values["lower_canine"])
        
        self.upper_right_incisor.set(ideal_values["upper_incisor"])
        self.upper_left_incisor.set(ideal_values["upper_incisor"])
        self.lower_right_incisor.set(ideal_values["lower_incisor"])
        self.lower_left_incisor.set(ideal_values["lower_incisor"])
        
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = RoyalLondonAnalysisApp(root)
    root.mainloop()