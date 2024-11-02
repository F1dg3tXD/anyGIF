import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import subprocess
import os
import re

# Path to ffmpeg executable
FFMPEG_PATH = "./bin/ffmpeg"

# Function to convert video to GIF with progress
def convert_to_gif():
    if not source_video_path.get() or not output_dir.get() or not output_name.get():
        messagebox.showerror("Error", "Please select a source video, output directory, and provide a name for the GIF.")
        return
    
    output_path = os.path.join(output_dir.get(), f"{output_name.get()}.gif")
    resolution = f"{width.get()}x{height.get()}"
    framerate = frame_rate.get()
    
    # Build ffmpeg command
    command = [
        FFMPEG_PATH, "-i", source_video_path.get(), "-vf",
        f"fps={framerate},scale={resolution}", "-loop", "0", output_path
    ]

    # Execute ffmpeg command and capture the output for progress
    process = subprocess.Popen(command, stderr=subprocess.PIPE, universal_newlines=True)
    for line in process.stderr:
        # Parse progress based on duration
        match = re.search(r"time=(\d+:\d+:\d+\.\d+)", line)
        if match:
            # Update progress bar
            update_progress(match.group(1))
    
    process.wait()
    progress_bar["value"] = 100
    messagebox.showinfo("Success", f"GIF created at: {output_path}")

# Function to update progress bar based on ffmpeg time output
def update_progress(current_time):
    # Example: Convert hh:mm:ss.ms to total seconds
    h, m, s = map(float, current_time.split(":"))
    elapsed_seconds = h * 3600 + m * 60 + s
    total_duration = duration.get()
    
    if total_duration > 0:
        progress = (elapsed_seconds / total_duration) * 100
        progress_bar["value"] = progress
        root.update_idletasks()

# Function to browse for source video and calculate duration
def browse_source_video():
    filename = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.mkv;*.mov")])
    source_video_path.set(filename)
    
    # Get video duration
    result = subprocess.run([FFMPEG_PATH, "-i", filename], stderr=subprocess.PIPE, universal_newlines=True)
    match = re.search(r"Duration: (\d+):(\d+):(\d+.\d+)", result.stderr)
    if match:
        h, m, s = map(float, match.groups())
        duration.set(h * 3600 + m * 60 + s)

# Function to select output directory
def browse_output_directory():
    directory = filedialog.askdirectory()
    output_dir.set(directory)

# Initialize main window
root = tk.Tk()
root.title("anyGIF")
root.configure(bg="#2E2E2E")

# Set the application icon
icon_path = "res/winIcon.ico"
try:
    root.iconphoto(False, tk.PhotoImage(file=icon_path))
except Exception as e:
    print(f"Error loading icon: {e}")

# Initialize StringVars
source_video_path = tk.StringVar()
output_dir = tk.StringVar()
output_name = tk.StringVar(value="output")
width = tk.IntVar(value=320)
height = tk.IntVar(value=240)
frame_rate = tk.IntVar(value=15)
duration = tk.DoubleVar(value=0.0)  # Store video duration in seconds

# UI Elements
tk.Label(root, text="Source Video:", fg="white", bg="#2E2E2E").grid(row=0, column=0, sticky="w")
tk.Entry(root, textvariable=source_video_path, width=40).grid(row=0, column=1)
tk.Button(root, text="Browse", command=browse_source_video).grid(row=0, column=2)

tk.Label(root, text="Output Directory:", fg="white", bg="#2E2E2E").grid(row=1, column=0, sticky="w")
tk.Entry(root, textvariable=output_dir, width=40).grid(row=1, column=1)
tk.Button(root, text="Browse", command=browse_output_directory).grid(row=1, column=2)

tk.Label(root, text="Output Name:", fg="white", bg="#2E2E2E").grid(row=2, column=0, sticky="w")
tk.Entry(root, textvariable=output_name, width=40).grid(row=2, column=1)

tk.Label(root, text="Width:", fg="white", bg="#2E2E2E").grid(row=3, column=0, sticky="w")
tk.Entry(root, textvariable=width, width=10).grid(row=3, column=1, sticky="w")

tk.Label(root, text="Height:", fg="white", bg="#2E2E2E").grid(row=4, column=0, sticky="w")
tk.Entry(root, textvariable=height, width=10).grid(row=4, column=1, sticky="w")

tk.Label(root, text="Framerate (fps):", fg="white", bg="#2E2E2E").grid(row=5, column=0, sticky="w")
tk.Entry(root, textvariable=frame_rate, width=10).grid(row=5, column=1, sticky="w")

tk.Button(root, text="Convert to GIF", command=convert_to_gif, bg="#4CAF50", fg="white").grid(row=6, column=1)

# Progress bar
progress_bar = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress_bar.grid(row=7, column=1, pady=10)

# Run the main loop
root.mainloop()
