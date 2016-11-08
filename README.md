# Rypple

## Microblog

### Introduction

Rypple is a microblog web platform wherein users can share textual content with a cap of 256 characters for every message they post.
This cap was introduced because of the fundamental idea that limits kindle art.
The platform is intended to share quickly the user's thoughts and connect with others.

Users must create an account before entering the website, wherein they will have an associated homepage and profile page.
They can edit their profile as they wish, and publish posts. Each post also has an associated privacy attribute.
The user can choose to keep a post public or private.

Users can follow other users. When they do this, they are presented the latest posts of people they follow.
They can share or save these for later viewing.

### Dependencies

Rypple was built using the Django framework, and MySQL database. The following additional dependencies are also required:
- Django Rest Framework
- Pillow
- MySQL-python

All of them can be installed by:
```
sudo pip install djangorestframework pillow mysql-python
```
