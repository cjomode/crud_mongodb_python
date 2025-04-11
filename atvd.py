import pymongo
from pymongo import MongoClient

client = MongoClient()
client = pymongo.MongoClient('mongo connection here')
db = client['senac3']
articles = db.articles

def menu():
    while True:
        print("1. Adicionar Artigo")
        print("2. Listar Todos os Artigos")
        print("3. Buscar Artigo por Autor")
        print("4. Atualizar Autor")
        print("5. Deletar Artigos por Autor")
        print("6. Sair")
        option = input("Escolha uma opção: ")

        match option:
            case "1":
                article = {
                    'author': 'Derrick Mwiti',
                    'about': 'Introduction to MongoDB and Python',
                    'tags': ['mongodb', 'python', 'pymongo']
                }
                article1 = {"author": "Emmanuel Kens",
                "about": "Knn and Python",
                "tags":["Knn","pymongo"]
                }
                article2 = {"author": "Daniel Kimeli",
                "about": "Web Development and Python",
                "tags": ["web", "design", "HTML"]
                }

                new_articles = articles.insert_many([article1, article2])

                print("The new article IDs are {}".format(new_articles.inserted_ids))

            case "2":
                for article in articles.find():
                    print(article)
            case "3":
                for article in articles.find({}, {'_id': 0, 'author': 1, 'about': 1}):
                    print(article)
            case "4":
                query = {'author': 'Derrick Mwiti'}
                new_author = {'$set': {'author': 'John David'}}
                articles.update_one(query, new_author)
                print("Autor atualizado!")
            case "5":
                delete_articles = articles.delete_many({'author': 'Daniel Kimeli'})
                print(delete_articles.deleted_count, 'artigos deletados')
            case "6":
                print("Saindo...")
                break
            case _:
                print("Opção inválida.")

menu()

