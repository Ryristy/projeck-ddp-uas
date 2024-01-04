import tkinter as tk
from tkinter import messagebox

class KasirApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Program Kasir")

        # menyimpan data barang
        self.barang_list = []
        
        # menyimpan total harga
        self.total_harga = tk.DoubleVar()
        
        # label dan entry untuk input nama barang
        tk.Label(root, text="Nama Barang:").grid(row=0, column=0)
        self.nama_barang_entry = tk.Entry(root)
        self.nama_barang_entry.grid(row=0, column=1)

        # label dan entry untuk input harga barang
        tk.Label(root, text="Harga Barang:").grid(row=1, column=0)
        self.harga_barang_entry = tk.Entry(root)
        self.harga_barang_entry.grid(row=1, column=1)

        # Tombol buat menambahkan barang
        tk.Button(root, text="Tambah Barang", command=self.tambah_barang).grid(row=2, column=0, columnspan=2, pady=10)

        # daftar barang yang sudah ditambahkan
        self.listbox = tk.Listbox(root, height=10, width=40)
        self.listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Tombol menghapus barang yang dipilih
        tk.Button(root, text="Hapus Barang", command=self.hapus_barang).grid(row=4, column=0, columnspan=2, pady=10)

        # label menampilkan total harga
        tk.Label(root, text="Total Harga:").grid(row=5, column=0)
        tk.Label(root, textvariable=self.total_harga).grid(row=5, column=1)

        # Tombol untuk menghitung total harga
        tk.Button(root, text="Hitung Total", command=self.hitung_total).grid(row=6, column=0, columnspan=2, pady=10)

        # Tombol mencetak struk
        tk.Button(root, text="Cetak Struk", command=self.cetak_struk).grid(row=7, column=0, columnspan=2, pady=10)

    def tambah_barang(self):
        # data dari input
        nama_barang = self.nama_barang_entry.get()
        harga_barang = self.harga_barang_entry.get()

        # Validasi input
        if not nama_barang or not harga_barang:
            messagebox.showwarning("Peringatan", "Mohon lengkapi data barang.")
            return

        # Menambahkan barang ke daftar
        self.barang_list.append((nama_barang, float(harga_barang)))
        self.listbox.insert(tk.END, f"{nama_barang} - Rp {harga_barang}")

        # Mengosongkan input setelah ditambahkan
        self.nama_barang_entry.delete(0, tk.END)
        self.harga_barang_entry.delete(0, tk.END)

    def hapus_barang(self):
        # Mendapatkan indeks barang yang dipilih
        selected_index = self.listbox.curselection()

        # Menghapus barang dari daftar dan listbox
        if selected_index:
            self.barang_list.pop(selected_index[0])
            self.listbox.delete(selected_index)

    def hitung_total(self):
        # Menghitung total harga dari daftar barang
        total = sum(harga for _, harga in self.barang_list)
        self.total_harga.set(total)

    def cetak_struk(self):
        # Menampilkan struk dengan informasi barang dan total harga
        struk = "===== Struk Pembelian =====\n"
        for nama, harga in self.barang_list:
            struk += f"{nama} - Rp {harga}\n"
        struk += f"\nTotal Harga: Rp {self.total_harga.get()}\n"
        struk += "===========================\n"

        messagebox.showinfo("Struk Pembelian", struk)

if __name__ == "__main__":
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()
