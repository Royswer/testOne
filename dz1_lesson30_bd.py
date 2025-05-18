import sqlite3
import requests
#123
#Домашнее задание
connect = sqlite3.connect('jsonplaceholder.db')
cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    username TEXT,
    phone TEXT
)
''')
#
cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY,
    userId INTEGER,
    title TEXT,
    body TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS comments (
    postId INTEGER,
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    body TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS albums (
    id INTEGER PRIMARY KEY,
    userId INTEGER,
    title TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS photos (
    albumId INTEGER,
    id INTEGER PRIMARY KEY,
    title TEXT,
    url TEXT,
    thumbnailUrl TEXT
)
''')


def fetch_and_store():
    
    # Пользователи:
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users_response.json()
    
    for user in users:
        cursor.execute('INSERT OR REPLACE INTO users (id, name, username, phone) VALUES (?, ?, ?, ?)',
                       (user['id'], user['name'], user['username'], user['phone']))
    
    # Посты:
    posts_response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = posts_response.json()
    
    for post in posts:
        cursor.execute('INSERT OR REPLACE INTO posts (id, userId, title, body) VALUES (?, ?, ?, ?)',
                       (post['id'], post['userId'], post['title'], post['body']))
    
    # Комментарии:
    comments_response = requests.get('https://jsonplaceholder.typicode.com/comments')
    comments = comments_response.json()
    
    for comment in comments:
        cursor.execute('INSERT OR REPLACE INTO comments (postId, id, name, email, body) VALUES (?, ?, ?, ?, ?)',
                       (comment['postId'], comment['id'], comment['name'], comment['email'], comment['body']))
    
    # Альбомы:
    albums_response = requests.get('https://jsonplaceholder.typicode.com/albums')
    albums = albums_response.json()
    
    for album in albums:
        cursor.execute('INSERT OR REPLACE INTO albums (id, userId, title) VALUES (?, ?, ?)',
                       (album['id'], album['userId'], album['title']))
    
    # Фото:
    photos_response = requests.get('https://jsonplaceholder.typicode.com/photos')
    photos = photos_response.json()
    
    for photo in photos:
        cursor.execute('INSERT OR REPLACE INTO photos (albumId, id, title, url, thumbnailUrl) VALUES (?, ?, ?, ?, ?)',
                       (photo['albumId'], photo['id'], photo['title'], photo['url'], photo['thumbnailUrl']))
    
    connect.commit()

fetch_store = fetch_and_store()
connect.close()
