# QuizMaster - Main File
# Bu dosya uygulamanın başlangıç noktasıdır.

# Quiz fonksiyonunu içe aktarıyoruz.
from quiz import start_quiz

# Mevcut kategorileri içe aktarıyoruz.
from categories import categories


# Uygulamanın karşılama ekranı.
print("==============================")
print("       WELCOME TO QUIZMASTER")
print("==============================")


# Kullanıcıdan geçerli bir isim alınana kadar devam ediyoruz.
while True:

    # Kullanıcıdan isim istiyoruz.
    name = input("Enter your name: ").strip()

    # İsim boş değilse döngüden çıkıyoruz.
    if name:
        break

    # İsim boşsa kullanıcıyı uyarıyoruz.
    print("Name cannot be empty! Please try again.")
    

# Kullanıcıyı karşılıyoruz.
print(f"\nHello, {name}!")

# Mevcut kategorileri ekrana yazdırıyoruz.
print("\nChoose a quiz category:")

# Kategorileri numaralandırarak gösteriyoruz.
category_list = list(categories.keys())

for number, category in enumerate(category_list, start=1):
    print(f"{number}. {category}")

# Kullanıcıdan kategori numarasını alıyoruz.
while True:

    choice = input("\nEnter category number: ")

    # Girilen değerin sayı olup olmadığını kontrol ediyoruz.
    if choice.isdigit():

        # Sayıyı tam sayıya dönüştürüyoruz.
        choice = int(choice)

        # Seçimin geçerli aralıkta olup olmadığını kontrol ediyoruz.
        if 1 <= choice <= len(category_list):
            break

    print("Invalid choice! Please select a valid category.")

# Seçilen kategori adını buluyoruz.
selected_category = category_list[choice - 1]

# Seçilen kategoride quiz'i başlatıyoruz.
start_quiz(name, selected_category)