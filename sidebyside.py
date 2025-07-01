import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def attach_images_side_by_side(img_path1, img_path2, output_path):
    img1 = Image.open(img_path1)
    img2 = Image.open(img_path2)
    max_height = max(img1.height, img2.height)

    def resize_to_height(img, height):
        w, h = img.size
        new_w = int(w * (height / h))
        return img.resize((new_w, height), Image.ANTIALIAS)

    img1_resized = resize_to_height(img1, max_height)
    img2_resized = resize_to_height(img2, max_height)
    total_width = img1_resized.width + img2_resized.width
    new_img = Image.new('RGB', (total_width, max_height))
    new_img.paste(img1_resized, (0, 0))
    new_img.paste(img2_resized, (img1_resized.width, 0))

    # Strip metadata by creating a new Image object and only copying pixel data
    data = list(new_img.getdata())
    clean_img = Image.new(new_img.mode, new_img.size)
    clean_img.putdata(data)
    clean_img.save(output_path)

def select_file(entry):
    filename = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All files", "*.*")]
    )
    if filename:
        entry.delete(0, tk.END)
        entry.insert(0, filename)

def select_save_path(entry):
    filename = filedialog.asksaveasfilename(
        defaultextension=".jpg",
        filetypes=[("JPEG Image", "*.jpg"), ("PNG Image", "*.png"), ("All files", "*.*")]
    )
    if filename:
        entry.delete(0, tk.END)
        entry.insert(0, filename)

def run():
    img1 = entry_img1.get()
    img2 = entry_img2.get()
    out = entry_output.get()
    if not img1 or not img2 or not out:
        messagebox.showerror("Error", "Please select all input and output files.")
        return
    try:
        attach_images_side_by_side(img1, img2, out)
        messagebox.showinfo("Success", f"Saved combined image to {out} (metadata removed)")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to combine images: {e}")

root = tk.Tk()
root.title("Attach Images Side by Side (No Metadata)")

tk.Label(root, text="Image 1:").grid(row=0, column=0, sticky="e")
entry_img1 = tk.Entry(root, width=40)
entry_img1.grid(row=0, column=1)
tk.Button(root, text="Browse...", command=lambda: select_file(entry_img1)).grid(row=0, column=2)

tk.Label(root, text="Image 2:").grid(row=1, column=0, sticky="e")
entry_img2 = tk.Entry(root, width=40)
entry_img2.grid(row=1, column=1)
tk.Button(root, text="Browse...", command=lambda: select_file(entry_img2)).grid(row=1, column=2)

tk.Label(root, text="Output:").grid(row=2, column=0, sticky="e")
entry_output = tk.Entry(root, width=40)
entry_output.grid(row=2, column=1)
tk.Button(root, text="Save as...", command=lambda: select_save_path(entry_output)).grid(row=2, column=2)

tk.Button(root, text="Combine Images", command=run).grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()