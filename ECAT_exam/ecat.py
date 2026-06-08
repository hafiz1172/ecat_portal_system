import time # Date aur Time record karne ke liye

# =====================================================================
# 1. CONSTANTS & STORAGE (In-Memory Data)
# =====================================================================
CORRECT_MARKS = 4
WRONG_MARKS = -1
SKIP_MARKS = 0

# Built-in Question Bank (List of Dictionaries)
questions = [
    {
   "id": 1,
        "subject": "Maths",
        "question": "What is 2 + 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "B"
    },{
        "id": 2,
        "subject": "Maths",
        "question": "What is 3/3?",
        "options": ["A) 1", "B) 4", "C) 5", "D) 6"],
        "answer": "A"
    },{
        "id": 3,
        "subject": "Maths",
        "question": "What is 4 x 4?",
        "options": ["A) 3", "B) 4", "C) 16", "D) 6"],
        "answer": "C"
    },{
        "id": 4,
        "subject": "Maths",
        "question": "What is 5 - 2?",
        "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
        "answer": "A"
    },{
        "id": 5,
        "subject": "chemistry",
        "question": "Molecule is ?",
        "options": ["A) atom", "B) group of atom", "C) independent ", "D) none"],
        "answer": "C"
    },{
        "id": 6,
        "subject": "English",
        "question": "What is noun?",
        "options": ["A) play", "B) happy", "C) excited", "D) chair"],
        "answer": "D"
    },{
        "id": 7,
        "subject": "English",
        "question": "What is verd?",
        "options": ["A) play", "B) happy", "C) excited", "D) chair"],
        "answer": "A"
    },{
        "id": 8,
        "subject": "Physics",
        "question": "Gravity is ?",
        "options": ["A) force", "B) work", "C) motion", "D) none"],
        "answer": "A"
    },{
        "id": 9,
        "subject": "Physics",
        "question": "formula of force is ",
        "options": ["A) m/a", "B) a/m", "C) ma", "D) none"],
        "answer": "C"
    },{
        "id": 10,
        "subject": "Physics",
        "question": "formula of work?",
        "options": ["A) Fd", "B) F/d", "C) d/F", "D) none"],
        "answer": "A"
    }
]

all_results = [] # Saare students ka result yahan save hoga

# =====================================================================
# 2. PORTAL 1: ADMIN SIDE FUNCTIONS
# =====================================================================

def admin_login():
    """Admin ka secure login system (3 attempts lockout)"""
    attempts = 0
    while attempts < 3:
        user = input("Enter Admin Username: ").strip()
        pwd = input("Enter Admin Password: ").strip()
        
        if user == "ecat_admin" and pwd == "ecat@2024":
            print("\nLogin Successful!")
            admin_menu() # Sahi login par menu khulega
            return
        else:
            attempts += 1
            print(f"Wrong username or password. Attempts left: {3 - attempts}")
            
    print("\nAccess Denied: Account Locked due to 3 failed attempts.")

def admin_menu():
    """Admin ka control center jahan se wo system chalaye ga"""
    while True:
        print("\n=== ECAT TEAM ADMIN PORTAL ===")
        print("1. View All Questions")
        print("2. Add New Question")
        print("3. Delete Question")
        print("4. View All Student Results")
        print("5. Logout")
        
        choice = input("Select an option (1-5): ").strip()
        
        if choice == "1":
            # 1. VIEW ALL QUESTIONS
            print("\n--- Current Question Bank ---")
            for idx in range(len(questions)):
                q = questions[idx]
                print(f"\nQ{idx+1} [Subject: {q['subject']}]: {q['question']}")
                for opt in q['options']:
                    print(opt)
                print(f"Correct Answer: {q['answer']}")
                
        elif choice == "2":
            # 2. ADD NEW QUESTION
            print("\n--- Add New MCQ ---")
            sub = input("Enter Subject: ")
            q_text = input("Enter Question: ")
            a = input("Option A: ")
            b = input("Option B: ")
            c = input("Option C: ")
            d = input("Option D: ")
            ans = input("Enter Correct Answer (A/B/C/D): ").strip().upper()
            
            new_q = {
                "id": len(questions) + 1,
                "subject": sub,
                "question": q_text,
                "options": [f"A) {a}", f"B) {b}", f"C) {c}", f"D) {d}"],
                "answer": ans
            }
            questions.append(new_q) # List me naya sawal jorna
            print("Question Added Successfully!")
            
        elif choice == "3":
            # 3. DELETE QUESTION
            print("\n--- Delete MCQ ---")
            num = int(input("Enter Question Number to Delete: "))
            if 0 < num <= len(questions):
                questions.pop(num - 1) # List se delete karna
                print("Question Deleted Successfully!")
            else:
                print("Invalid Question Number!")
                
        elif choice == "4":
            # 4. VIEW STUDENT RESULTS
            print("\n--- Student Results Summary ---")
            if not all_results:
                print("No student has taken the test yet.")
            for r in all_results:
                print(f"Name: {r['name']} | Roll No: {r['roll_no']} | Score: {r['score']} | Percentage: {r['percentage']}% | Grade: {r['grade']}")
                
        elif choice == "5":
            print("Logging out from Admin Portal...")
            break

