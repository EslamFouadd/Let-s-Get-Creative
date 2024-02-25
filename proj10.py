import matplotlib.pyplot as plt

# Create a number line
plt.figure(figsize = (8, 1))
plt.axhline(y = 0, color = "black", linestyle = "-", linewidth = 2)
plt.xticks(range(-5, 6))
plt.yticks([])

# Mark positive and negative integers
for i in range(-5, 6):
    plt.text(i, 0.1, str(i), ha = "center", va = "bottom")
    
plt.title("Number Line (Integers)")
plt.xlabel("Integers")
plt.grid(axis = "x")
plt.show()

