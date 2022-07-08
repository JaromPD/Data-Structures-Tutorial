import LinkedList as LL

def display_songs(songs):
    song_count = 0
    for song in songs:
        song_count += 1
        print(str(song_count) + ". " + song)

def main():
    print("Welcome to Music Ranker!")
    songs = LL.LinkedList()
    menu = True
    while menu == True:
        print("""
    What would you like to do?
        1. Add a song
        2. Remove a song
        3. View the list of songs
        """)
        user_choice = input("> ")

        if user_choice == "1":
            print("What song would you like to add?")
            new_song = input("> ")
            if songs.head is None:
                songs.insert_head(new_song)
                print("Added " + new_song + " to the list!")
            else:
                placement_menu = True
                while placement_menu == True:
                    print("""
    Where would you like to add this song?
        1. At the beginning
        2. At the end
        3. After a song
        4. Display the list of songs
                    """)
                    placement_choice = input("> ")
                    if placement_choice == "1":
                        songs.insert_head(new_song)
                        print("Added " + new_song + " to the list!")
                        placement_menu = False

                    elif placement_choice == "2":
                        songs.insert_tail(new_song)
                        print("Added " + new_song + " to the list!")
                        placement_menu = False

                    elif placement_choice == "3":
                        print("What song would you like to add this song after?")
                        after_song = input("> ")
                        if after_song in songs:
                            songs.insert_after(after_song, new_song)
                            print("Added " + new_song + " to the list!")
                            placement_menu = False
                        else:
                            print("That song is not in the list.")
                        placement_menu = False

                    elif placement_choice == "4":
                        print("Here is the list of songs:")
                        display_songs(songs)

                    else:
                        print(f"({placement_choice}) is not a valid option.")
                        placement_menu = True

        elif user_choice == "2":
            print("What song would you like to remove?")
            remove_song = input("> ")
            if remove_song in songs:
                songs.remove(remove_song)
                print("Removed " + remove_song + " from the list!")
            else:
                print("That song is not in the list.")

        elif user_choice == "3":
            print("Here is the list of songs:")
            display_songs(songs)

if __name__ == "__main__":
    main()