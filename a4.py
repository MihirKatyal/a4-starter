from fileinput import filename
from pathlib import Path
import json
from Profile import Profile, Post, DsuFileError, DsuProfileError
import ui

class Profile:
    def __init__(self, username, password, bio):
        self.username = username
        self.password = password
        self.bio = bio

    def save(self, filename):
        data = {
            'username': self.username,
            'password': self.password,
            'bio': self.bio
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

def create_profile(directory, name):
    print("Creating a new profile...")
    username = input("Username: ")
    password = input("Password: ")
    bio = input("Bio: ")

    profile = Profile(username, password, bio)
    filename = Path(directory) / f"{name}.dsu"
    try:
        profile.save(filename)
        print(f"Profile saved to {filename}")
    except DsuFileError as e:
        print(f"Failed to save profile: {e}")

def load_profile(filename):
    try:
        profile = Profile()
        profile.load(filename)
        print(f"Loaded profile from {filename}")
        return profile
    except (DsuFileError, DsuProfileError) as e:
        print(f"Failed to load profile: {e}")
        return None
    
def edit_profile(profile, args):
    for i in range(1, len(args), 2):
        if args[i] == '-usr':
            profile.username = args[i + 1]
        elif args[i] == '-pwd':
            profile.password = args[i + 1]
        elif args[i] == '-bio':
            profile.bio = args[i + 1]
        elif args[i] == '-addpost':
            profile.add_post(Post(args[i + 1]))
        elif args[i] == '-delpost':
            if profile.del_post(int(args[i + 1])):
                print("Post deleted.")
            else:
                print("Failed to delete post.")
    try:
        profile.save(filename)  # Assumed filename is stored 
        print("Profile updated.")
    except DsuFileError as e:
        print(f"Failed to update profile: {e}")

def print_profile(profile, args):
    if '-all' in args:
        print(f"Username: {profile.username}, Password: {profile.password}, Bio: {profile.bio}")
        for index, post in enumerate(profile.get_posts()):
            print(f"Post {index + 1}: {post.entry}, Timestamp: {post.timestamp}")
    if '-usr' in args:
        print(f"Username: {profile.username}")
    if '-pwd' in args:
        print(f"Password: {profile.password}")
    if '-bio' in args:
        print(f"Bio: {profile.bio}")
    if '-posts' in args:
        for index, post in enumerate(profile.get_posts()):
            print(f"Post {index + 1}: {post.entry}, Timestamp: {post.timestamp}")
    if '-post' in args:
        post_index = args.index('-post') + 1
        if post_index < len(args):
            try:
                post_id = int(args[post_index]) - 1  # Assumed that post IDs start at 1 
                posts = profile.get_posts()
                if 0 <= post_id < len(posts):
                    post = posts[post_id]
                    print(f"Post {post_id + 1}: {post.entry}, Timestamp: {post.timestamp}")
                else:
                    print("Post ID is out of range.")
            except ValueError:
                print("Invalid post ID.")
        else:
            print("Post ID not specified.")

def list_directory(path, options):
    files = []
    for file_path in Path(path).rglob("*"):
        if file_path.is_file():
            files.append(file_path)

    if '-f' in options:
        files = [file for file in files if file.is_file()]
    elif '-r' not in options:
        files = [file for file in files if file.parent == Path(path)]

    if '-s' in options:
        files = [file for file in files if options['-s'] in file.name]

    if '-e' in options:
        files = [file for file in files if file.suffix == options['-e']]

    files.sort()

    for file in files:
        print(file)

def delete_file(file_path):
    try:
        if file_path.suffix != ".dsu":
            raise ValueError("Can only delete .dsu files")
        file_path.unlink()
        print(f"{file_path} deleted")
    except FileNotFoundError:
        print("File not found")
    except ValueError as e:
        print(e)

def read_file(file_path):
    try:
        if file_path.suffix != ".dsu":
            raise ValueError("Can only read .dsu files")
        if not file_path.exists():
            raise FileNotFoundError("File does not exist")
        with file_path.open() as file:
            content = file.read().strip()
            print(content if content else "File is empty")
    except FileNotFoundError as e:
        print(e)
    except ValueError as e:
        print(e)

def main():
    current_profile = None
    current_filename = None

    while True:
        choice = ui.user_interface()

        if choice == 'c':
            directory = input("Enter the directory where the file should be created: ")
            name = input("What is the name of the new DSU file? ")
            ui.create_profile(directory, name)
            current_filename = Path(directory) / f"{name}.dsu"
        elif choice == 'l':
            filename = input("Enter the full path to the DSU file you would like to load: ")
            current_profile = ui.load_profile(Path(filename))
            current_filename = Path(filename)
        elif choice == 'p' and current_profile:
            ui.publish_post(current_profile)
        elif choice == 'u' and current_profile:
            ui.update_bio(current_profile)
        elif choice == 'v' and current_profile:
            ui.view_profile_info(current_profile)
        elif choice == 'admin':
            ui.admin_mode(current_profile)
        elif choice == 'q':
            break
        else:
            print("Invalid option or no profile loaded. Please choose 'c' to create or 'l' to load a profile.")

if __name__ == "__main__":
    main()
