#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/CharlesPrado23/Notebooks/blob/main/Semana3_Exerc%C3%ADcios.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# ## Semana 3 
# ## Exercícios (FOR, IF, WHILE) 

# 1) Dado a lista, abaixo, de temperaturas da cidade de Boulder em Fahrenheit (F):
# 
#  1.1) Crie uma lista convertendo para Celsius (C). Para converter use a fórmula C = (F-32)*(5/9); Print os valores na tela. 
#  
#  1.2) Crie uma função que receba a lista de temperaturas em Fahrenheit e retorna uma lista em graus Celsius. Print a lista na tela. 
# 
#  1.3) **(Desafio)** Generalize a função criada em 1.2 usando *args para que a função receba uma lista de tamanho variável.
#  
# 
#  F = [47,49,57,64,72,83,89,87,79,67,55,47]; (Temperaturas em F da cidade de Boulder)

# In[2]:


F = [47,49,57,64,72,83,89,87,79,67,55,47]


# In[8]:


c = []
for f in F:
    celsius = ((f-32)*(5/9))
    c.append(celsius)
c


# 2)Passe por todos os números até 99 (começando em 1). Imprima 'fizz' para cada número que é divisível por 7, imprima 'buzz' para cada número divisível por 5 e imprima 'fizzbuzz' para cada número divisível por 7 e 5! Se o número não for divisível por 7 ou 5, imprima um travessão (‘-‘)! 
# 
#  Para descubrir se um número x é divisível por y use operador (%): 
# 
#     x % y retorna True se x é divísel por y, False se não for. 
# 
# Dica : use  FOR , IF, ELIF, ELSE 
#    

# In[19]:


for x in range(1,100):
    if x % 7 == 0:
        if x % 5 == 0:
            print(str(x) +': fizzbuzz')
        else:
            print(str(x) +': fizz')
    elif x % 5 == 0:
        print(str(x) +': buzz')
    else:
        print(str(x) + ': -')
        
        
        
        


# 3) Os filmes/séries podem ser classificados conforme o seu genero (ação,comédia, drama, terror etc). Considerando as classificações abaixo: 
# 
#    a) Ação = Jumanji, Projeto Gemini,The old guard,WandaVision.
# 
#    b) Comédia = Jumanji,How I Met Your Mother,Friends, Amigos para sempre.
# 
#    c)  Drama = Amigos para sempre, After,Game of Thrones, WandaVision.
# 
#  Tarefas: 
# 
#    3.1 - Cria uma lista de listas para representar cada um dos conjuntos acima. 
# 
#    3.2 - Usando a lista criada em 3.1, escreva um programa que "print" na tela a quantidade de caracteres de cada título.    

# In[24]:


# 3.1
genres = [['Jumanji', 'Projeto Gemini','The old guard','WandaVision'],
          ['Jumanji','How I Met Your Mother','Friends', 'Amigos para sempre'],
          ['Amigos para sempre', 'After','Game of Thrones', 'WandaVision'],
         ]
genres


# In[31]:


# 3.2
for lists in genres:
    for word in lists:
        count = len(list(word))
        print(f'{word} has {count} characters')
        
x


# In[ ]:


# Retirando os duplicados
nd = []
for lists in genres:
    for word in lists:
        if word not in nd:
            nd.append(word)
            count = len(list(word))
            print(f'{word} has {count} characters')
        
x


# 4) Escreva um programa que calcule o fatorial de um número (entre com o número usando input). Sabendo que: 
# 
#   a) n! = n*(n-1)*(n-2)*...*1 
# 
#   b) 1! = 1
# 
#   c) 0! = 1
#   
#   Dica: Use While  

# In[66]:


n = int(input('Digite um número inteiro: '))
result = n*(n-1)
n -= 1
while n > 2:
    n -= 1
    result = result*(n)
print(result)


# **5) Desafio**
# 
# Considerando o problema 3): 
# 
#  5.1) Crie um dicionário no qual cada chave representa o genero do filme; 
# 
#  5.2) Em um sistema de recomendação baseado em conteúdos, deseja-se saber as classificações (generos) de cada filme. Faça um programa que usando o dicionário criado em 5.1, retorne os generos associados a cada filme. (Dica: use um outro dicionário).
# 

# In[77]:


# 5.1
movies = [['Jumanji', 'Projeto Gemini','The old guard','WandaVision'],
          ['Jumanji','How I Met Your Mother','Friends', 'Amigos para sempre'],
          ['Amigos para sempre', 'After','Game of Thrones', 'WandaVision']
         ]
genres = ['Action', 'Comedy', 'Drama']

movies_genres = dict(zip(genres, movies))


# In[ ]:


# 5.2


# ## Exercícios de Class (Retirado do Livro - Python Crash Course)
#  
#  1)
# 
# (a) Make a class called User. 
# 
# (b) Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 
# 
# (c) Make a method called describe_user() that prints a summary of the user’s information. 
# 
# (d) Make another method called greet_user() that prints a personalized greeting to the user.

# In[98]:


# # 1.
# class User(object):
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def describe_user(self, user):
#         print(f'Name: {user.first_name}\nLast Name: {user.last_name}')
#     def greet_user(self, user):
#         print(f'Hello, {user.first_name} {user.last_name}')
# person = User('Lucas', 'Sousa')
# person.greet_user(person)


# 2)
# 
# (a) Add an attribute called login_attempts to your User class from Exercise. 
# 
# (b) Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
# 
# (c) Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
# 
# (d) Make an instance of the User class and call increment_login_attempts() several times. 
# 
# (e) Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
# 
# (f) Print login_attempts again to make sure it was reset to 0.

# In[1]:


# 2.
class User(object):
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self, user):
        print(f'Name: {user.first_name}\nLast Name: {user.last_name}')
    def greet_user(self, user):
        print(f'Hello, {user.first_name} {user.last_name}')
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
        
        
person = User('Lucas', 'Sousa')

person.increment_login_attempts()
person.increment_login_attempts()
person.increment_login_attempts()


# In[30]:


print(f'Before reset: {person.login_attempts}')
person.reset_login_attempts()
print(f'After reset: {person.login_attempts}')


# 3)
# 
# Admin: An administrator is a special kind of user. 
# (a) Write a class called Admin that inherits from the User class you wrote .
# 
# (b) Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on.
# 
# (C) Write a method called show_privileges() that lists the administrator’s set of privileges.
# 
# (d) Create an instance of Admin, and call your method.

# In[14]:


# 3.
class Admin(User):
    privileges = ['can add post', 'can delete post', 
                  'can ban user', 'can block comments']
    def show_privileges(self):
        for priv in self.privileges:
            print(f'- {priv}')
admin = Admin('Lucas', 'Sousa')
admin.show_privileges()


# 4)
# 
# (a) Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in previous Exercise.
# 
# (b) Move the show_privileges() method to this class.

# In[35]:


# 4.
class Privileges(object):
    def __init__(self, privileges = ['can add post', 'can delete post', 'can ban user', 'can block comments']):
        self.privileges = ['can add post', 'can delete post', 
                           'can ban user', 'can block comments']
    def show_privileges(self):
        for priv in self.privileges:
            print(f'- {priv}')
a = Privileges()
a.show_privileges()


# 
# 5)
# 
# (a) Make a Privileges instance as an attribute in the Admin class.
# 
# (b) Create a new instance of Admin and use your method to show its privileges.

# In[ ]:




