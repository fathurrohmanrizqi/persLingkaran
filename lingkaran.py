import matplotlib.pyplot as plt
import numpy as np

# Fungsi untuk menggambar lingkaran
def draw_circle(a, b, r):
    """Menggambar lingkaran dengan pusat (a, b) dan jari-jari r, serta menunjukkan radiusnya.

    Args:
        a: Absis pusat lingkaran.
        b: Ordinat pusat lingkaran.
        r: Jari-jari lingkaran.
    """

    # Membuat data untuk lingkaran
    theta = np.linspace(0, 2*np.pi, 100)
    x = a + r * np.cos(theta)
    y = b + r * np.sin(theta)

    # Membuat plot lingkaran
    plt.plot(x, y, label=f"Circle with radius {r}")
    plt.grid(True)
    plt.axis('equal')

    # Menambahkan garis radius dari pusat ke tepi lingkaran
    x_radius = [a, a + r]
    y_radius = [b, b]
    plt.plot(x_radius, y_radius, 'r--')  # Garis radius berwarna merah putus-putus

    # Menambahkan teks untuk jari-jari
    plt.annotate(f"r = {r}", xy=(a + r / 2, b), xytext=(a + r / 2, b + 0.1),
                 ha='center', color='red')

    plt.legend()
    plt.show()

# Meminta input pengguna (opsional)
# a = float(input("Masukkan nilai a (absis pusat): "))
# b = float(input("Masukkan nilai b (ordinat pusat): "))
# r = float(input("Masukkan nilai r (jari-jari): "))

# Menggambar lingkaran
draw_circle(7, 12, 8)