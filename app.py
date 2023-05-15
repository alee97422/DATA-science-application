
#This is an app i am developing that will in the end will create a wide variety 
#of data science and analysis tools all in one place and at the click of a 
#button
# so far my vision for this app so far is:
# - read collumn values in csv files
# - store these values as an array
# - have this array be visualized as  filter options
#   in order for end user to use this function to compare differnt collumns of data
#   part of this will be outputing several graphs and charts to suggest quick easy plots charts 
#   for visualization stage in mind
# add functionlity to change data types and clean data



import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create Tkinter window
window = tk.Tk()
window.geometry("800x600")
window.configure(bg="#212121")  # Set background color for dark mode

# Set a custom dark mode theme
window.tk_setPalette(background='#212121', foreground='white',
                     activeBackground='#3a3a3a', activeForeground='white')

# Create a frame for the file upload widget
upload_frame = tk.Frame(window, bg="#212121")
upload_frame.pack(pady=20)

# Create a dropdown menu for column selection
column_var = tk.StringVar(window)
column_var.set("Select Column")  # Set default text for dropdown menu
column_dropdown = tk.OptionMenu(window, column_var, [])
column_dropdown.pack(pady=10)

# Create a second dropdown menu for column selection
column_var2 = tk.StringVar(window)
column_var2.set("Select Column")  # Set default text for the second dropdown menu
column_dropdown2 = tk.OptionMenu(window, column_var2, [])
column_dropdown2.pack(pady=10)

# Create a third dropdown menu for column selection
column_var3 = tk.StringVar(window)
column_var3.set("Select Column")  # Set default text for the third dropdown menu
column_dropdown3 = tk.OptionMenu(window, column_var3, [])
column_dropdown3.pack(pady=10)

# Create a Label for max data points of column 1
max_data_points_col1_label = tk.Label(window, text="Max Data Points (Column 1):")
max_data_points_col1_label.pack()

# Create an Entry widget for max data points of column 1
max_data_points_col1_entry = tk.Entry(window)
max_data_points_col1_entry.pack()

# Create a Label for max data points of column 2
max_data_points_col2_label = tk.Label(window, text="Max Data Points (Column 2):")
max_data_points_col2_label.pack()

# Create an Entry widget for max data points of column 2
max_data_points_col2_entry = tk.Entry(window)
max_data_points_col2_entry.pack()

# Create a Label for max data points of column 3
max_data_points_col3_label = tk.Label(window, text="Max Data Points (Column 3):")
max_data_points_col3_label.pack()

# Create an Entry widget for max data points of column 3
max_data_points_col3_entry = tk.Entry(window)
max_data_points_col3_entry.pack()

# Create a frame for the plots
plot_frame = tk.Frame(window, bg="#212121")


def upload_csv():
    global column_names, csv_data
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv')])
    if file_path:
        df = pd.read_csv(file_path)
        column_names = df.columns.tolist()
        csv_data = df.values.tolist()

        print("File uploaded and processed successfully")
        print("Column Names:", column_names)
        print("CSV Data:", csv_data)


# Create button to upload CSV file
upload_button = tk.Button(upload_frame, text="Upload CSV", command=upload_csv, bg="#757575", fg="white")
upload_button.pack(side="left")


def retrieve_column_names():
    global column_names, selected_column_1, selected_column_2, selected_column_3
    if column_names:
        selected_column_1 = column_var.get()
        selected_column_2 = column_var2.get()
        selected_column_3 = column_var3.get()
        print("Column Names retrieved successfully")
        print("Selected Column 1:", selected_column_1)
        print("Selected Column 2:", selected_column_2)
        print("Selected Column 3:", selected_column_3)

        # Update dropdown menus
        column_dropdown['menu'].delete(0, 'end')
        column_dropdown2['menu'].delete(0, 'end')
        column_dropdown3['menu'].delete(0, 'end')

        for column in column_names:
            column_dropdown['menu'].add_command(label=column, command=tk._setit(column_var, column))
            column_dropdown2['menu'].add_command(label=column, command=tk._setit(column_var2, column))
            column_dropdown3['menu'].add_command(label=column, command=tk._setit(column_var3, column))

    else:
        print("No CSV file loaded yet")

# Create button to retrieve column names
retrieve_button = tk.Button(upload_frame, text="Retrieve Column Names", command=retrieve_column_names, bg="#757575", fg="white")
retrieve_button.pack(side="left")


