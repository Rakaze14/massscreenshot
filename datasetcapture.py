import cv2
import os
import time

# Buat folder images kalau belum ada
os.makedirs("images", exist_ok=True)

# Buka kamera (ganti 0 kalau perlu, misal ke 1 atau 2 kalau nggak kebaca)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Kamera tidak terdeteksi.")
    exit()

# Jumlah gambar yang mau di-capture
total_images = 200
saved_count = 0

print("Mulai capture 400 gambar... Tekan 'q' untuk keluar lebih awal.")

while saved_count < total_images:
    ret, frame = cap.read()
    if not ret:
        print("Gagal ambil gambar.")
        break

    # Tampilkan preview frame
    cv2.imshow("RealSense Webcam Capture", frame)

    # Simpan gambar ke folder images/
    filename = f"images/image_{saved_count+1:04d}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Tersimpan: {filename}")

    saved_count += 1

    # Delay sedikit biar capture nggak terlalu ngebut
    time.sleep(0.1)

    # Tekan 'q' buat keluar manual
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release kamera & tutup window
print(f"\nTotal gambar tersimpan: {saved_count}")
cap.release()
cv2.destroyAllWindows()