import tkinter as tk  # Import the Tkinter library
import random  # Import the random module

# Create a list of possible answers
answers = ["Yes, go for it!",
    "No, it might not be the best idea.",
    "It's up to you, but consider the potential consequences.",
    "If it aligns with your values and goals, then go for it.",
    "It depends on the specifics of the situation.",
    "It might be worth considering other options first.",
    "It could be a good opportunity, but make sure you weigh the pros and cons.",
    "If you feel confident and prepared, then go for it.",
    "It could be a great decision, but make sure you have a plan in place.",
    "It might not be the right choice for you at this time.",
    "It could be a risky move, but the potential reward could be worth it.",
    "It's ultimately your decision, but make sure you think it through carefully.",
    "If it aligns with your long-term goals, then go for it.",
    "It could be a great opportunity, but be prepared for the challenges that may come with it.",
    "It's up to you, but make sure you have the necessary resources and support.",
    "If it aligns with your values and beliefs, then go for it.",
    "It could be a good decision, but make sure you have a backup plan in case things don't go as expected.",
    "It's ultimately your decision, but consider the potential risks and rewards.",
    "If you feel passionate about it, then go for it.",
    "It could be a great opportunity, but make sure you have a clear plan in place.",
    "It's up to you, but consider the potential impact on your personal and professional life.",
    "If it aligns with your long-term goals and values, then go for it.",
    "It could be a good decision, but make sure you have the necessary resources and support.",
    "It's ultimately your decision, but consider the potential consequences.",
    "It's up to you, but make sure you have a plan in place.",
    "Make sure you have a clear understanding of the task at hand before making a decision.",
    "It's important to consider the potential impact on others before making a decision.",
    "It might be a good idea to get a second opinion before deciding.",
    "Think about how this decision will affect your future goals and plans.",
    "It's okay to take some time to think it through before making a decision.",
    "Make sure you fully understand the implications of this decision before proceeding.",
    "Consider the potential risks and rewards before making a decision.",
    "It might be helpful to consult with others who have experience with a similar situation.",
    "Make sure you have all the information you need before making a decision.",
    "Think about how this decision aligns with your values and beliefs.",
    "It's important to consider the potential long-term effects of this decision.",
    "Make sure you have a clear understanding of the task at hand before deciding.",
    "Consider the potential risks and rewards before making a decision."]

def get_answer():
  # Get a random answer from the list
  answer = random.choice(answers)
  # Set the text of the label to the answer
  label.config(text=answer)

# Create the main window
window = tk.Tk()
# Get the width and height of the screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate the position of the window on the screen
x_coord = (screen_width / 2) - (300 / 2)
y_coord = (screen_height / 2) - (500 / 2)

# Set the size and position of the window
window.geometry("300x500+{}+{}".format(int(x_coord), int(y_coord)))
# Set the window title
window.title("Should I Do It?")

# Create a label to display the answer
label = tk.Label(window, text="")
label.pack(side="top", fill="both", expand=True)
# Create a button to get a new answer
button = tk.Button(window, text="Get Answer", command=get_answer)

# Use the grid layout manager to place the label and button
label.grid(row=0, column=0,columnspan=2)
button.grid(row=1, column=0, columnspan=2)

# Run the Tkinter event loop
window.mainloop()

