import os
import time
import pwinput
from prettytable import PrettyTable
import math
import json


os.system("cls")

table = PrettyTable()

# MENDEFINISIKAN KELAS PYTHON
class Contacts:
    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.next = None
        self.previous = None

# MENDEFINISIKAN KELAS KONTAKLIST  
class ContactList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.history = []

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

# DEFINISI MERGESORT

     def merge_sort(self, contacts, sort_by):
        if len(contacts) > 1:
            mid = len(contacts) // 2
            left_half = contacts[:mid]
            right_half = contacts[mid:]

            self.merge_sort(left_half, sort_by)
            self.merge_sort(right_half, sort_by)

            i = 0
            j = 0
            k = 0

            while i < len(left_half) and j < len(right_half):
                if sort_by == 'name':
                    if left_half[i]['name'] < right_half[j]['name']:
                        contacts[k] = left_half[i]
                        i += 1
                    else:
                        contacts[k] = right_half[j]
                        j += 1
                elif sort_by == 'phone':
                    if left_half[i]['phone'] < right_half[j]['phone']:
                        contacts[k] = left_half[i]
                        i += 1
                    else:
                        contacts[k] = right_half[j]
                        j += 1
                k += 1

            while i < len(left_half):
                contacts[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                contacts[k] = right_half[j]
                j += 1
                k += 1

        return contacts
    
# MENGURUTKAN KONTAK MENGGUNAKAN MERGESORT

     def sort_contacts(self):
        print("PILIH KATEGORI URUTAN UNTUK MELIHAT KONTAK : ")
        print("1. Nama")
        print("2. Nomor Telepon")
        sort_choice = input("Masukkan pilihan (1/2): ")

        if sort_choice == "1":
            sort_by = "name"
        elif sort_choice == "2":
            sort_by = "phone"
        else:
            print("Pilihan tidak valid!")
            return

        contacts = []
        current = self.head
        while current:
            contacts.append({'name': current.nama, 'phone': current.no_hp})
            current = current.next

        sorted_contacts = self.merge_sort(contacts, sort_by)

        table = PrettyTable(['No', 'Nama', 'No. HP'])
        for i, contact in enumerate(sorted_contacts):
            table.add_row([str(i+1), contact['name'], contact['phone']])

        print(table)
        back()

# MENAMBAHKAN KONTAK 

     def add_contacts(self):
        print("")
        os.system("cls")
        while True:
            nama = input("MASUKKAN NAMA KONTAK: ")
            if not nama:
                print("ERROR: Nama kontak tidak boleh kosong. Silakan coba lagi.")
                continue
            no_hp = input("MASUKKAN NOMOR TELEPON: ")
            if not no_hp:
                print("ERROR: Nomor telepon tidak boleh kosong. Silakan coba lagi.")
                continue
            elif not no_hp.isdigit():
                print("ERROR: Nomor telepon hanya boleh diisi dengan angka. Silakan coba lagi.")
                continue
            elif self.find_contact_by_no_hp(no_hp):
                print("ERROR: Nomor telepon sudah terdaftar. Silakan coba lagi.")
                continue
            no_baru = Contacts(nama, no_hp)
            if self.head is None:
                self.head = no_baru
                self.tail = no_baru
            else:
                no_baru.previous = self.tail
                self.tail.next = no_baru
                self.tail = no_baru
            self.history.append(("Kontak Ditambahkan", nama, no_hp))
            print("")
            print("=== KONTAK BERHASIL DITAMBAHKAN ===")
            print("Mohon Tunggu...")
            time.sleep(1)
            os.system("cls")
            break

    def find_contact_by_no_hp(self, no_hp):
        current = self.head
        while current:
            if current.no_hp == no_hp:
                return current
            current = current.next
        return None


# MENGUPDATE KONTAK

    def update_contact(self):
        print("")
        os.system("cls")
        nama = input("MASUKKAN NAMA KONTAK YANG INGIN DIUPDATE: ")
        current = self.head
        while current:
            if current.nama.lower() == nama.lower():
                print("KONTAK YANG AKAN DIUPDATE: ")
                print(f"NAMA: {current.nama}")
                print(f"NO HP: {current.no_hp}")
                new_nama = input("MASUKKAN NAMA BARU (ATAU TEKAN ENTER JIKA TIDAK INGIN DIUBAH): ")
                new_no_hp = input("MASUKKAN NOMOR TELEPON BARU (ATAU TEKAN ENTER JIKA TIDAK INGIN DIUBAH): ")
                if new_nama == "" and new_no_hp == "":
                    print("=== TIDAK ADA DATA YANG DIUBAH ===")
                    time.sleep(3)
                    os.system("cls")
                    return
                if new_nama.strip() != "":
                    current.nama = new_nama.strip()
                if new_no_hp.isdigit():
                    current.no_hp = new_no_hp
                else:
                    print("=== NOMOR TELEPON TIDAK VALID ===")
                    time.sleep(1)
                    os.system("cls")
                    return
                self.history.append(("Kontak Diupdate", current.nama, current.no_hp))
                print("")
                print("=== KONTAK BERHASIL DIUPDATE ===")
                print("Mohon Tunggu...")
                time.sleep(3)
                os.system("cls")
                return
            current = current.next
        print("")
        print("=== MAAF, KONTAK TIDAK DITEMUKAN ===")
        time.sleep(1)
        os.system("cls")
        back()

# MENGHAPUS KONTAK
    def delete_contacts(self):
        print("")
        os.system("cls")
        nama = input("\nMASUKKAN NAMA KONTAK YANG INGIN DIHAPUS: ")
        current = self.head
        while current:
            if current.nama.lower() == nama.lower():
                if current == self.head and current == self.tail:
                    self.head = None
                    self.tail = None
                elif current == self.head:
                    self.head = current.next
                    current.next.previous = None
                elif current == self.tail:
                    self.tail = current.previous
                    current.previous.next = None
                else:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                self.history.append(("Kontak Dihapus", current.nama, current.no_hp))
                print("")
                print("=== KONTAK BERHASIL DIHAPUS ===")
                print("Mohon Tunggu...")
                time.sleep(2)
                os.system("cls")
                return
            current = current.next
        print("")
        print("=== MAAF, KONTAK TIDAK DITEMUKAN ===")
        time.sleep(3)
        os.system("cls")

# MENDIFINISIKAN JUMP SEARCH
    def jump_search(self, nama, jump):
        current = self.head
        count = 0
        while current:
            if current.nama.lower().find(nama.lower()) != -1:
                return current
            count += 1
            if count % jump == 0:
                if current.nama.lower() >= nama.lower():
                    break
            current = current.next
        return None

# MENCARI KONTAK MENGGUNAKAN JUMP SEARCH 
   def search_contact(self):
        print("")
        os.system("cls")
        while True:
            nama = input("MASUKKAN NAMA KONTAK YANG INGIN DICARI: ")
            if not nama:
                print("ERROR: Nama kontak tidak boleh kosong. Silakan coba lagi.")
                continue
            else:
                break
        jump = int(math.sqrt(len(self)))
        result = self.jump_search(nama, jump)
        if not result:
            print("")
            print("MAAF, TIDAK DITEMUKAN KONTAK DENGAN NAMA TERSEBUT")
        else:
            result_list = []
            while result:
                if result.nama.lower().find(nama.lower()) != -1:
                    result_list.append(result)
                result = result.next
            os.system("cls")
            print(">>>> HASIL PENCARIAN KONTAK <<<<")
            print("")
            table = PrettyTable(['Nama', 'No. HP'])
            for contact in result_list:
                table.add_row([contact.nama, contact.no_hp])
            print(table)
            time.sleep(3)
            os.system("cls")
            back()

# MENAMPILKAN RIWAYAT        
    def display_history(self):
        os.system("cls")
        print("============== RIWAYAT ANDA ===============".center(70))
        print("===========================================".center(70))
        print("")
        if len(self.history) == 0:
            print("MAAF, TIDAK ADA RIWAYAT ANDA".center(70))
        else:
            for action in self.history:
                print(action[0], "--->", action[1], "-", action[2])
                back()

# Fungsi untuk melakukan registrasi
def register():
    with open("users.json", "r") as f:
        users = json.load(f)
    email = input("Masukkan email: ")
    
# Mencari apakah email sudah terdaftar sebelumnya
    for user in users:
        if email == user["email"]:
            print("Email sudah terdaftar. Silakan login atau gunakan email lain.\n")
            return
    password = pwinput.pwinput("Masukkan password: ")
    phone = input("Masukkan nomor telepon: ")
    user = {"email": email, "password": password, "phone": phone}
    users.append(user)
    with open("users.json", "w") as f:
        json.dump(users, f)
    print("Registrasi berhasil.\n")
    time.sleep(2)
    os.system("cls")

# Fungsi untuk melakukan login
def login():
    while True:
        with open("users.json", "r") as f:
            users = json.load(f)
        email = input("Masukkan email: ")
        password = pwinput.pwinput("Masukkan password: ")
        for user in users:
            if email == user["email"] and password == user["password"]:
                print("Login berhasil.\n")
                time.sleep(2)
                os.system("cls")
                return
        print("Email atau password salah.\n")

# Program utama
def utama():
    try:
        while True:
            print(f"Silakan pilih menu yang diinginkan:\n"
            '''
            ||===================================||
            ||               Menu :              ||
            ||===================================||
            ||      1. Login                     ||
            ||      2. Register                  ||
            ||      3. Exit                      ||
            ||===================================||\n''')

            choice = int(input("Pilih menu: "))
            if choice == 1:
                login()
                main()
            elif choice == 2:
                register()
            elif choice == 3:
                exit()
            else:
                print("Menu tidak tersedia.\n")
     except:
        print("masukkan menu yang benar: ")
        utama()

# MENU PROGRAM                
def main():
    if __name__ == '__main__':
        print("")
        contacts_list = ContactList()
        try:
            while True:
                print("============================================================".center(70))
                print("======== SILAHKAN PILIH MENU YANG INGIN ANDA AKSES =========".center(70))
                print("============================================================".center(70))
                print("""
                +====================================================+
                |           ==== MENU YANG TERSEDIA ====             |
                +====================================================+
                |                (1) TAMBAH KONTAK                   |
                |                (2) HAPUS KONTAK                    |
                |                (3) LIHAT KONTAK                    |
                |                (4) CARI KONTAK                     |
                |                (5) LIHAT HISTORY                   |
                |                (6) UPDATE KONTAK                   |
                |                (7) KELUAR                          |
                +====================================================+
                """)
                print("")

                choice = input("SILAHKAN PILIH MENU YANG ANDA INGINKAN (1-6): ")

                if choice == '1':
                    contacts_list.add_contacts()
                elif choice == '2':
                    contacts_list.delete_contacts()
                elif choice == '3':
                    print("=======  DAFTAR KONTAK ANDA  =======")
                    contacts_list.sort_contacts()
                    print("====================================")
                elif choice == '4':
                    contacts_list.search_contact()
                elif choice == '5':
                    contacts_list.display_history()
                elif choice == '6':
                    contacts_list.update_contact()
                elif choice == '7':
                    exit()
                else:
                    print("=== MAAF TIDAK ADA PILIHAN, SILAHKAN PILIH ULANG (1-6) ===")
        except:
            print("masukkan menu dengan valid: ")
            main()

def exit():
    time.sleep(2)
    os.system("cls")
    print ("=== TERIMA KASIH ===")
    raise SystemExit
    
def back():
    print ('''
0. back
1. Exit''')

    pilih = input("SILAHKAN PILIH OPSI : ")
    if pilih == '1':
        print("Tunggu...")
        time.sleep(2)
        os.system("cls")
        main()
    elif pilih == '2':
        exit()

utama()
