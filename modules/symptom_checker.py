# modules/symptom_checker.py
import tkinter as tk
from tkinter import ttk, messagebox
# from modules.nlp_matcher import SymptomNLPMatcher

class SymptomChecker(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent , style='Custom.TFrame')
        self.controller = controller
        # self.nlp_matcher = SymptomNLPMatcher()

        self.symptom_database = {
            "fever": "You may have a viral infection or the flu.",
            "headache": "You might be experiencing a migraine or dehydration.",
            "cough": "You may have a cold or respiratory infection.",
            "sore throat": "You may have a throat infection or early flu.",
            "dizziness": "This could be due to low blood pressure or dehydration.",
            "fatigue": "You might be overworked, or it could be early signs of anemia.",
            "high fever": "Seek medical attention if fever exceeds 102°F.",
            "stomach ache": "Could be indigestion or a gastric issue.",
            "diarrhea": "You may be having food poisoning or stomach flu.",
            "rash": "Might be an allergic reaction or skin infection.",
            "chills": "Often accompanies fever or flu.",
            "breathing difficulty": "Could be asthma or a respiratory infection.",
            "loss of smell": "Common in viral infections, including COVID-19.",
            "nausea": "Might indicate motion sickness or gastritis.",
            "muscle pain": "You could be experiencing flu or physical fatigue.",
            "blurred vision": "Could indicate vision strain or neurological issues.",
            "ear pain": "Possibly an ear infection or sinus issue.",
            "vomiting": "Could be food poisoning or stomach infection.",
            "chest pain": "Possible heart or lung issue – seek urgent care.",
            "anxiety": "Could be emotional stress or mental health issue.",
            "back pain": "Might be posture-related or a muscle injury.",
            "sweating": "May indicate fever, anxiety, or hypoglycemia.",
            "shortness of breath": "Possibly asthma or panic attack.",
            "runny nose": "Usually a common cold or allergy.",
            "eye redness": "Could be conjunctivitis or irritation.",
            "itching": "Could be allergies or skin irritation.",
            "leg cramps": "May result from dehydration or mineral deficiency.",
            "joint pain": "Could be arthritis or viral fever.",
            "loss of appetite": "Often accompanies flu or stomach upset.",
        }

        self.symptom_list = list(self.symptom_database.keys())
        # Widgets
        ttk.Label(self, text="🩺 Symptom Checker", font=("Arial", 16)).pack(pady=10)

        ttk.Label(self, text="Select or enter symptoms(comma-separated):").pack()
        self.symptom_entry = ttk.Entry(self, width=60)
        self.symptom_entry.pack(pady=5)

        self.combo = ttk.Combobox(self, values=self.symptom_list)
        self.combo.set("Choose from common symptoms")
        self.combo.pack(pady=5)

        ttk.Button(self, text="Add to List", command=self.add_to_entry).pack(pady=3)

        ttk.Label(self, text="How long have you had these symptoms?").pack()
        self.duration_entry = ttk.Entry(self, width=60)
        self.duration_entry.pack(pady=5)

        ttk.Button(self, text="Check", command=self.check_symptoms).pack(pady=10)
        ttk.Button(self, text="Back", command=lambda: controller.show_frame("WelcomeScreen")).pack()

        self.result_text = tk.Text(self, height=12, width=80, wrap="word")
        self.result_text.pack(pady=10)

        # Add tags once for styling
        self.result_text.tag_config("user", foreground="blue", font=("Arial", 10, "bold"))
        self.result_text.tag_config("bot", foreground="darkgreen", font=("Arial", 10))

    def add_to_entry(self):
        selected = self.combo.get().strip().lower()
        existing = self.symptom_entry.get().strip()
        if selected and selected in self.symptom_list:
            new_text = f"{existing}, {selected}" if existing else selected
            self.symptom_entry.delete(0, tk.END)
            self.symptom_entry.insert(0, new_text)
            
    def check_symptoms(self):
        self.result_text.delete("1.0", tk.END)
        symptoms_input = self.symptom_entry.get().lower().strip()
        duration = self.duration_entry.get().strip()

        if not symptoms_input or not duration:
            messagebox.showwarning("Missing Info", "Please fill all fields.")
            return

        symptoms_entered = [s.strip() for s in symptoms_input.split(',')]
        found = 0
        urgent_flags = []
        messages = []

        self.result_text.insert(tk.END, f"👤 You: I've been having {symptoms_input} for {duration}.\n\n", "user")

        for symptom in symptoms_entered:
            if symptom in self.symptom_database:
                found += 1
                response = self.symptom_database[symptom]
                if any(critical in symptom for critical in ["high fever", "breathing difficulty", "blurred vision"]):
                    urgent_flags.append(symptom)
                messages.append(f"🩺 {symptom.title()}: {response}")
            else:
                messages.append(f"❗ {symptom.title()}:  Not recognized. Consider consulting a healthcare provider.")

        if found > 0:
            self.result_text.insert(tk.END, "🤖 Assistant:\n", "bot")
            for msg in messages:
                self.result_text.insert(tk.END, f"{msg}\n", "bot")

            self.result_text.insert(tk.END, "\n📋 Recommendation:\n", "bot")
            if urgent_flags:
                self.result_text.insert(tk.END, f"⚠️ These symptoms could be serious: {', '.join(urgent_flags)}.\n", "bot")
                self.result_text.insert(tk.END, "🚨 Please seek medical help immediately.\n", "bot")
            elif found >= 2:
                self.result_text.insert(tk.END, "💡 Multiple symptoms detected. Keep monitoring your condition closely.\n", "bot")
            else:
                self.result_text.insert(tk.END, "👍 Seems like a mild condition. Rest and hydration are key.\n", "bot")

        else:
            self.result_text.insert(tk.END, "🤖 Assistant: Sorry, I couldn't identify the symptoms. Please recheck or contact a doctor.\n", "bot")

        self.result_text.tag_config("user", foreground="blue", font=("Arial", 10, "bold"))
        self.result_text.tag_config("bot", foreground="darkgreen", font=("Arial", 10))
        