def clear_graphs():
    global selected_column_1, selected_column_2, selected_column_3, max_data_points_col1, max_data_points_col2, max_data_points_col3

    selected_column_1 = None
    selected_column_2 = None
    selected_column_3 = None
    max_data_points_col1 = None
    max_data_points_col2 = None
    max_data_points_col3 = None

    # Clear dropdown selections
    column_var.set("Select Column")
    column_var2.set("Select Column")
    column_var3.set("Select Column")

    # Clear entry values
    max_data_points_col1_entry.delete(0, 'end')
    max_data_points_col2_entry.delete(0, 'end')
    max_data_points_col3_entry.delete(0, 'end')

    # Clear existing plots
    for widget in plot_frame.winfo_children():
        widget.destroy()


# Create button to clear dropdown menus
clear_button = tk.Button(upload_frame, text="Clear", command=clear_graphs, bg="#757575", fg="white")
clear_button.pack(side="left")


def generate_visualizations():
    global selected_column_1, selected_column_2, selected_column_3, csv_data, column_names, max_data_points_col1, max_data_points_col2, max_data_points_col3

    selected_column_1 = column_var.get()
    selected_column_2 = column_var2.get()
    selected_column_3 = column_var3.get()

    if selected_column_1 != "Select Column" and selected_column_2 != "Select Column":
        if csv_data:
            df = pd.DataFrame(csv_data, columns=column_names)

            max_data_points_col1_str = max_data_points_col1_entry.get()
            max_data_points_col2_str = max_data_points_col2_entry.get()

            if max_data_points_col1_str.isdigit() and max_data_points_col2_str.isdigit():
                max_data_points_col1 = int(max_data_points_col1_str)
                max_data_points_col2 = int(max_data_points_col2_str)

                df_col1 = df[selected_column_1].head(max_data_points_col1)
                df_col2 = df[selected_column_2].head(max_data_points_col2)

                # Clear existing plots
                for widget in plot_frame.winfo_children():
                    widget.destroy()

                # Plot scatter plot
                fig = plt.figure(figsize=(12, 8))

                # Plot scatter plot
                ax1 = fig.add_subplot(211)
                ax1.scatter(df_col1, df_col2)
                ax1.set_xlabel(selected_column_1)
                ax1.set_ylabel(selected_column_2)
                ax1.set_title("Scatter Plot")

                # Plot line chart
                ax2 = fig.add_subplot(223)
                ax2.plot(df_col2)
                ax2.set_xlabel("Index")
                ax2.set_ylabel(selected_column_2)
                ax2.set_title("Line Chart")

                if selected_column_3 != "Select Column":
                    max_data_points_col3_str = max_data_points_col3_entry.get()
                    if max_data_points_col3_str.isdigit():
                        max_data_points_col3 = int(max_data_points_col3_str)
                        df_col3 = df[selected_column_3].head(max_data_points_col3)

                        # Add a 3D scatter plot
                        ax3 = fig.add_subplot(224, projection='3d')
                        ax3.scatter(df_col1, df_col2, df_col3)
                        ax3.set_xlabel(selected_column_1)
                        ax3.set_ylabel(selected_column_2)
                        ax3.set_zlabel(selected_column_3)
                        ax3.set_title("3D Scatter Plot")

                # Adjust subplot spacing
                plt.subplots_adjust(hspace=0.5, wspace=0.3)

                # Create a FigureCanvasTkAgg widget
                plot_canvas = FigureCanvasTkAgg(fig, master=plot_frame)
                plot_canvas.draw()
                plot_canvas.get_tk_widget().pack()

                # Disable the Go button
                go_button.config(state=tk.DISABLED)

            else:
                print("Max Data Points should be valid integers")
        else:
            print("No CSV file loaded yet")
    else:
        print("Please select at least two columns from the dropdown menus")


# Create a "Go" button
go_button = tk.Button(window, text="Go", command=generate_visualizations, bg="#757575", fg="white")
go_button.pack(pady=20)

plot_frame = tk.Frame(window, bg="#212121")
plot_frame.pack(pady=20)

# Create a "Go" button
go_button = tk.Button(window, text="Go", command=generate_visualizations, bg="#757575", fg="white")
go_button.pack(pady=20)

# Create a "Clear" button
clear_button = tk.Button(window, text="Clear", command=clear_graphs, bg="#757575", fg="white")
clear_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()

