import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Stick Figure Game")

# Set the window size and position
window.geometry("400x400+200+200")

# Create a canvas to draw the stick figure and graphics on
canvas = tk.Canvas(window, width=400, height=400)
canvas.pack()

# Create the stick figure
stick_figure = canvas.create_rectangle(200, 350, 210, 360, fill="black")
stick_figure_arms = canvas.create_line(195, 360, 215, 360)
stick_figure_legs = canvas.create_line(200, 365, 190, 375, 210, 375)

# Create some graphics to collect
graphic1 = canvas.create_oval(100, 100, 120, 120, fill="red")
graphic2 = canvas.create_oval(300, 300, 320, 320, fill="blue")

# Create a label to display the objective
objective_label = tk.Label(text="Collect all the graphics!")
objective_label.pack()

# Create a list to track the collected graphics
collected_graphics = []

# Create a function to move the stick figure
def move_stick_figure(event):
  # Get the current position of the stick figure
  x1, y1, x2, y2 = canvas.coords(stick_figure)
  # Move the stick figure based on the key pressed
  if event.keysym == "Up":
    canvas.coords(stick_figure, x1, y1-5, x2, y2-5)
  elif event.keysym == "Down":
    canvas.coords(stick_figure, x1, y1+5, x2, y2+5)
  elif event.keysym == "Left":
    canvas.coords(stick_figure, x1-5, y1, x2-5, y2)
  elif event.keysym == "Right":
    canvas.coords(stick_figure, x1+5, y1, x2+5, y2)
  # Update the arms and legs to match the new position
  canvas.coords(stick_figure_arms, x1-5, y2, x2+5, y2)
  canvas.coords(stick_figure_legs, x1, y2+5, x1-10, y2+15, x2+10, y2+15)
  # Check if the stick figure has collected any graphics
  if canvas.coords(stick_figure).intersects(canvas.coords(graphic1)) and graphic1 not in collected_graphics:
    # Add the graphic to the collected graphics list
    collected_graphics.append(graphic1)
    # Remove the graphic from the canvas
    canvas.delete(graphic1)
  if canvas.coords(stick_figure).intersects(canvas.coords(graphic2)) and graphic2 not in collected_graphics:
    collected_graphics.append(graphic2)
    canvas.delete(graphic2)
  # Check if all graphics have been collected
  if len(collected_graphics) == 2:
    objective_label.config(text="You win!")

# Bind the arrow keys to the move function
window.bind("<Up>", move_stick_figure)
window.bind("<Down>", move_stick_figure)
window.bind("<Left>", move_stick_figure)
window.bind("<Right>", move_stick_figure)

# Run the main loop
window.mainloop()
