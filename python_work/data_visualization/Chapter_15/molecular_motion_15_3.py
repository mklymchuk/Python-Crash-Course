import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = RandomWalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    points_numbers = range(rw.num_points)
    ax.plot(
        rw.x_values, rw.y_values, linewidth = 1
        ) 
    
    # Emphasize the first and last points.
    ax.plot(0, 0, linewidth = 1)
    ax.plot(
        rw.x_values[-1], rw.y_values[-1],
        linewidth = 1
        )
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    
    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break