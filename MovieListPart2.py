#Sean Holbrook
#CIS261
#MovieGuidePart2

filename = "movies.txt"


print("The Movie List Program")

#create a command list menu function and call it

def menu():
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")

menu()

#need a function to write movies to the list
def write_movies(movie_list):
    with open(filename, "w") as f:
        for movie in movie_list:
            f.write(f"{movie}\n")



#create a function for list that holds movie titles, minimum of three titles

#this function becomes read_movies() so you can read off the text file
def my_movie_list():
    movie_list = []
    with open(filename) as f:
        for line in f:
            line = line.replace("\n", "")
            movie_list.append(line)
    return movie_list

movie_list = my_movie_list()

#create a function to display the list

def display_list(movie_list):
    num = 1
    for item in movie_list:
        print(f"{num}. {item}")
        num += 1


#create a function to add a title to the list

def add_movie(movie_list):
    movie_to_add = input("Name: ")
    movie_list.append(movie_to_add)
    write_movies(movie_list)
    print(f"{movie_to_add} was added")
    return movie_list


#create a function to delete a title from the list

def delete_movie(movie_list):
    movie_to_delete = int(input("Number: "))
    if movie_to_delete > len(movie_list):
        print("Invalid Movie Number")
    else:
        movie_to_delete -= 1
        removed_movie = movie_list.pop(movie_to_delete)
        write_movies(movie_list)
        print(f"{removed_movie} was deleted")


#Create choice menu

command = str(input("Command: "))


while command.lower() != "exit":
        if command.lower() == "list":
            display_list(movie_list)
            command = str(input("Command: "))
        elif command.lower() == "add":
            add_movie(movie_list)
            command = str(input("Command: "))
        elif command.lower() == "del":
            delete_movie(movie_list)
            command = str(input("Command: "))
        elif command == "exit":
            break
        else:
            print("Try another command please")
            command = str(input("Command: "))

print("Bye!")

