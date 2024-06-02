from tkinter import *

root = Tk()
root.geometry("800x600")
root.title("VOTING")

# Function to enable scrolling
def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

# Create a frame to contain the scrollable content
scroll_frame = Frame(root)

# Add a Canvas widget for scrolling
canvas = Canvas(scroll_frame, bg="white", width=780, height=480)
scrollbar = Scrollbar(scroll_frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Bind mousewheel event to scroll
canvas.bind_all("<MouseWheel>", on_mousewheel)

# Create and pack elements inside the scrollable frame
sample_label = Label(scrollable_frame, text="DIGITAL VOTING", foreground="Orange", font="times 40 bold")
sample_label.pack()

buttons_frame = Frame(scrollable_frame)

button1 = Button(buttons_frame, text="Electors", bg="Pale green", fg="white", font="Arial 15 bold", width=10)
button1.grid(row=1, column=0, padx=10, pady=10)

button2 = Button(buttons_frame, text="Candidates", bg="Purple", fg="white", font="Arial 15 bold", width=10)
button2.grid(row=1, column=1, padx=10, pady=10)

button3 = Button(buttons_frame, text="Management", bg="Red", fg="white", font="Arial 15 bold", width=10)
button3.grid(row=4, column=0, padx=10, pady=10)

button4 = Button(buttons_frame, text="Voter Details", bg="Sky blue", fg="white", font="Arial 15 bold", width=10)
button4.grid(row=4, column=1, padx=10, pady=10)

buttons_frame.pack(pady=20)

sample_label2 = Label(scrollable_frame, text="ABOUT US", foreground="Black", font="times 30 bold")
sample_label2.pack()

about_text = """E-voting, or electronic voting, is a method of casting votes using electronic means,
typically over the internet or through specialized voting machines. It offers several potential advantages 
over traditional paper-based voting systems, including increased accessibility, faster tabulation of results,
and potentially reduced costs."""  # To create a long enough text for scrolling

about_label = Label(scrollable_frame, text=about_text, foreground="Black", font="times 20")
about_label.pack()

voting_details_label = Label(scrollable_frame, text="Voting Details", foreground="Black", font="times 30 bold")
voting_details_label.pack()

voting_details_text = """E-voting, or electronic voting, is a method of casting votes using electronic means,
typically over the internet or through specialized voting machines. It offers several potential advantages 
over traditional paper-based voting systems, including increased accessibility, faster tabulation of results,
and potentially reduced costs."""   # To create a long enough text for scrolling

voting_details_label = Label(scrollable_frame, text=voting_details_text, foreground="Black", font="times 20")
voting_details_label.pack()

# Pack the scrollbar and canvas
canvas.pack( fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

scroll_frame.pack(fill="both", expand=True)

root.mainloop()
