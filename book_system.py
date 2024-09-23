from abc import ABC, abstractmethod

# Abstract class untuk Buku
class Book(ABC):
    def __init__(self, judul, penulis, tahunterbit):
        self.judul = judul
        self.penulis = penulis
        self.tahunterbit = tahunterbit

    @abstractmethod
    def get_info(self):
        pass

# Concrete class untuk Buku Fiksi
class FictionBook(Book):
    def get_info(self):
        return f"[Buku Fiksi] Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahunterbit}"

# Concrete class untuk Buku Non-Fiksi
class NonFictionBook(Book):
    def get_info(self):
        return f"[Buku Non-Fiksi] Judul: {self.judul}, Penulis: {self.penulis}, Tahun Terbit: {self.tahunterbit}"

# Factory Method Class
class BookFactory(ABC):
    @abstractmethod
    def create_book(self, judul, penulis, tahunterbit):
        pass
    def update_book(self, book, judul=None, penulis=None, tahunterbit=None):
        pass

# Concrete Factory untuk Buku Fiksi
class FictionBookFactory(BookFactory):
    def create_book(self, judul, penulis, tahunterbit):
        return FictionBook(judul, penulis, tahunterbit)

    def update_book(self, book, judul=None, penulis=None, tahunterbit=None):  # Tambahkan self
        if judul:
            book.judul = judul
        if penulis:
            book.penulis = penulis
        if tahunterbit:
            book.tahunterbit = tahunterbit
        return book

# Concrete Factory untuk Buku Non-Fiksi
class NonFictionBookFactory(BookFactory):
    def create_book(self, judul, penulis, tahunterbit):
        return NonFictionBook(judul, penulis, tahunterbit)

    def update_book(self, book, judul=None, penulis=None, tahunterbit=None):  # Tambahkan self
        if judul:
            book.judul = judul
        if penulis:
            book.penulis = penulis
        if tahunterbit:
            book.tahunterbit = tahunterbit
        return book

# Fungsi untuk menampilkan daftar buku
def display_books(books):
    if not books:
        print("Tidak ada buku yang terdaftar")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book.get_info()}")

# Fungsi untuk menambahkan buku melalui terminal
def created_book(fiction_factory, nonfiction_factory):
    judul = input("Masukkan judul buku: ")
    penulis = input("Masukkan nama penulis: ")
    tahunterbit = input("Masukkan tahun terbit: ")
    
    # Pilih jenis buku (Fiksi atau Non-Fiksi)
    while True:
        jenis = input("Masukkan jenis buku (fiksi/non-fiksi): ").lower()
        if jenis == "fiksi":
            return fiction_factory.create_book(judul, penulis, tahunterbit)
        elif jenis == "non-fiksi":
            return nonfiction_factory.create_book(judul, penulis, tahunterbit)
        else:
            print("Pilihan tidak valid. Silakan pilih 'fiksi' atau 'non-fiksi'.")

# Fungsi untuk memperbarui buku dari terminal
def updated_book(fiction_factory, nonfiction_factory, books):
    if not books:
        print("Tidak ada buku yang terdaftar untuk diperbarui.")
        return

    display_books(books)  # Tampilkan daftar buku untuk dipilih
    while True:
        try:
            index = int(input("Pilih nomor buku yang ingin diperbarui (atau 0 untuk batal): ")) - 1
            if index == -1:
                return  # Batalkan pembaruan
            if 0 <= index < len(books):
                break
            else:
                print("Nomor buku tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

    judul = input("Masukkan judul baru (kosongkan jika tidak ingin mengubah): ")
    penulis = input("Masukkan nama penulis baru (kosongkan jika tidak ingin mengubah): ")
    tahunterbit = input("Masukkan tahun terbit baru (kosongkan jika tidak ingin mengubah): ")

    book = books[index]
    if isinstance(book, FictionBook):
        fiction_factory.update_book(book, judul or None, penulis or None, tahunterbit or None)
    elif isinstance(book, NonFictionBook):
        nonfiction_factory.update_book(book, judul or None, penulis or None, tahunterbit or None)
    
    print("Informasi buku berhasil diperbarui!")

if __name__ == "__main__":
    # Membuat factory untuk buku fiksi dan non-fiksi
    fiction_factory = FictionBookFactory()
    nonfiction_factory = NonFictionBookFactory()
    
    # Menyimpan daftar buku
    books = []
    
    # Membuat buku baru menggunakan input dari terminal
    while True:
        print("\nPilih opsi:")
        print("1. Tambah buku")
        print("2. Lihat daftar buku")
        print("3. Update buku")
        print("4. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            # Menambahkan buku baru dari terminal
            new_book = created_book(fiction_factory, nonfiction_factory)
            books.append(new_book)
            print("Buku berhasil ditambahkan!\n")
        
        elif pilihan == "2":
            # Menampilkan daftar buku
            print("\nDaftar Buku:")
            display_books(books)
        
        elif pilihan == "3":
            # Memperbarui buku
            updated_book(fiction_factory, nonfiction_factory, books)
        
        elif pilihan == "4":
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
