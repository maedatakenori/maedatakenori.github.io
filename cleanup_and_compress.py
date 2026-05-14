import os
import sys
import shutil

try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Installing...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image

image_dir = r"d:\My_Art_Project\artist-site\assets\images"
lumen_backup_dir = r"d:\My_Art_Project\Lumen_Originals"
site_dir = r"d:\My_Art_Project\artist-site"

# サイトで使用中の画像（圧縮対象）
images_to_compress = [
    "untitled-lumen-prize-next-side1.jpg",
    "untitled-lumen-prize-next-side2.jpg",
    "untitled-lumen-prize-next-front.jpg",
    "untitled-lumen-prize-next-receipt-full.jpg",
    "untitled-lumen-prize-receipt-full.jpg",
    "untitled-lumen-prize-up-1.jpg",
    "untitled-lumen-prize-up-2.jpg",
    "untitled-lumen-prize-front.jpg"
]

# サイトでは未使用だが、Lumen応募用に保存してから削除する画像
images_to_backup_then_delete = [
    "takenorimaeda.jpeg",
    "combined_image.png",
    "untitle.webp",
    "untitle1.jpg",
    "reuntitle-Lumen Prize.jpg",
    "untitle Lumen Prize 全面（仮）.jpg",
    "untitle Lumen-Prize-next-レシート横.jpg",
    "untitle-Lumen Prize(1).jpg",
    "untitle-Lumen-Prize-レシート横.jpg",
    "Execution Protoco0403ljpegglitchshoot 3.png",
    "Execution Protoco0403ljpegglitchshoot1.png",
    "Execution Protocoljpegglitchshoot .png",
    "Execution Protocoljpegglitchshoot 1.png",
    "Execution Protocoljpegglitchshoot 2.png",
    "Execution Protocoljpegglitchshoot3.png",
]

# 単純に削除してよいスクリプト類
scripts_to_delete = [
    "copy_image.bat",
    "copy_images.bat",
    "copy_portrait.bat",
    "rename_images.py",
]

max_size = 2000

print("--- Step 1: Backing up original images for Lumen Prize ---")
if not os.path.exists(lumen_backup_dir):
    os.makedirs(lumen_backup_dir)
    print(f"Created backup directory: {lumen_backup_dir}")

# 使用中の画像も念のためバックアップ
all_images_to_backup = images_to_compress + images_to_backup_then_delete

for img_name in all_images_to_backup:
    src_path = os.path.join(image_dir, img_name)
    dst_path = os.path.join(lumen_backup_dir, img_name)
    if os.path.exists(src_path):
        if not os.path.exists(dst_path):
            shutil.copy2(src_path, dst_path)
            print(f"Backed up: {img_name}")
    else:
        print(f"File not found for backup: {img_name}")

print("\n--- Step 2: Compressing images for the website ---")
# サイトディレクトリ内の画像を上書き圧縮（HTMLの変更を避けるため）
for img_name in images_to_compress:
    img_path = os.path.join(image_dir, img_name)
    if os.path.exists(img_path):
        try:
            print(f"Processing {img_name}...")
            img = Image.open(img_path)
            
            width, height = img.size
            if width > max_size or height > max_size:
                if width > height:
                    new_width = max_size
                    new_height = int(max_size * height / width)
                else:
                    new_height = max_size
                    new_width = int(max_size * width / height)
                
                print(f"  Resizing from {width}x{height} to {new_width}x{new_height}")
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            img.save(img_path, "JPEG", quality=80, optimize=True)
            new_size = os.path.getsize(img_path) / 1024
            print(f"  Saved {img_name} ({new_size:.1f} KB)")
        except Exception as e:
            print(f"  Error processing {img_name}: {e}")

print("\n--- Step 3: Cleaning up artist-site directory ---")
for file_name in images_to_backup_then_delete + scripts_to_delete:
    file_path = os.path.join(image_dir, file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"Deleted from site (backed up): {file_name}")
        except Exception as e:
            print(f"Error deleting {file_name}: {e}")

# スクリプト自身の削除
old_script = os.path.join(site_dir, "compress.py")
if os.path.exists(old_script):
    os.remove(old_script)

print("\nAll done! Your original images are safe in: " + lumen_backup_dir)
print("The artist-site directory is now clean and ready for GitHub Pages deployment.")
