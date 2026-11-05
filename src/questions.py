# QuizMaster - Question Database
# Bu dosya quiz uygulamasında kullanılacak soruları saklar.

# questions adında bir liste oluşturuyoruz.
# Liste içerisinde birden fazla soru tutabiliriz.
questions = [

    # Birinci soru
    {
        # Soru metni
        "question": "What does CPU stand for?",

        # Kullanıcıya gösterilecek dört cevap seçeneği
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing User"
        ],

        # Bu sorunun doğru cevabı
        "answer": "A"
    },

    # İkinci soru
    {
        "question": "What does RAM stand for?",

        "options": [
            "A. Read Access Memory",
            "B. Random Access Memory",
            "C. Run Active Memory",
            "D. Remote Access Machine"
        ],

        "answer": "B"
    },

    # Üçüncü soru
    {
        "question": "Which language is used for web development?",

        "options": [
            "A. HTML",
            "B. CSS",
            "C. JavaScript",
            "D. All of the above"
        ],

        "answer": "D"
    }

]

# Toplam soru sayısını hesaplamak için len() kullanabiliriz.
# Örneğin len(questions) sonucu şu anda 3 olacaktır.
