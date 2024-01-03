import requests

class Repository:
    def __init__(self, name, description, stars, forks, url):
        self.name = name
        self.description = description
        self.stars = stars
        self.forks = forks
        self.url = url

    def display_details(self):
        print(f"\nRepository: {self.name}")
        print(f"Description: {self.description}")
        print(f"Stars: {self.stars}")
        print(f"Forks: {self.forks}")
        print(f"URL: {self.url}")

class GitHubCLI:
    def __init__(self):
        self.username = None
        self.repositories = []

    def get_user_input(self):
        self.username = input("Enter your GitHub username: ")

    def fetch_repositories(self):
        api_url = f"https://api.github.com/users/{self.username}/repos"
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            self.repositories = [Repository(repo['name'], repo['description'], repo['stargazers_count'],
                                           repo['forks_count'], repo['html_url']) for repo in data]
        else:
            print("Failed to fetch repositories. Please check your username and try again.")
            exit()

    def display_repositories(self):
        print("\nYour Repositories:")
        for index, repo in enumerate(self.repositories, start=1):
            print(f"{index}. {repo.name}")

    def run(self):
        self.get_user_input()
        self.fetch_repositories()
        self.display_repositories()

        while True:
            try:
                repo_index = int(input("\nEnter the number of the repository to view details (0 to exit): "))
                if repo_index == 0:
                    print("Goodbye!")
                    break
                elif 1 <= repo_index <= len(self.repositories):
                    selected_repo = self.repositories[repo_index - 1]
                    selected_repo.display_details()
                else:
                    print("Invalid input. Please enter a valid repository number.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    github_cli = GitHubCLI()
    github_cli.run()
