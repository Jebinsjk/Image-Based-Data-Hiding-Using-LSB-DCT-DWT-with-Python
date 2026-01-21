import matplotlib.pyplot as plt
import cv2
import os

# List of image names (without path)
image_names = ["image1.jpg", "BC876E45-B40C-4CE6-80BA-8BC0E3048BBB.jpeg",
               "9DFCE638-586B-43AD-B721-DF187108470F.png"]

# Loop through all images
for name in image_names:
    try:
        # Paths
        original_path = os.path.join("Original_image", name)
        lsb_path = os.path.join("Encoded_image", "lsb_" + name)
        dct_path = os.path.join("Encoded_image", "dct_" + name)
        dwt_path = os.path.join("Encoded_image", "dwt_" + name)  # 👈 NEW

        # Read images
        original = cv2.imread(original_path)
        lsb = cv2.imread(lsb_path)
        dct = cv2.imread(dct_path)
        dwt = cv2.imread(dwt_path)  # 👈 NEW

        # Skip if any image missing
        if original is None or lsb is None or dct is None or dwt is None:
            print(
                f"Skipping {name} — one or more encoded images not found.")
            continue

        # Convert BGR → RGB
        original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
        lsb = cv2.cvtColor(lsb, cv2.COLOR_BGR2RGB)
        dct = cv2.cvtColor(dct, cv2.COLOR_BGR2RGB)
        dwt = cv2.cvtColor(dwt, cv2.COLOR_BGR2RGB)  # 👈 NEW

        # Plot side-by-side comparison
        fig, axs = plt.subplots(1, 4, figsize=(20, 6))  # 👈 4 columns now

        titles = ["ORIGINAL", "LSB", "DCT", "DWT"]
        images = [original, lsb, dct, dwt]

        for ax, title, img in zip(axs, titles, images):
            ax.imshow(img)
            ax.set_title(title, fontsize=14, fontweight='bold')
            ax.axis('off')

        plt.tight_layout()
        plt.savefig(f"comparison_{name}.jpg", dpi=300, bbox_inches='tight')
        plt.show()

    except Exception as e:
        print(f"Skipping {name}, error: {e}")