# =====================================================================
# 3. PORTAL 2: STUDENT SIDE FUNCTIONS
# =====================================================================

def student_login():
    """Student Portal login aur info collection"""
    attempts = 0
    while attempts < 3:
        user = input("Enter Student Username: ").strip()
        pwd = input("Enter Student Password: ").strip()
        
        if user == "student" and pwd == "student123":
            print("\nLogin Successful!")
            name = input("Enter your Full Name: ").strip()
            roll = input("Enter your Roll Number: ").strip()
            student_menu(name, roll) # Name aur Roll number aagay pass karna
            return
        else:
            attempts += 1
            print(f"Wrong credentials. Attempts left: {3 - attempts}")
            
    print("\nAccess Denied.")

def student_menu(name, roll_no):
    """Student ka exam menu"""
    while True:
        print(f"\n=== STUDENT EXAM PORTAL (Welcome {name}) ===")
        print("1. View Exam Rules")
        print("2. Start Exam")
        print("3. Exit Portal")
        
        choice = input("Select an option (1-3): ").strip()
        
        if choice == "1":
            print("\n--- EXAM RULES & MARKING SCHEME ---")
            print(f"1. Total Questions: {len(questions)}")
            print(f"2. Correct Answer: +{CORRECT_MARKS} Marks")
            print(f"3. Wrong Answer: {WRONG_MARKS} Mark")
            print(f"4. Skip Question: Enter 'S' (0 Marks)")
            print("5. Type 'SUBMIT' anytime to end the exam early.")
            
        elif choice == "2":
            start_exam(name, roll_no) # Exam shuru karne ka function call
            break
        elif choice == "3":
            break

def start_exam(name, roll_no):
    """Exam lene aur calculation karne ka main engine"""
    student_answers = {} # Dictionary user ke answers save karne k liye
    correct_count = 0
    wrong_count = 0
    skipped_count = 0
    
    print("\n--- Exam Started! Good Luck ---")
    
    for idx in range(len(questions)):
        q = questions[idx]
        print(f"\nQuestion {idx+1}: {q['question']}")
        for opt in q['options']:
            print(opt)
            
        ans = input("Your Answer (A/B/C/D) or 'S' to Skip or 'SUBMIT': ").strip().upper()
        
        if ans == "SUBMIT":
            print("Submitting exam early...")
            break
            
        if ans == "S" or ans == "":
            student_answers[idx] = "S"
            skipped_count += 1
        else:
            student_answers[idx] = ans
            if ans == q['answer']:
                correct_count += 1
            else:
                wrong_count += 1
                
    # --- CALCULATIONS (Marking Engine) ---
    total_score = (correct_count * CORRECT_MARKS) + (wrong_count * WRONG_MARKS)
    max_marks = len(questions) * CORRECT_MARKS
    percentage = (total_score / max_marks) * 100
    
    # Grade Table
    if percentage >= 80: grade = "EXCELLENT"
    elif percentage >= 65: grade = "GOOD"
    elif percentage >= 50: grade = "AVERAGE"
    else: grade = "BELOW AVERAGE"
    
    # Save result dictionary in main list
    result_record = {
        "name": name, "roll_no": roll_no,
        "score": total_score, "percentage": round(percentage, 2), "grade": grade,
        "time": time.strftime("%Y-%m-%d %H:%M:%S") # Live timestamp
    }
    all_results.append(result_record)
    
    # Show Instant Result to Student
    print("\n===============================")
    print("        EXAM RESULT            ")
    print("===============================")
    print(f"Student Name : {name}")
    print(f"Roll Number  : {roll_no}")
    print(f"Total Marks  : {total_score} / {max_marks}")
    print(f"Percentage   : {round(percentage, 2)}%")
    print(f"Grade        : {grade}")
    print("===============================")

# =====================================================================
# 4. MAIN PROGRAM ENTRY POINT
# =====================================================================
while True:
    print("\n====== WELCOME TO ECAT EXAM APP ======")
    print("1. Admin Portal Login")
    print("2. Student Portal Login")
    print("3. Exit System")
    
    main_choice = input("Choose Portal (1-3): ").strip()
    
    if main_choice == "1":
        admin_login() # Call Admin system
    elif main_choice == "2":
        student_login() # Call Student system
    elif main_choice == "3":
        print("Thank you for using ECAT System. Goodbye!")
        break