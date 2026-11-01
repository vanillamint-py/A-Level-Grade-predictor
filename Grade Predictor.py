import tkinter as tk 

window = tk.Tk()
window.title("A level Grade predictor") 
window.geometry("600x600")
window.config(bg="#FCEF91")

subjects = ["Mathematics", "Chemistry", "Physics", "English General Paper", "Biology", "Computer science"]
subjectstates = {sub: False for sub in subjects}
subjectbuttons = {}
scoreentries = {}

def choosesubject(subjectname):
    subjectstates[subjectname] = not subjectstates[subjectname]
    if subjectstates[subjectname]:
        subjectbuttons[subjectname].config(bg="#C3B1E1")
    else:
        subjectbuttons[subjectname].config(bg="#FFFFFF")

lable = tk.Label(window, text="Enter your chosen subjects", font=("Arial",16,"bold"), bg="#FCEF91")
lable.pack(pady=(40,20))

for i in subjects:
    button = tk.Button(
        window, 
        text=i,
        font=("Arial",12),
        relief="raised",
        bd=2,
        bg="#FFFFFF",
        command=lambda s=i: choosesubject(s)
        )
    button.pack(pady=6)
    subjectbuttons[i] = button

def proceed():
    chosensubjects = [sub for sub, selected in subjectstates.items() if selected]
    print("subjects chosen :", chosensubjects)
    
    if not chosensubjects:
        return
    
    for widget in window.winfo_children():
        widget.destroy()
    
    window.config(bg="#FCEF91")
    
    scoretitle = tk.Label(window, text="Enter your overall score (%)", font=("Arial",16,"bold"), bg="#FCEF91")
    scoretitle.pack(pady=(40,20))
    
    for sub in chosensubjects:
        rowframe = tk.Frame(window, bg="#FCEF91")
        rowframe.pack(pady=10)
        sublabel = tk.Label(rowframe, text=f"{sub}: ", bg="#FCEF91", font=("Arial",12), width=22, anchor="w")
        sublabel.pack(side="left")
        scoreentry = tk.Entry(rowframe, width=8, justify="center", font=("Arial",12))
        scoreentry.pack(side="left", padx=10)
        scoreentries[sub] = scoreentry
        
    predictbutton = tk.Button(window, text="Predict grade", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=prediction)
    predictbutton.pack(side="bottom", pady=40)

def prediction():
    if hasattr(prediction, "result_frame"):
        prediction.result_frame.destroy()
        
    prediction.result_frame = tk.Frame(window, bg="#FCEF91")
    prediction.result_frame.pack(side="bottom", pady=10)
    
    for sub, entry in scoreentries.items():
        try:
            scoretext = entry.get().strip()
            if not scoretext:
                raise ValueError("Empty")
            score = float(scoretext)
            
            if score >= 90 and score <= 100:
                grade = "A*"
            elif score >= 80:
                grade = "A"
            elif score >= 70:
                grade = "B"
            elif score >= 60:
                grade = "C" 
            elif score >= 50:
                grade = "D"
            elif score >= 40:
                grade = "E" 
            elif score < 40 and score >=0:
                grade = "U"
            resulttext = f"{sub}: {grade}"
            textcolour = "#2E7D32"
        except ValueError:
            resulttext = f"{sub: Please enter a valid number.}"
            textcolour = "#C62828"
    
        grade_label = tk.Label(
            prediction.result_frame, 
            text=resulttext,
            bg="#FCEF91", 
            font=("Arial", 12, "bold"),
            fg=textcolour
        )
        grade_label.pack(pady=2)

nextbutton = tk.Button(window, text="Continue -->", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white", command=proceed)
nextbutton.pack(side="bottom", pady=40)

window.mainloop()

