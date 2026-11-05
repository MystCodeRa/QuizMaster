
# QuizMaster - Quiz Logic
# Bu dosya quiz işlemlerini, puan kaydetmeyi ve leaderboard sistemini yönetir.

import json
import os

# Kategorileri categories.py dosyasından alıyoruz.
from categories import categories


# ==========================================
# SCORE SAVING
# ==========================================

# Kullanıcının puanını JSON dosyasına kaydediyoruz.
def save_score(score, name, category):

    # Skor dosyasının yolunu belirliyoruz.
    score_file = "data/scores.json"

    # data klasörü yoksa otomatik oluşturuyoruz.
    os.makedirs("data", exist_ok=True)

    # Skor dosyası yoksa boş listeyle oluşturuyoruz.
    if not os.path.exists(score_file):
        with open(score_file, "w") as file:
            json.dump([], file)

    # Mevcut skorları güvenli şekilde okuyoruz.
    try:
        with open(score_file, "r") as file:
            scores = json.load(file)

        # JSON içeriğinin liste olup olmadığını kontrol ediyoruz.
        if not isinstance(scores, list):
            scores = []

    # JSON bozuksa veya dosya okunamıyorsa boş liste kullanıyoruz.
    except (json.JSONDecodeError, OSError):
        scores = []

    # Yeni oyuncunun bilgilerini listeye ekliyoruz.
    scores.append({
        "name": name,
        "category": category,
        "score": score
    })

    # Güncellenmiş skorları dosyaya kaydediyoruz.
    with open(score_file, "w") as file:
        json.dump(scores, file, indent=4, ensure_ascii=False)


# ==========================================
# LEADERBOARD
# ==========================================


# Kullanıcının kişisel en yüksek puanını buluyoruz.
def show_personal_best(name, category):

    # Skor dosyasının yolunu belirliyoruz.
    score_file = "data/scores.json"

    # Skorları dosyadan okuyoruz.
    with open(score_file, "r") as file:
        scores = json.load(file)

    # Sadece bu kullanıcının seçilen kategorideki skorlarını alıyoruz.
    personal_scores = [
        player["score"]
        for player in scores
        if player.get("name") == name
        and player.get("category") == category
    ]

    # En yüksek puanı buluyoruz.
    if personal_scores:
        best_score = max(personal_scores)
        print("Personal best:", best_score, "points")



# Puan tablosunu seçilen kategoriye göre gösteriyoruz.
def show_leaderboard(category):

    # Skor dosyasının yolunu belirliyoruz.
    score_file = "data/scores.json"

    # Dosya mevcut değilse bilgi veriyoruz.
    if not os.path.exists(score_file):
        print("\nNo scores available yet.")
        return

    # Skorları güvenli şekilde okuyoruz.
    try:
        with open(score_file, "r") as file:
            scores = json.load(file)

        # Dosyanın liste içerip içermediğini kontrol ediyoruz.
        if not isinstance(scores, list):
            print("\nLeaderboard data is invalid.")
            return

    except (json.JSONDecodeError, OSError):
        print("\nCould not read leaderboard data.")
        return

    # Sadece seçilen kategoriye ait skorları alıyoruz.
    scores = [
        player for player in scores
        if isinstance(player, dict) and player.get("category") == category
    ]

    # Bu kategoride henüz skor yoksa bilgi veriyoruz.
    if not scores:
        print("\nNo scores available for this category yet.")
        return

    # Puanları büyükten küçüğe sıralıyoruz.
    scores = sorted(
        scores,
        key=lambda item: item.get("score", 0),
        reverse=True
    )

    print(f"\n===== {category.upper()} LEADERBOARD =====")

    # Oyuncuları sırasıyla gösteriyoruz.
    for rank, player in enumerate(scores, start=1):
        print(
            f"{rank}. {player.get('name', 'Unknown')} - "
            f"{player.get('score', 0)} points"
        )




# ==========================================
# QUIZ SYSTEM
# ==========================================

# Quiz fonksiyonunu oluşturuyoruz.
def start_quiz(name, selected_category):

    # Kullanıcı yeniden oynamak istediği sürece döngü devam eder.
    while True:

        # Seçilen kategorinin sorularını alıyoruz.
        questions = categories[selected_category]

        # Her yeni oyunda puanı sıfırlıyoruz.
        score = 0

        # Soruları sırayla gösteriyoruz.
        for question in questions:

            print("\n" + question["question"])

            # Cevap seçeneklerini gösteriyoruz.
            for option in question["options"]:
                print(option)

            # Geçerli cevap girilene kadar kullanıcıyı bekliyoruz.
            while True:
                user_answer = input("Your answer (A/B/C/D): ").strip().upper()

                if user_answer in ["A", "B", "C", "D"]:
                    break
                else:
                    print("Invalid answer! Please enter A, B, C or D.")

            # Kullanıcının cevabını kontrol ediyoruz.
            if user_answer == question["answer"]:
                print("Correct!")
                score += 10
            else:
                print("Wrong!")

        # Quiz sonuçlarını gösteriyoruz.
        print("\nQuiz Completed!")
        print("Category:", selected_category)
        print("Your score:", score)
        print("Maximum score:", len(questions) * 10)

        # Başarı yüzdesini hesaplıyoruz.
        success_rate = (score / (len(questions) * 10)) * 100
        print(f"Success rate: {success_rate:.1f}%")

        # Kullanıcının puanını kaydediyoruz.
        save_score(score, name, selected_category)

        # Kişisel rekorunu gösteriyoruz.
        show_personal_best(name, selected_category)

        # Kategori liderlik tablosunu gösteriyoruz.
        show_leaderboard(selected_category)

        # Kullanıcıya tekrar oynamak isteyip istemediğini soruyoruz.
        play_again = input("\nDo you want to play again? (Y/N): ").strip().upper()

        # Kullanıcı Y yazarsa döngü baştan başlar.
        if play_again == "Y":
            print("\nStarting a new quiz...")
        else:
            # Diğer girişlerde quiz sona erer.
            print("\nThank you for playing QuizMaster!")
            break