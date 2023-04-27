import os
import time
import pwinput
from prettytable import PrettyTable
import math
import mysql.connector

os.system("cls")

def database() :
    db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="kontak"
    )
    return db

#fungsi registrasi user
import re

def register():
    db = database()
    #membuat objek cursor untuk melakukan operasi database
    cursor = db.cursor()
    #mengambil input user
    username = str(input("Masukkan email : "))
    password = str(input("Masukkan password : "))
    no_hp = str(input("Masukan nomor telepon : "))

    if username == ""  or password == "" or no_hp =="":
        print("Input tidak boleh kosong")
        time.sleep(3)
    elif not re.match("^[0-9]*$", no_hp):
        # jika nomor telepon mengandung karakter selain angka
        print("Nomor telepon harus terdiri dari angka saja.")
        register()
        time.sleep(2)
    else :
        #mengecek apakah username sudah terdaftar di dalam tabel user di database
        cursor.execute("SELECT * FROM user WHERE email=%s", (username,))
        result = cursor.fetchone()

        if result: #jika username telah terdaftar
            print("email sudah terdaftar.")
            time.sleep(3)

        else: #jika username belum terdaftar

            # menambahkan user baru ke database
            sql = "INSERT INTO user (email, password, no_telepon) VALUES (%s, %s, %s)"
            val = (username, password, no_hp)
            cursor.execute(sql, val) # eksekusi query
            db.commit() #menyimpan perubahan pada database setelah query dijalankan

            print("Registrasi berhasil.")

#fungsi login user
def login():
    global username

    username = input("Masukkan email : ")
    password = pwinput.pwinput(prompt="Masukkan password : ")

    db = database()
    cursor = db.cursor()
    sql = "SELECT * FROM user WHERE email = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, val)
    
    user = cursor.fetchone() #mengambil satu baris data dari hasil query yang telah dieksekusi 
  
    if user: #jika user ditemukan
        print("Login berhasil!")
        
    else: #jika user tidak ditemukan
        print("Username atau password salah.")
        login()
        time.sleep(2)

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
    
    def add_database(self):
    #menambahkan data ke dalam database
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

            db = database()
            cursor = db.cursor()

            # Cek apakah nama kontak sudah ada di database
            sql = "SELECT * FROM nomor_telepon WHERE nama = %s"
            val = (nama,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result:
                print("ERROR: Nama kontak sudah terdaftar. Silakan coba lagi.")
                continue

            # Cek apakah nomor telepon sudah ada di database
            sql = "SELECT * FROM nomor_telepon WHERE nomor = %s"
            val = (no_hp,)
            cursor.execute(sql, val)
            result = cursor.fetchone()
            if result:
                print("ERROR: Nomor telepon sudah terdaftar. Silakan coba lagi.")
                continue

            # Jika nama dan nomor telepon belum terdaftar, tambahkan ke database
            sql = "INSERT INTO nomor_telepon (nama, nomor, email) VALUES (%s, %s, %s)"
            val = (nama, no_hp, username)
            cursor.execute(sql, val)
            db.commit()

            self.history.append(("Kontak Ditambahkan", nama, no_hp))
            print("")
            print("=== KONTAK BERHASIL DITAMBAHKAN ===")
            print("Mohon Tunggu...")
            time.sleep(1)
            os.system("cls")
            break


    def get_data(self):
        #mengambil data dari database
        db = database()
        cursor = db.cursor()
        sql = "SELECT * FROM nomor_telepon WHERE email = %s"
        val = (username,)
        cursor.execute(sql, val)
        data = cursor.fetchall()
        return data

    def refreshList(self):
        #mereset semua data di node
        self.reset_data()
        #untuk mengambil data dari database
        result = self.get_data()
        for i in result:
            # Memasukan data kedalam node
            self.add_contacts(i[0], i[1])

    def reset_data(self):
        # Mengembalikan self.head menjadi None
        self.head = None

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

    def add_contacts(self, nama, no_hp):
        no_baru = Contacts(nama, no_hp)
        if self.head is None:
            self.head = no_baru
            self.tail = no_baru
        else:
            no_baru.previous = self.tail
            self.tail.next = no_baru
            self.tail = no_baru

    def find_contact_by_no_hp(self, no_hp):
        current = self.head
        while current:
            if current.no_hp == no_hp:
                return current
            current = current.next
        return None


# MENGUPDATE KONTAK
    def update_contact(self):
        nama = input("MASUKKAN NAMA KONTAK YANG INGIN DIUPDATE: ")
        new_no_hp = input("MASUKKAN NOMOR TELEPON BARU: ")
        db = database()
        cursor = db.cursor()
        sql = "UPDATE nomor_telepon SET nomor = %s WHERE nama = %s"
        val = (new_no_hp,nama)
        cursor.execute(sql, val)
        db.commit()
        print("Kontak berhasil diupdate.")
        self.refreshList()
   
# MENGHAPUS KONTAK
    def delete_contacts(self):
        nama = input("\nMASUKKAN NAMA KONTAK YANG INGIN DIHAPUS: ")
        #menghapus data di database
        db = database()
        cursor = db.cursor()
        sql = "DELETE FROM nomor_telepon WHERE nama = %s"
        val = (nama,)
        cursor.execute(sql, val)
        db.commit()
        print("Kontak berhasil dihapus.")
        self.refreshList()       

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
                    contacts_list.add_database()
                elif choice == '2':
                    contacts_list.delete_contacts()
                elif choice == '3':
                    contacts_list.refreshList()
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
